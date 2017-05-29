# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496046521.745268
_enable_loop = True
_template_filename = 'themes/zen/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_js', 'content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('annotations', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'annotations')] = ns

    ns = runtime.TemplateNamespace('arusahni', context._clean_inheritance_tokens(), templateuri='arusahni_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'arusahni')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\r\n')
        __M_writer(str(arusahni.html_headstart()))
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\r\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\r\n</head>\r\n<body>\r\n    <section class="social">\r\n        <ul>\r\n')
        if logo_url:
            __M_writer('            <li>\r\n                <a href="')
            __M_writer(str(abs_link(_link("root", None, lang))))
            __M_writer('">\r\n                    <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" id="logo">\r\n                </a>\r\n            </li>\r\n')
        __M_writer('        ')
        __M_writer(str(arusahni.html_navigation_links()))
        __M_writer('\r\n        </ul>\r\n    </section>\r\n    <section class="page-content">\r\n        <div class="content" rel="main">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n             ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\r\n        </div>\r\n    </section>\r\n    ')
        __M_writer(str(body_end))
        __M_writer('\r\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\r\n    ')
        __M_writer(str(arusahni.late_load_js()))
        __M_writer('\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <script type="text/javascript">\r\n            $(function(){\r\n                $(\'.timeago\').timeago();\r\n            });\r\n        </script>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'arusahni')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"67": 9, "68": 10, "69": 10, "70": 15, "71": 16, "72": 17, "73": 17, "74": 18, "75": 18, "76": 18, "77": 18, "78": 22, "79": 22, "80": 22, "90": 32, "85": 27, "86": 28, "23": 4, "88": 31, "89": 31, "26": 2, "91": 32, "92": 33, "29": 3, "133": 7, "32": 0, "98": 40, "87": 28, "104": 34, "148": 142, "142": 7, "93": 33, "113": 34, "119": 27, "56": 2, "57": 3, "58": 4, "59": 5, "60": 5, "61": 6, "62": 6}, "source_encoding": "utf-8", "uri": "base.tmpl", "filename": "themes/zen/templates/base.tmpl"}
__M_END_METADATA
"""
