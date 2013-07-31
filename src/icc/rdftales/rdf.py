import re
import ast


from chameleon.tales import TalesExpr
from chameleon.codegen import template
from chameleon.astutil import load
from chameleon.astutil import Symbol
from chameleon.exc import ExpressionError


marker = object()


def rdf_evaluate(obj, name, further_path, default=marker, request=None):
    """Traverse a single step 'name' relative to the given object."""

    if name == '.':
        return obj

    if name == '..':
        return obj.__parent__

    attr = getattr(obj, name, marker)
    if attr is not marker:
        return attr

    if hasattr(obj, '__getitem__'):
        try:
            return obj[name]
        except KeyError:
            pass

    raise AttributeError(name)


def path_traverse(base, econtext, call, path_items):
    if path_items:
        request = econtext.get('request')
        path_items = list(path_items)
        path_items.reverse()

        while len(path_items):
            name = path_items.pop()

            # special-case dicts for performance reasons
            if isinstance(base, dict):
                next = base.get(name, marker)
            else:
                next = getattr(base, name, marker)

            if next is not marker:
                base = next
            else:
                base = traverse(
                    base, name, path_items, request=request)

    if call and getattr(base, '__call__', marker) is not marker:
        return base()

    return base


class RDFExpr(TalesExpr):
    rdf_regex = re.compile(
        r'^(\s*(?:(?:(?:nocall|not|exists):\s*)*(?:[A-Za-z_][A-Za-z0-9_:]*\s*)'+
        r'(?:(?:[A-Za-z_][A-Za-z0-9_:]*:\s*)?)(?:[?A-Za-z_@\-+][?A-Za-z0-9_@\-\.+]*)\s*)*)$')

    interpolation_regex = re.compile(
        r'\?[A-Za-z][A-Za-z0-9_]+')

    traverser = Symbol(rdf_evaluate)

    def translate(self, string, target):
        """
        >>> from chameleon.tales import test
        >>> test(PathExpr('')) is None
        True
        """

        string = string.strip()

        if not string:
            return template("target = None", target=target)

        m = self.path_regex.match(string)
        if m is None:
            raise ExpressionError("Not a valid path-expression.", string)

        nocall, path = m.groups()

        # note that unicode paths are not allowed
        parts = str(path).split('/')

        components = []
        for part in parts[1:]:
            interpolation_args = []

            def replace(match):
                start, end = match.span()
                interpolation_args.append(
                    part[start + 1:end])
                return "%s"

            while True:
                part, count = self.interpolation_regex.subn(replace, part)
                if count == 0:
                    break

            if len(interpolation_args):
                component = template(
                    "format % args", format=ast.Str(part),
                    args=ast.Tuple(
                        list(map(load, interpolation_args)),
                        ast.Load()
                    ),
                    mode="eval")
            else:
                component = ast.Str(part)

            components.append(component)

        base = parts[0]

        if not components:
            if len(parts) == 1 and (nocall or base == 'None'):
                return template("target = base", base=base, target=target)
            else:
                components = ()

        call = template(
            "traverse(base, econtext, call, path_items)",
            traverse=self.traverser,
            base=load(base),
            call=load(str(not nocall)),
            path_items=ast.Tuple(elts=components),
            mode="eval",
        )

        return template("target = value", target=target, value=call)


if __name__=="__main__":
    # some tests:
    m=RDFExpr.rdf_regex.match(' not: exists: subj FOAF:mailTo FOAF:text hasMobileNo not:exists:milk')
    print m.groups()
