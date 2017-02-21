# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487709580.1520119
_enable_loop = True
_template_filename = 'c:/users/john paton/appdata/local/programs/python/python35-32/lib/site-packages/nikola/data/themes/base/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'sourcelink', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        def content():
            return render_content(context._locals(__M_locals))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        def content():
            return render_content(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ul>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i\n        class="icon-folder-open"></i>&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        if photo_array:
            __M_writer('    <ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('            <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(str(image['title']))
                __M_writer('">\n                <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" /></a>\n')
            __M_writer('    </ul>\n')
        if site_has_comments and enable_comments:
            __M_writer('    ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_head():
            return render_extra_head(context)
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "c:/users/john paton/appdata/local/programs/python/python35-32/lib/site-packages/nikola/data/themes/base/templates/gallery.tmpl", "uri": "gallery.tmpl", "line_map": {"128": 29, "129": 31, "130": 33, "131": 34, "132": 34, "133": 34, "139": 5, "23": 4, "152": 38, "26": 3, "32": 0, "161": 38, "162": 39, "163": 39, "169": 163, "56": 2, "57": 3, "58": 4, "63": 5, "68": 36, "73": 41, "79": 7, "97": 7, "98": 8, "99": 8, "100": 9, "101": 10, "102": 10, "103": 10, "104": 12, "105": 13, "106": 14, "107": 14, "108": 17, "109": 18, "110": 19, "111": 20, "112": 20, "113": 20, "114": 21, "115": 21, "116": 23, "117": 25, "118": 26, "119": 27, "120": 28, "121": 28, "122": 28, "123": 28, "124": 28, "125": 29, "126": 29, "127": 29}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
