# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487708736.915452
_enable_loop = True
_template_filename = 'c:/users/john paton/appdata/local/programs/python/python35-32/lib/site-packages/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_headstart', 'html_feedlinks', 'late_load_js', 'html_stylesheets']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        use_cdn = context.get('use_cdn', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        title = context.get('title', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        description = context.get('description', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n    <meta name="generator" content="Nikola (getnikola.com)">\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_helper.tmpl", "filename": "c:/users/john paton/appdata/local/programs/python/python35-32/lib/site-packages/nikola/data/themes/base/templates/base_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 68, "23": 72, "24": 93, "25": 116, "26": 126, "32": 118, "42": 118, "43": 120, "44": 121, "45": 122, "46": 122, "47": 122, "48": 122, "49": 122, "50": 122, "51": 122, "52": 125, "58": 3, "87": 3, "88": 6, "89": 7, "90": 8, "91": 10, "92": 11, "93": 13, "94": 14, "95": 15, "96": 17, "97": 18, "98": 21, "99": 21, "100": 21, "101": 24, "102": 25, "103": 25, "104": 25, "105": 27, "106": 28, "107": 28, "108": 28, "109": 30, "110": 31, "111": 32, "112": 32, "113": 32, "114": 33, "115": 34, "116": 34, "117": 34, "118": 34, "119": 34, "120": 36, "121": 37, "122": 37, "123": 38, "124": 38, "125": 40, "126": 40, "127": 41, "128": 41, "129": 43, "130": 44, "131": 45, "132": 45, "133": 45, "134": 45, "135": 45, "136": 45, "137": 45, "138": 48, "139": 49, "140": 50, "141": 50, "142": 50, "143": 52, "144": 53, "145": 54, "146": 54, "147": 54, "148": 56, "149": 57, "150": 57, "151": 57, "152": 59, "153": 60, "154": 60, "155": 61, "156": 62, "157": 63, "158": 64, "159": 64, "160": 64, "161": 66, "162": 67, "163": 67, "169": 95, "180": 95, "181": 96, "182": 97, "183": 97, "184": 97, "185": 98, "186": 99, "187": 100, "188": 101, "189": 101, "190": 101, "191": 101, "192": 101, "193": 103, "194": 104, "195": 104, "196": 104, "197": 107, "198": 108, "199": 109, "200": 110, "201": 110, "202": 110, "203": 110, "204": 110, "205": 112, "206": 113, "207": 113, "208": 113, "214": 70, "219": 70, "220": 71, "221": 71, "227": 74, "235": 74, "236": 75, "237": 76, "238": 77, "239": 78, "240": 79, "241": 81, "242": 82, "243": 85, "244": 86, "245": 89, "246": 90, "252": 246}}
__M_END_METADATA
"""
