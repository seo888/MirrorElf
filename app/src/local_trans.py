import httpx


class LocalTrans():

    def __init__(self, url="http://127.0.0.1:5000/translate"):
        self.url = url

    def trans(self, querry, lang="auto", to_lang="zh"):
        data = {
            "q": querry,
            "source": lang,
            "target": to_lang,
            "format": "text",
            "alternatives": 0,
            "api_key": ""
        }
        with httpx.Client() as client:
            response = client.post(self.url, timeout=30, json=data)
        return response.json()['translatedText']

    def web_trans(self, source, lang="auto", to_lang="zh"):
        data = {
            "q": source,
            "source": lang,
            "target": to_lang,
            "format": "text",
            "alternatives": 0,
            "api_key": ""
        }
        with httpx.Client() as client:
            response = client.post(self.url, timeout=30, json=data)
        return response.json()


if __name__ == "__main__":
    translator = LocalTrans(url="http://38.34.175.146:5000/translate")
    source = """
<!DOCTYPE html>
<html lang="en-US">
<head>
	<meta charset="UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<link rel="pingback" href="https://fcmc.org/xmlrpc.php" />

	<script type="text/javascript">
		document.documentElement.className = 'js';
	</script>
	
	<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
<script type="text/javascript">
			let jqueryParams=[],jQuery=function(r){return jqueryParams=[...jqueryParams,r],jQuery},$=function(r){return jqueryParams=[...jqueryParams,r],$};window.jQuery=jQuery,window.$=jQuery;let customHeadScripts=!1;jQuery.fn=jQuery.prototype={},$.fn=jQuery.prototype={},jQuery.noConflict=function(r){if(window.jQuery)return jQuery=window.jQuery,$=window.jQuery,customHeadScripts=!0,jQuery.noConflict},jQuery.ready=function(r){jqueryParams=[...jqueryParams,r]},$.ready=function(r){jqueryParams=[...jqueryParams,r]},jQuery.load=function(r){jqueryParams=[...jqueryParams,r]},$.load=function(r){jqueryParams=[...jqueryParams,r]},jQuery.fn.ready=function(r){jqueryParams=[...jqueryParams,r]},$.fn.ready=function(r){jqueryParams=[...jqueryParams,r]};</script>
	<!-- This site is optimized with the Yoast SEO plugin v23.7 - https://yoast.com/wordpress/plugins/seo/ -->
	<title>Services | Franklin County Medical Center | Preston, ID</title>
	<meta name="description" content="Discover a comprehensive range of healthcare services at Franklin County Medical Center. From primary care to specialized treatments, we offer cutting-edge medical care tailored to your needs." />
	<link rel="canonical" href="https://fcmc.org/services/" />
	<meta property="og:locale" content="en_US" />
	<meta property="og:type" content="article" />
	<meta property="og:title" content="Services | Franklin County Medical Center | Preston, ID" />
	<meta property="og:description" content="Discover a comprehensive range of healthcare services at Franklin County Medical Center. From primary care to specialized treatments, we offer cutting-edge medical care tailored to your needs." />
	<meta property="og:url" content="https://fcmc.org/services/" />
	<meta property="og:site_name" content="Franklin County Medical Center" />
	<meta property="article:modified_time" content="2024-04-11T19:53:57+00:00" />
	<meta name="twitter:card" content="summary_large_image" />
	<meta name="twitter:label1" content="Est. reading time" />
	<meta name="twitter:data1" content="1 minute" />
	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://fcmc.org/services/","url":"https://fcmc.org/services/","name":"Services | Franklin County Medical Center | Preston, ID","isPartOf":{"@id":"https://fcmc.org/#website"},"datePublished":"2023-09-11T18:46:17+00:00","dateModified":"2024-04-11T19:53:57+00:00","description":"Discover a comprehensive range of healthcare services at Franklin County Medical Center. From primary care to specialized treatments, we offer cutting-edge medical care tailored to your needs.","breadcrumb":{"@id":"https://fcmc.org/services/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://fcmc.org/services/"]}]},{"@type":"BreadcrumbList","@id":"https://fcmc.org/services/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://fcmc.org/"},{"@type":"ListItem","position":2,"name":"Services"}]},{"@type":"WebSite","@id":"https://fcmc.org/#website","url":"https://fcmc.org/","name":"Franklin County Medical Center","description":"","potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://fcmc.org/?s={search_term_string}"},"query-input":{"@type":"PropertyValueSpecification","valueRequired":true,"valueName":"search_term_string"}}],"inLanguage":"en-US"}]}</script>
	<!-- / Yoast SEO plugin. -->


<link rel='dns-prefetch' href='//fonts.googleapis.com' />
<link rel="alternate" type="application/rss+xml" title="Franklin County Medical Center &raquo; Feed" href="https://fcmc.org/feed/" />
<link rel="alternate" type="application/rss+xml" title="Franklin County Medical Center &raquo; Comments Feed" href="https://fcmc.org/comments/feed/" />
<meta content="Franklin County Medical Center v.1.0" name="generator"/><style id='wp-block-library-theme-inline-css' type='text/css'>
.wp-block-audio :where(figcaption){color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-audio :where(figcaption){color:#ffffffa6}.wp-block-audio{margin:0 0 1em}.wp-block-code{border:1px solid #ccc;border-radius:4px;font-family:Menlo,Consolas,monaco,monospace;padding:.8em 1em}.wp-block-embed :where(figcaption){color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-embed :where(figcaption){color:#ffffffa6}.wp-block-embed{margin:0 0 1em}.blocks-gallery-caption{color:#555;font-size:13px;text-align:center}.is-dark-theme .blocks-gallery-caption{color:#ffffffa6}:root :where(.wp-block-image figcaption){color:#555;font-size:13px;text-align:center}.is-dark-theme :root :where(.wp-block-image figcaption){color:#ffffffa6}.wp-block-image{margin:0 0 1em}.wp-block-pullquote{border-bottom:4px solid;border-top:4px solid;color:currentColor;margin-bottom:1.75em}.wp-block-pullquote cite,.wp-block-pullquote footer,.wp-block-pullquote__citation{color:currentColor;font-size:.8125em;font-style:normal;text-transform:uppercase}.wp-block-quote{border-left:.25em solid;margin:0 0 1.75em;padding-left:1em}.wp-block-quote cite,.wp-block-quote footer{color:currentColor;font-size:.8125em;font-style:normal;position:relative}.wp-block-quote.has-text-align-right{border-left:none;border-right:.25em solid;padding-left:0;padding-right:1em}.wp-block-quote.has-text-align-center{border:none;padding-left:0}.wp-block-quote.is-large,.wp-block-quote.is-style-large,.wp-block-quote.is-style-plain{border:none}.wp-block-search .wp-block-search__label{font-weight:700}.wp-block-search__button{border:1px solid #ccc;padding:.375em .625em}:where(.wp-block-group.has-background){padding:1.25em 2.375em}.wp-block-separator.has-css-opacity{opacity:.4}.wp-block-separator{border:none;border-bottom:2px solid;margin-left:auto;margin-right:auto}.wp-block-separator.has-alpha-channel-opacity{opacity:1}.wp-block-separator:not(.is-style-wide):not(.is-style-dots){width:100px}.wp-block-separator.has-background:not(.is-style-dots){border-bottom:none;height:1px}.wp-block-separator.has-background:not(.is-style-wide):not(.is-style-dots){height:2px}.wp-block-table{margin:0 0 1em}.wp-block-table td,.wp-block-table th{word-break:normal}.wp-block-table :where(figcaption){color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-table :where(figcaption){color:#ffffffa6}.wp-block-video :where(figcaption){color:#555;font-size:13px;text-align:center}.is-dark-theme .wp-block-video :where(figcaption){color:#ffffffa6}.wp-block-video{margin:0 0 1em}:root :where(.wp-block-template-part.has-background){margin-bottom:0;margin-top:0;padding:1.25em 2.375em}
</style>
<style id='global-styles-inline-css' type='text/css'>
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:root { --wp--style--global--content-size: 823px;--wp--style--global--wide-size: 1080px; }:where(body) { margin: 0; }.wp-site-blocks > .alignleft { float: left; margin-right: 2em; }.wp-site-blocks > .alignright { float: right; margin-left: 2em; }.wp-site-blocks > .aligncenter { justify-content: center; margin-left: auto; margin-right: auto; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}.is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}a:where(:not(.wp-element-button)){text-decoration: underline;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;line-height: inherit;padding: calc(0.667em + 2px) calc(1.333em + 2px);text-decoration: none;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
:root :where(.wp-block-pullquote){font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='wtfdivi-user-css-css' href='https://fcmc.org/wp-content/uploads/wtfdivi/wp_head.css?ver=1708716144' type='text/css' media='all' />
<style id='divi-style-parent-inline-inline-css' type='text/css'>
/*!
Theme Name: Divi
Theme URI: http://www.elegantthemes.com/gallery/divi/
Version: 4.25.1
Description: Smart. Flexible. Beautiful. Divi is the most powerful theme in our collection.
Author: Elegant Themes
Author URI: http://www.elegantthemes.com
License: GNU General Public License v2
License URI: http://www.gnu.org/licenses/gpl-2.0.html
*/

a,abbr,acronym,address,applet,b,big,blockquote,body,center,cite,code,dd,del,dfn,div,dl,dt,em,fieldset,font,form,h1,h2,h3,h4,h5,h6,html,i,iframe,img,ins,kbd,label,legend,li,object,ol,p,pre,q,s,samp,small,span,strike,strong,sub,sup,tt,u,ul,var{margin:0;padding:0;border:0;outline:0;font-size:100%;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;vertical-align:baseline;background:transparent}body{line-height:1}ol,ul{list-style:none}blockquote,q{quotes:none}blockquote:after,blockquote:before,q:after,q:before{content:"";content:none}blockquote{margin:20px 0 30px;border-left:5px solid;padding-left:20px}:focus{outline:0}del{text-decoration:line-through}pre{overflow:auto;padding:10px}figure{margin:0}table{border-collapse:collapse;border-spacing:0}article,aside,footer,header,hgroup,nav,section{display:block}body{font-family:Open Sans,Arial,sans-serif;font-size:14px;color:#666;background-color:#fff;line-height:1.7em;font-weight:500;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}body.page-template-page-template-blank-php #page-container{padding-top:0!important}body.et_cover_background{background-size:cover!important;background-position:top!important;background-repeat:no-repeat!important;background-attachment:fixed}a{color:#2ea3f2}a,a:hover{text-decoration:none}p{padding-bottom:1em}p:not(.has-background):last-of-type{padding-bottom:0}p.et_normal_padding{padding-bottom:1em}strong{font-weight:700}cite,em,i{font-style:italic}code,pre{font-family:Courier New,monospace;margin-bottom:10px}ins{text-decoration:none}sub,sup{height:0;line-height:1;position:relative;vertical-align:baseline}sup{bottom:.8em}sub{top:.3em}dl{margin:0 0 1.5em}dl dt{font-weight:700}dd{margin-left:1.5em}blockquote p{padding-bottom:0}embed,iframe,object,video{max-width:100%}h1,h2,h3,h4,h5,h6{color:#333;padding-bottom:10px;line-height:1em;font-weight:500}h1 a,h2 a,h3 a,h4 a,h5 a,h6 a{color:inherit}h1{font-size:30px}h2{font-size:26px}h3{font-size:22px}h4{font-size:18px}h5{font-size:16px}h6{font-size:14px}input{-webkit-appearance:none}input[type=checkbox]{-webkit-appearance:checkbox}input[type=radio]{-webkit-appearance:radio}input.text,input.title,input[type=email],input[type=password],input[type=tel],input[type=text],select,textarea{background-color:#fff;border:1px solid #bbb;padding:2px;color:#4e4e4e}input.text:focus,input.title:focus,input[type=text]:focus,select:focus,textarea:focus{border-color:#2d3940;color:#3e3e3e}input.text,input.title,input[type=text],select,textarea{margin:0}textarea{padding:4px}button,input,select,textarea{font-family:inherit}img{max-width:100%;height:auto}.clear{clear:both}br.clear{margin:0;padding:0}.pagination{clear:both}#et_search_icon:hover,.et-social-icon a:hover,.et_password_protected_form .et_submit_button,.form-submit .et_pb_buttontton.alt.disabled,.nav-single a,.posted_in a{color:#2ea3f2}.et-search-form,blockquote{border-color:#2ea3f2}#main-content{background-color:#fff}.container{width:80%;max-width:1080px;margin:auto;position:relative}body:not(.et-tb) #main-content .container,body:not(.et-tb-has-header) #main-content .container{padding-top:58px}.et_full_width_page #main-content .container:before{display:none}.main_title{margin-bottom:20px}.et_password_protected_form .et_submit_button:hover,.form-submit .et_pb_button:hover{background:rgba(0,0,0,.05)}.et_button_icon_visible .et_pb_button{padding-right:2em;padding-left:.7em}.et_button_icon_visible .et_pb_button:after{opacity:1;margin-left:0}.et_button_left .et_pb_button:hover:after{left:.15em}.et_button_left .et_pb_button:after{margin-left:0;left:1em}.et_button_icon_visible.et_button_left .et_pb_button,.et_button_left .et_pb_button:hover,.et_button_left .et_pb_module .et_pb_button:hover{padding-left:2em;padding-right:.7em}.et_button_icon_visible.et_button_left .et_pb_button:after,.et_button_left .et_pb_button:hover:after{left:.15em}.et_password_protected_form .et_submit_button:hover,.form-submit .et_pb_button:hover{padding:.3em 1em}.et_button_no_icon .et_pb_button:after{display:none}.et_button_no_icon.et_button_icon_visible.et_button_left .et_pb_button,.et_button_no_icon.et_button_left .et_pb_button:hover,.et_button_no_icon .et_pb_button,.et_button_no_icon .et_pb_button:hover{padding:.3em 1em!important}.et_button_custom_icon .et_pb_button:after{line-height:1.7em}.et_button_custom_icon.et_button_icon_visible .et_pb_button:after,.et_button_custom_icon .et_pb_button:hover:after{margin-left:.3em}#left-area .post_format-post-format-gallery .wp-block-gallery:first-of-type{padding:0;margin-bottom:-16px}.entry-content table:not(.variations){border:1px solid #eee;margin:0 0 15px;text-align:left;width:100%}.entry-content thead th,.entry-content tr th{color:#555;font-weight:700;padding:9px 24px}.entry-content tr td{border-top:1px solid #eee;padding:6px 24px}#left-area ul,.entry-content ul,.et-l--body ul,.et-l--footer ul,.et-l--header ul{list-style-type:disc;padding:0 0 23px 1em;line-height:26px}#left-area ol,.entry-content ol,.et-l--body ol,.et-l--footer ol,.et-l--header ol{list-style-type:decimal;list-style-position:inside;padding:0 0 23px;line-height:26px}#left-area ul li ul,.entry-content ul li ol{padding:2px 0 2px 20px}#left-area ol li ul,.entry-content ol li ol,.et-l--body ol li ol,.et-l--footer ol li ol,.et-l--header ol li ol{padding:2px 0 2px 35px}#left-area ul.wp-block-gallery{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;list-style-type:none;padding:0}#left-area ul.products{padding:0!important;line-height:1.7!important;list-style:none!important}.gallery-item a{display:block}.gallery-caption,.gallery-item a{width:90%}#wpadminbar{z-index:100001}#left-area .post-meta{font-size:14px;padding-bottom:15px}#left-area .post-meta a{text-decoration:none;color:#666}#left-area .et_featured_image{padding-bottom:7px}.single .post{padding-bottom:25px}body.single .et_audio_content{margin-bottom:-6px}.nav-single a{text-decoration:none;color:#2ea3f2;font-size:14px;font-weight:400}.nav-previous{float:left}.nav-next{float:right}.et_password_protected_form p input{background-color:#eee;border:none!important;width:100%!important;border-radius:0!important;font-size:14px;color:#999!important;padding:16px!important;-webkit-box-sizing:border-box;box-sizing:border-box}.et_password_protected_form label{display:none}.et_password_protected_form .et_submit_button{font-family:inherit;display:block;float:right;margin:8px auto 0;cursor:pointer}.post-password-required p.nocomments.container{max-width:100%}.post-password-required p.nocomments.container:before{display:none}.aligncenter,div.post .new-post .aligncenter{display:block;margin-left:auto;margin-right:auto}.wp-caption{border:1px solid #ddd;text-align:center;background-color:#f3f3f3;margin-bottom:10px;max-width:96%;padding:8px}.wp-caption.alignleft{margin:0 30px 20px 0}.wp-caption.alignright{margin:0 0 20px 30px}.wp-caption img{margin:0;padding:0;border:0}.wp-caption p.wp-caption-text{font-size:12px;padding:0 4px 5px;margin:0}.alignright{float:right}.alignleft{float:left}img.alignleft{display:inline;float:left;margin-right:15px}img.alignright{display:inline;float:right;margin-left:15px}.page.et_pb_pagebuilder_layout #main-content{background-color:transparent}body #main-content .et_builder_inner_content>h1,body #main-content .et_builder_inner_content>h2,body #main-content .et_builder_inner_content>h3,body #main-content .et_builder_inner_content>h4,body #main-content .et_builder_inner_content>h5,body #main-content .et_builder_inner_content>h6{line-height:1.4em}body #main-content .et_builder_inner_content>p{line-height:1.7em}.wp-block-pullquote{margin:20px 0 30px}.wp-block-pullquote.has-background blockquote{border-left:none}.wp-block-group.has-background{padding:1.5em 1.5em .5em}@media (min-width:981px){#left-area{width:79.125%;padding-bottom:23px}#main-content .container:before{content:"";position:absolute;top:0;height:100%;width:1px;background-color:#e2e2e2}.et_full_width_page #left-area,.et_no_sidebar #left-area{float:none;width:100%!important}.et_full_width_page #left-area{padding-bottom:0}.et_no_sidebar #main-content .container:before{display:none}}@media (max-width:980px){#page-container{padding-top:80px}.et-tb #page-container,.et-tb-has-header #page-container{padding-top:0!important}#left-area,#sidebar{width:100%!important}#main-content .container:before{display:none!important}.et_full_width_page .et_gallery_item:nth-child(4n+1){clear:none}}@media print{#page-container{padding-top:0!important}}#wp-admin-bar-et-use-visual-builder a:before{font-family:ETmodules!important;content:"\e625";font-size:30px!important;width:28px;margin-top:-3px;color:#974df3!important}#wp-admin-bar-et-use-visual-builder:hover a:before{color:#fff!important}#wp-admin-bar-et-use-visual-builder:hover a,#wp-admin-bar-et-use-visual-builder a:hover{transition:background-color .5s ease;-webkit-transition:background-color .5s ease;-moz-transition:background-color .5s ease;background-color:#7e3bd0!important;color:#fff!important}* html .clearfix,:first-child+html .clearfix{zoom:1}.iphone .et_pb_section_video_bg video::-webkit-media-controls-start-playback-button{display:none!important;-webkit-appearance:none}.et_mobile_device .et_pb_section_parallax .et_pb_parallax_css{background-attachment:scroll}.et-social-facebook a.icon:before{content:"\e093"}.et-social-twitter a.icon:before{content:"\e094"}.et-social-google-plus a.icon:before{content:"\e096"}.et-social-instagram a.icon:before{content:"\e09a"}.et-social-rss a.icon:before{content:"\e09e"}.ai1ec-single-event:after{content:" ";display:table;clear:both}.evcal_event_details .evcal_evdata_cell .eventon_details_shading_bot.eventon_details_shading_bot{z-index:3}.wp-block-divi-layout{margin-bottom:1em}*{-webkit-box-sizing:border-box;box-sizing:border-box}#et-info-email:before,#et-info-phone:before,#et_search_icon:before,.comment-reply-link:after,.et-cart-info span:before,.et-pb-arrow-next:before,.et-pb-arrow-prev:before,.et-social-icon a:before,.et_audio_container .mejs-playpause-button button:before,.et_audio_container .mejs-volume-button button:before,.et_overlay:before,.et_password_protected_form .et_submit_button:after,.et_pb_button:after,.et_pb_contact_reset:after,.et_pb_contact_submit:after,.et_pb_font_icon:before,.et_pb_newsletter_button:after,.et_pb_pricing_table_button:after,.et_pb_promo_button:after,.et_pb_testimonial:before,.et_pb_toggle_title:before,.form-submit .et_pb_button:after,.mobile_menu_bar:before,a.et_pb_more_button:after{font-family:ETmodules!important;speak:none;font-style:normal;font-weight:400;-webkit-font-feature-settings:normal;font-feature-settings:normal;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-shadow:0 0;direction:ltr}.et-pb-icon,.et_pb_custom_button_icon.et_pb_button:after,.et_pb_login .et_pb_custom_button_icon.et_pb_button:after,.et_pb_woo_custom_button_icon .button.et_pb_custom_button_icon.et_pb_button:after,.et_pb_woo_custom_button_icon .button.et_pb_custom_button_icon.et_pb_button:hover:after{content:attr(data-icon)}.et-pb-icon{font-family:ETmodules;speak:none;font-weight:400;-webkit-font-feature-settings:normal;font-feature-settings:normal;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;font-size:96px;font-style:normal;display:inline-block;-webkit-box-sizing:border-box;box-sizing:border-box;direction:ltr}#et-ajax-saving{display:none;-webkit-transition:background .3s,-webkit-box-shadow .3s;transition:background .3s,-webkit-box-shadow .3s;transition:background .3s,box-shadow .3s;transition:background .3s,box-shadow .3s,-webkit-box-shadow .3s;-webkit-box-shadow:rgba(0,139,219,.247059) 0 0 60px;box-shadow:0 0 60px rgba(0,139,219,.247059);position:fixed;top:50%;left:50%;width:50px;height:50px;background:#fff;border-radius:50px;margin:-25px 0 0 -25px;z-index:999999;text-align:center}#et-ajax-saving img{margin:9px}.et-safe-mode-indicator,.et-safe-mode-indicator:focus,.et-safe-mode-indicator:hover{-webkit-box-shadow:0 5px 10px rgba(41,196,169,.15);box-shadow:0 5px 10px rgba(41,196,169,.15);background:#29c4a9;color:#fff;font-size:14px;font-weight:600;padding:12px;line-height:16px;border-radius:3px;position:fixed;bottom:30px;right:30px;z-index:999999;text-decoration:none;font-family:Open Sans,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.et_pb_button{font-size:20px;font-weight:500;padding:.3em 1em;line-height:1.7em!important;background-color:transparent;background-size:cover;background-position:50%;background-repeat:no-repeat;border:2px solid;border-radius:3px;-webkit-transition-duration:.2s;transition-duration:.2s;-webkit-transition-property:all!important;transition-property:all!important}.et_pb_button,.et_pb_button_inner{position:relative}.et_pb_button:hover,.et_pb_module .et_pb_button:hover{border:2px solid transparent;padding:.3em 2em .3em .7em}.et_pb_button:hover{background-color:hsla(0,0%,100%,.2)}.et_pb_bg_layout_light.et_pb_button:hover,.et_pb_bg_layout_light .et_pb_button:hover{background-color:rgba(0,0,0,.05)}.et_pb_button:after,.et_pb_button:before{font-size:32px;line-height:1em;content:"\35";opacity:0;position:absolute;margin-left:-1em;-webkit-transition:all .2s;transition:all .2s;text-transform:none;-webkit-font-feature-settings:"kern" off;font-feature-settings:"kern" off;font-variant:none;font-style:normal;font-weight:400;text-shadow:none}.et_pb_button.et_hover_enabled:hover:after,.et_pb_button.et_pb_hovered:hover:after{-webkit-transition:none!important;transition:none!important}.et_pb_button:before{display:none}.et_pb_button:hover:after{opacity:1;margin-left:0}.et_pb_column_1_3 h1,.et_pb_column_1_4 h1,.et_pb_column_1_5 h1,.et_pb_column_1_6 h1,.et_pb_column_2_5 h1{font-size:26px}.et_pb_column_1_3 h2,.et_pb_column_1_4 h2,.et_pb_column_1_5 h2,.et_pb_column_1_6 h2,.et_pb_column_2_5 h2{font-size:23px}.et_pb_column_1_3 h3,.et_pb_column_1_4 h3,.et_pb_column_1_5 h3,.et_pb_column_1_6 h3,.et_pb_column_2_5 h3{font-size:20px}.et_pb_column_1_3 h4,.et_pb_column_1_4 h4,.et_pb_column_1_5 h4,.et_pb_column_1_6 h4,.et_pb_column_2_5 h4{font-size:18px}.et_pb_column_1_3 h5,.et_pb_column_1_4 h5,.et_pb_column_1_5 h5,.et_pb_column_1_6 h5,.et_pb_column_2_5 h5{font-size:16px}.et_pb_column_1_3 h6,.et_pb_column_1_4 h6,.et_pb_column_1_5 h6,.et_pb_column_1_6 h6,.et_pb_column_2_5 h6{font-size:15px}.et_pb_bg_layout_dark,.et_pb_bg_layout_dark h1,.et_pb_bg_layout_dark h2,.et_pb_bg_layout_dark h3,.et_pb_bg_layout_dark h4,.et_pb_bg_layout_dark h5,.et_pb_bg_layout_dark h6{color:#fff!important}.et_pb_module.et_pb_text_align_left{text-align:left}.et_pb_module.et_pb_text_align_center{text-align:center}.et_pb_module.et_pb_text_align_right{text-align:right}.et_pb_module.et_pb_text_align_justified{text-align:justify}.clearfix:after{visibility:hidden;display:block;font-size:0;content:" ";clear:both;height:0}.et_pb_bg_layout_light .et_pb_more_button{color:#2ea3f2}.et_builder_inner_content{position:relative;z-index:1}header .et_builder_inner_content{z-index:2}.et_pb_css_mix_blend_mode_passthrough{mix-blend-mode:unset!important}.et_pb_image_container{margin:-20px -20px 29px}.et_pb_module_inner{position:relative}.et_hover_enabled_preview{z-index:2}.et_hover_enabled:hover{position:relative;z-index:2}.et_pb_all_tabs,.et_pb_module,.et_pb_posts_nav a,.et_pb_tab,.et_pb_with_background{position:relative;background-size:cover;background-position:50%;background-repeat:no-repeat}.et_pb_background_mask,.et_pb_background_pattern{bottom:0;left:0;position:absolute;right:0;top:0}.et_pb_background_mask{background-size:calc(100% + 2px) calc(100% + 2px);background-repeat:no-repeat;background-position:50%;overflow:hidden}.et_pb_background_pattern{background-position:0 0;background-repeat:repeat}.et_pb_with_border{position:relative;border:0 solid #333}.post-password-required .et_pb_row{padding:0;width:100%}.post-password-required .et_password_protected_form{min-height:0}body.et_pb_pagebuilder_layout.et_pb_show_title .post-password-required .et_password_protected_form h1,body:not(.et_pb_pagebuilder_layout) .post-password-required .et_password_protected_form h1{display:none}.et_pb_no_bg{padding:0!important}.et_overlay.et_pb_inline_icon:before,.et_pb_inline_icon:before{content:attr(data-icon)}.et_pb_more_button{color:inherit;text-shadow:none;text-decoration:none;display:inline-block;margin-top:20px}.et_parallax_bg_wrap{overflow:hidden;position:absolute;top:0;right:0;bottom:0;left:0}.et_parallax_bg{background-repeat:no-repeat;background-position:top;background-size:cover;position:absolute;bottom:0;left:0;width:100%;height:100%;display:block}.et_parallax_bg.et_parallax_bg__hover,.et_parallax_bg.et_parallax_bg_phone,.et_parallax_bg.et_parallax_bg_tablet,.et_parallax_gradient.et_parallax_gradient__hover,.et_parallax_gradient.et_parallax_gradient_phone,.et_parallax_gradient.et_parallax_gradient_tablet,.et_pb_section_parallax_hover:hover .et_parallax_bg:not(.et_parallax_bg__hover),.et_pb_section_parallax_hover:hover .et_parallax_gradient:not(.et_parallax_gradient__hover){display:none}.et_pb_section_parallax_hover:hover .et_parallax_bg.et_parallax_bg__hover,.et_pb_section_parallax_hover:hover .et_parallax_gradient.et_parallax_gradient__hover{display:block}.et_parallax_gradient{bottom:0;display:block;left:0;position:absolute;right:0;top:0}.et_pb_module.et_pb_section_parallax,.et_pb_posts_nav a.et_pb_section_parallax,.et_pb_tab.et_pb_section_parallax{position:relative}.et_pb_section_parallax .et_pb_parallax_css,.et_pb_slides .et_parallax_bg.et_pb_parallax_css{background-attachment:fixed}body.et-bfb .et_pb_section_parallax .et_pb_parallax_css,body.et-bfb .et_pb_slides .et_parallax_bg.et_pb_parallax_css{background-attachment:scroll;bottom:auto}.et_pb_section_parallax.et_pb_column .et_pb_module,.et_pb_section_parallax.et_pb_row .et_pb_column,.et_pb_section_parallax.et_pb_row .et_pb_module{z-index:9;position:relative}.et_pb_more_button:hover:after{opacity:1;margin-left:0}.et_pb_preload .et_pb_section_video_bg,.et_pb_preload>div{visibility:hidden}.et_pb_preload,.et_pb_section.et_pb_section_video.et_pb_preload{position:relative;background:#464646!important}.et_pb_preload:before{content:"";position:absolute;top:50%;left:50%;background:url(https://fcmc.org/wp-content/themes/Divi/includes/builder/styles/images/preloader.gif) no-repeat;border-radius:32px;width:32px;height:32px;margin:-16px 0 0 -16px}.box-shadow-overlay{position:absolute;top:0;left:0;width:100%;height:100%;z-index:10;pointer-events:none}.et_pb_section>.box-shadow-overlay~.et_pb_row{z-index:11}body.safari .section_has_divider{will-change:transform}.et_pb_row>.box-shadow-overlay{z-index:8}.has-box-shadow-overlay{position:relative}.et_clickable{cursor:pointer}.screen-reader-text{border:0;clip:rect(1px,1px,1px,1px);-webkit-clip-path:inset(50%);clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute!important;width:1px;word-wrap:normal!important}.et_multi_view_hidden,.et_multi_view_hidden_image{display:none!important}@keyframes multi-view-image-fade{0%{opacity:0}10%{opacity:.1}20%{opacity:.2}30%{opacity:.3}40%{opacity:.4}50%{opacity:.5}60%{opacity:.6}70%{opacity:.7}80%{opacity:.8}90%{opacity:.9}to{opacity:1}}.et_multi_view_image__loading{visibility:hidden}.et_multi_view_image__loaded{-webkit-animation:multi-view-image-fade .5s;animation:multi-view-image-fade .5s}#et-pb-motion-effects-offset-tracker{visibility:hidden!important;opacity:0;position:absolute;top:0;left:0}.et-pb-before-scroll-animation{opacity:0}header.et-l.et-l--header:after{clear:both;display:block;content:""}.et_pb_module{-webkit-animation-timing-function:linear;animation-timing-function:linear;-webkit-animation-duration:.2s;animation-duration:.2s}@-webkit-keyframes fadeBottom{0%{opacity:0;-webkit-transform:translateY(10%);transform:translateY(10%)}to{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}}@keyframes fadeBottom{0%{opacity:0;-webkit-transform:translateY(10%);transform:translateY(10%)}to{opacity:1;-webkit-transform:translateY(0);transform:translateY(0)}}@-webkit-keyframes fadeLeft{0%{opacity:0;-webkit-transform:translateX(-10%);transform:translateX(-10%)}to{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@keyframes fadeLeft{0%{opacity:0;-webkit-transform:translateX(-10%);transform:translateX(-10%)}to{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@-webkit-keyframes fadeRight{0%{opacity:0;-webkit-transform:translateX(10%);transform:translateX(10%)}to{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@keyframes fadeRight{0%{opacity:0;-webkit-transform:translateX(10%);transform:translateX(10%)}to{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@-webkit-keyframes fadeTop{0%{opacity:0;-webkit-transform:translateY(-10%);transform:translateY(-10%)}to{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@keyframes fadeTop{0%{opacity:0;-webkit-transform:translateY(-10%);transform:translateY(-10%)}to{opacity:1;-webkit-transform:translateX(0);transform:translateX(0)}}@-webkit-keyframes fadeIn{0%{opacity:0}to{opacity:1}}@keyframes fadeIn{0%{opacity:0}to{opacity:1}}.et-waypoint:not(.et_pb_counters){opacity:0}@media (min-width:981px){.et_pb_section.et_section_specialty div.et_pb_row .et_pb_column .et_pb_column .et_pb_module.et-last-child,.et_pb_section.et_section_specialty div.et_pb_row .et_pb_column .et_pb_column .et_pb_module:last-child,.et_pb_section.et_section_specialty div.et_pb_row .et_pb_column .et_pb_row_inner .et_pb_column .et_pb_module.et-last-child,.et_pb_section.et_section_specialty div.et_pb_row .et_pb_column .et_pb_row_inner .et_pb_column .et_pb_module:last-child,.et_pb_section div.et_pb_row .et_pb_column .et_pb_module.et-last-child,.et_pb_section div.et_pb_row .et_pb_column .et_pb_module:last-child{margin-bottom:0}}@media (max-width:980px){.et_overlay.et_pb_inline_icon_tablet:before,.et_pb_inline_icon_tablet:before{content:attr(data-icon-tablet)}.et_parallax_bg.et_parallax_bg_tablet_exist,.et_parallax_gradient.et_parallax_gradient_tablet_exist{display:none}.et_parallax_bg.et_parallax_bg_tablet,.et_parallax_gradient.et_parallax_gradient_tablet{display:block}.et_pb_column .et_pb_module{margin-bottom:30px}.et_pb_row .et_pb_column .et_pb_module.et-last-child,.et_pb_row .et_pb_column .et_pb_module:last-child,.et_section_specialty .et_pb_row .et_pb_column .et_pb_module.et-last-child,.et_section_specialty .et_pb_row .et_pb_column .et_pb_module:last-child{margin-bottom:0}.et_pb_more_button{display:inline-block!important}.et_pb_bg_layout_light_tablet.et_pb_button,.et_pb_bg_layout_light_tablet.et_pb_module.et_pb_button,.et_pb_bg_layout_light_tablet .et_pb_more_button{color:#2ea3f2}.et_pb_bg_layout_light_tablet .et_pb_forgot_password a{color:#666}.et_pb_bg_layout_light_tablet h1,.et_pb_bg_layout_light_tablet h2,.et_pb_bg_layout_light_tablet h3,.et_pb_bg_layout_light_tablet h4,.et_pb_bg_layout_light_tablet h5,.et_pb_bg_layout_light_tablet h6{color:#333!important}.et_pb_module .et_pb_bg_layout_light_tablet.et_pb_button{color:#2ea3f2!important}.et_pb_bg_layout_light_tablet{color:#666!important}.et_pb_bg_layout_dark_tablet,.et_pb_bg_layout_dark_tablet h1,.et_pb_bg_layout_dark_tablet h2,.et_pb_bg_layout_dark_tablet h3,.et_pb_bg_layout_dark_tablet h4,.et_pb_bg_layout_dark_tablet h5,.et_pb_bg_layout_dark_tablet h6{color:#fff!important}.et_pb_bg_layout_dark_tablet.et_pb_button,.et_pb_bg_layout_dark_tablet.et_pb_module.et_pb_button,.et_pb_bg_layout_dark_tablet .et_pb_more_button{color:inherit}.et_pb_bg_layout_dark_tablet .et_pb_forgot_password a{color:#fff}.et_pb_module.et_pb_text_align_left-tablet{text-align:left}.et_pb_module.et_pb_text_align_center-tablet{text-align:center}.et_pb_module.et_pb_text_align_right-tablet{text-align:right}.et_pb_module.et_pb_text_align_justified-tablet{text-align:justify}}@media (max-width:767px){.et_pb_more_button{display:inline-block!important}.et_overlay.et_pb_inline_icon_phone:before,.et_pb_inline_icon_phone:before{content:attr(data-icon-phone)}.et_parallax_bg.et_parallax_bg_phone_exist,.et_parallax_gradient.et_parallax_gradient_phone_exist{display:none}.et_parallax_bg.et_parallax_bg_phone,.et_parallax_gradient.et_parallax_gradient_phone{display:block}.et-hide-mobile{display:none!important}.et_pb_bg_layout_light_phone.et_pb_button,.et_pb_bg_layout_light_phone.et_pb_module.et_pb_button,.et_pb_bg_layout_light_phone .et_pb_more_button{color:#2ea3f2}.et_pb_bg_layout_light_phone .et_pb_forgot_password a{color:#666}.et_pb_bg_layout_light_phone h1,.et_pb_bg_layout_light_phone h2,.et_pb_bg_layout_light_phone h3,.et_pb_bg_layout_light_phone h4,.et_pb_bg_layout_light_phone h5,.et_pb_bg_layout_light_phone h6{color:#333!important}.et_pb_module .et_pb_bg_layout_light_phone.et_pb_button{color:#2ea3f2!important}.et_pb_bg_layout_light_phone{color:#666!important}.et_pb_bg_layout_dark_phone,.et_pb_bg_layout_dark_phone h1,.et_pb_bg_layout_dark_phone h2,.et_pb_bg_layout_dark_phone h3,.et_pb_bg_layout_dark_phone h4,.et_pb_bg_layout_dark_phone h5,.et_pb_bg_layout_dark_phone h6{color:#fff!important}.et_pb_bg_layout_dark_phone.et_pb_button,.et_pb_bg_layout_dark_phone.et_pb_module.et_pb_button,.et_pb_bg_layout_dark_phone .et_pb_more_button{color:inherit}.et_pb_module .et_pb_bg_layout_dark_phone.et_pb_button{color:#fff!important}.et_pb_bg_layout_dark_phone .et_pb_forgot_password a{color:#fff}.et_pb_module.et_pb_text_align_left-phone{text-align:left}.et_pb_module.et_pb_text_align_center-phone{text-align:center}.et_pb_module.et_pb_text_align_right-phone{text-align:right}.et_pb_module.et_pb_text_align_justified-phone{text-align:justify}}@media (max-width:479px){a.et_pb_more_button{display:block}}@media (min-width:768px) and (max-width:980px){[data-et-multi-view-load-tablet-hidden=true]:not(.et_multi_view_swapped){display:none!important}}@media (max-width:767px){[data-et-multi-view-load-phone-hidden=true]:not(.et_multi_view_swapped){display:none!important}}.et_pb_menu.et_pb_menu--style-inline_centered_logo .et_pb_menu__menu nav ul{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}@-webkit-keyframes multi-view-image-fade{0%{-webkit-transform:scale(1);transform:scale(1);opacity:1}50%{-webkit-transform:scale(1.01);transform:scale(1.01);opacity:1}to{-webkit-transform:scale(1);transform:scale(1);opacity:1}}
</style>
<style id='divi-dynamic-critical-inline-css' type='text/css'>
@font-face{font-family:ETmodules;font-display:block;src:url(//fcmc.org/wp-content/themes/Divi/core/admin/fonts/modules/all/modules.eot);src:url(//fcmc.org/wp-content/themes/Divi/core/admin/fonts/modules/all/modules.eot?#iefix) format("embedded-opentype"),url(//fcmc.org/wp-content/themes/Divi/core/admin/fonts/modules/all/modules.woff) format("woff"),url(//fcmc.org/wp-content/themes/Divi/core/admin/fonts/modules/all/modules.ttf) format("truetype"),url(//fcmc.org/wp-content/themes/Divi/core/admin/fonts/modules/all/modules.svg#ETmodules) format("svg");font-weight:400;font-style:normal}
@media (min-width:981px){.et_pb_gutters3 .et_pb_column,.et_pb_gutters3.et_pb_row .et_pb_column{margin-right:5.5%}.et_pb_gutters3 .et_pb_column_4_4,.et_pb_gutters3.et_pb_row .et_pb_column_4_4{width:100%}.et_pb_gutters3 .et_pb_column_4_4 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_module{margin-bottom:2.75%}.et_pb_gutters3 .et_pb_column_3_4,.et_pb_gutters3.et_pb_row .et_pb_column_3_4{width:73.625%}.et_pb_gutters3 .et_pb_column_3_4 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_module{margin-bottom:3.735%}.et_pb_gutters3 .et_pb_column_2_3,.et_pb_gutters3.et_pb_row .et_pb_column_2_3{width:64.833%}.et_pb_gutters3 .et_pb_column_2_3 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_module{margin-bottom:4.242%}.et_pb_gutters3 .et_pb_column_3_5,.et_pb_gutters3.et_pb_row .et_pb_column_3_5{width:57.8%}.et_pb_gutters3 .et_pb_column_3_5 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_module{margin-bottom:4.758%}.et_pb_gutters3 .et_pb_column_1_2,.et_pb_gutters3.et_pb_row .et_pb_column_1_2{width:47.25%}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_module{margin-bottom:5.82%}.et_pb_gutters3 .et_pb_column_2_5,.et_pb_gutters3.et_pb_row .et_pb_column_2_5{width:36.7%}.et_pb_gutters3 .et_pb_column_2_5 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_2_5 .et_pb_module{margin-bottom:7.493%}.et_pb_gutters3 .et_pb_column_1_3,.et_pb_gutters3.et_pb_row .et_pb_column_1_3{width:29.6667%}.et_pb_gutters3 .et_pb_column_1_3 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_1_3 .et_pb_module{margin-bottom:9.27%}.et_pb_gutters3 .et_pb_column_1_4,.et_pb_gutters3.et_pb_row .et_pb_column_1_4{width:20.875%}.et_pb_gutters3 .et_pb_column_1_4 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_1_4 .et_pb_module{margin-bottom:13.174%}.et_pb_gutters3 .et_pb_column_1_5,.et_pb_gutters3.et_pb_row .et_pb_column_1_5{width:15.6%}.et_pb_gutters3 .et_pb_column_1_5 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_1_5 .et_pb_module{margin-bottom:17.628%}.et_pb_gutters3 .et_pb_column_1_6,.et_pb_gutters3.et_pb_row .et_pb_column_1_6{width:12.0833%}.et_pb_gutters3 .et_pb_column_1_6 .et_pb_module,.et_pb_gutters3.et_pb_row .et_pb_column_1_6 .et_pb_module{margin-bottom:22.759%}.et_pb_gutters3 .et_full_width_page.woocommerce-page ul.products li.product{width:20.875%;margin-right:5.5%;margin-bottom:5.5%}.et_pb_gutters3.et_left_sidebar.woocommerce-page #main-content ul.products li.product,.et_pb_gutters3.et_right_sidebar.woocommerce-page #main-content ul.products li.product{width:28.353%;margin-right:7.47%}.et_pb_gutters3.et_left_sidebar.woocommerce-page #main-content ul.products.columns-1 li.product,.et_pb_gutters3.et_right_sidebar.woocommerce-page #main-content ul.products.columns-1 li.product{width:100%;margin-right:0}.et_pb_gutters3.et_left_sidebar.woocommerce-page #main-content ul.products.columns-2 li.product,.et_pb_gutters3.et_right_sidebar.woocommerce-page #main-content ul.products.columns-2 li.product{width:48%;margin-right:4%}.et_pb_gutters3.et_left_sidebar.woocommerce-page #main-content ul.products.columns-2 li:nth-child(2n+2),.et_pb_gutters3.et_right_sidebar.woocommerce-page #main-content ul.products.columns-2 li:nth-child(2n+2){margin-right:0}.et_pb_gutters3.et_left_sidebar.woocommerce-page #main-content ul.products.columns-2 li:nth-child(3n+1),.et_pb_gutters3.et_right_sidebar.woocommerce-page #main-content ul.products.columns-2 li:nth-child(3n+1){clear:none}}
@media (min-width:981px){.et_pb_gutters3 .et_pb_column .et_pb_blog_grid .column.size-1of1 .et_pb_post:last-child,.et_pb_gutters3 .et_pb_column .et_pb_blog_grid .column.size-1of2 .et_pb_post:last-child,.et_pb_gutters3 .et_pb_column .et_pb_blog_grid .column.size-1of3 .et_pb_post:last-child,.et_pb_gutters3.et_pb_row .et_pb_column .et_pb_blog_grid .column.size-1of1 .et_pb_post:last-child,.et_pb_gutters3.et_pb_row .et_pb_column .et_pb_blog_grid .column.size-1of2 .et_pb_post:last-child,.et_pb_gutters3.et_pb_row .et_pb_column .et_pb_blog_grid .column.size-1of3 .et_pb_post:last-child{margin-bottom:30px}.et_pb_gutters3 .et_pb_column_4_4 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_4_4 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_4_4 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_widget{width:20.875%;margin-right:5.5%;margin-bottom:5.5%}.et_pb_gutters3 .et_pb_column_4_4 .et_pb_blog_grid .column.size-1of3,.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_blog_grid .column.size-1of3{width:29.667%;margin-right:5.5%}.et_pb_gutters3 .et_pb_column_4_4 .et_pb_blog_grid .column.size-1of3 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_blog_grid .column.size-1of3 .et_pb_post{margin-bottom:18.539%}.et_pb_gutters3 .et_pb_column_3_4 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_3_4 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_3_4 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_widget{width:28.353%;margin-right:7.47%;margin-bottom:7.47%}.et_pb_gutters3 .et_pb_column_3_4 .et_pb_blog_grid .column.size-1of2,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_blog_grid .column.size-1of2{width:46.265%;margin-right:7.47%}.et_pb_gutters3 .et_pb_column_3_4 .et_pb_blog_grid .column.size-1of2 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_blog_grid .column.size-1of2 .et_pb_post{margin-bottom:14.941%}.et_pb_gutters3 .et_pb_column_2_3 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_2_3 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_2_3 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_widget{width:45.758%;margin-right:8.483%;margin-bottom:8.483%}.et_pb_gutters3 .et_pb_column_2_3 .et_pb_blog_grid .column.size-1of2,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_blog_grid .column.size-1of2{width:45.758%;margin-right:8.483%}.et_pb_gutters3 .et_pb_column_2_3 .et_pb_blog_grid .column.size-1of2 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_blog_grid .column.size-1of2 .et_pb_post{margin-bottom:16.967%}.et_pb_gutters3 .et_pb_column_3_5 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_3_5 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_3_5 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_widget{width:45.242%;margin-right:9.516%;margin-bottom:9.516%}.et_pb_gutters3 .et_pb_column_3_5 .et_pb_blog_grid .column.size-1of1,.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_blog_grid .column.size-1of1{width:100%;margin-right:0}.et_pb_gutters3 .et_pb_column_3_5 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_blog_grid .column.size-1of1 .et_pb_post{margin-bottom:9.516%}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_1_2 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_1_2 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_widget{width:44.18%;margin-right:11.64%;margin-bottom:11.64%}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_blog_grid .column.size-1of1,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_blog_grid .column.size-1of1{width:100%;margin-right:0}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_blog_grid .column.size-1of1 .et_pb_post{margin-bottom:11.64%}.et_pb_gutters3 .et_pb_column_2_5 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3 .et_pb_column_2_5 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_2_5 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_2_5 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_2_5 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_2_5 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_2_5 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_2_5 .et_pb_widget{width:100%;margin-bottom:14.986%}.et_pb_gutters3 .et_pb_column_1_3 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3 .et_pb_column_1_3 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_1_3 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_1_3 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_1_3 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_1_3 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_1_3 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_1_3 .et_pb_widget{width:100%;margin-bottom:18.539%}.et_pb_gutters3 .et_pb_column_1_4 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3 .et_pb_column_1_4 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_1_4 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_1_4 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_1_4 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_1_4 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_1_4 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_1_4 .et_pb_widget{width:100%;margin-bottom:26.347%}.et_pb_gutters3 .et_pb_column_1_5 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3 .et_pb_column_1_5 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_1_5 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_1_5 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_1_5 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_1_5 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_1_5 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_1_5 .et_pb_widget{width:100%;margin-bottom:35.256%}.et_pb_gutters3 .et_pb_column_1_6 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3 .et_pb_column_1_6 .et_pb_grid_item,.et_pb_gutters3 .et_pb_column_1_6 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3 .et_pb_column_1_6 .et_pb_widget,.et_pb_gutters3.et_pb_row .et_pb_column_1_6 .et_pb_blog_grid .column.size-1of1 .et_pb_post,.et_pb_gutters3.et_pb_row .et_pb_column_1_6 .et_pb_grid_item,.et_pb_gutters3.et_pb_row .et_pb_column_1_6 .et_pb_shop_grid .woocommerce ul.products li.product,.et_pb_gutters3.et_pb_row .et_pb_column_1_6 .et_pb_widget{width:100%;margin-bottom:45.517%}.et_pb_gutters3 .et_pb_column_4_4 .et_pb_grid_item.et_pb_portfolio_item:nth-child(4n),.et_pb_gutters3 .et_pb_column_4_4 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(4n),.et_pb_gutters3 .et_pb_column_4_4 .et_pb_widget:nth-child(4n),.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_grid_item.et_pb_portfolio_item:nth-child(4n),.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(4n),.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_widget:nth-child(4n){margin-right:0}.et_pb_gutters3 .et_pb_column_4_4 .et_pb_grid_item.et_pb_portfolio_item:nth-child(4n+1),.et_pb_gutters3 .et_pb_column_4_4 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(4n+1),.et_pb_gutters3 .et_pb_column_4_4 .et_pb_widget:nth-child(4n+1),.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_grid_item.et_pb_portfolio_item:nth-child(4n+1),.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(4n+1),.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_widget:nth-child(4n+1){clear:both}.et_pb_gutters3 .et_pb_column_4_4 .et_pb_blog_grid .column.size-1of3:nth-child(3n),.et_pb_gutters3 .et_pb_column_4_4 .et_pb_grid_item.last_in_row,.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_blog_grid .column.size-1of3:nth-child(3n),.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_grid_item.last_in_row{margin-right:0}.et_pb_gutters3 .et_pb_column_4_4 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_4_4 .et_pb_grid_item.on_last_row{margin-bottom:0}.et_pb_gutters3 .et_pb_column_3_4 .et_pb_grid_item.et_pb_portfolio_item:nth-child(3n),.et_pb_gutters3 .et_pb_column_3_4 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(3n),.et_pb_gutters3 .et_pb_column_3_4 .et_pb_widget:nth-child(3n),.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_grid_item.et_pb_portfolio_item:nth-child(3n),.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(3n),.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_widget:nth-child(3n){margin-right:0}.et_pb_gutters3 .et_pb_column_3_4 .et_pb_grid_item.et_pb_portfolio_item:nth-child(3n+1),.et_pb_gutters3 .et_pb_column_3_4 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(3n+1),.et_pb_gutters3 .et_pb_column_3_4 .et_pb_widget:nth-child(3n+1),.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_grid_item.et_pb_portfolio_item:nth-child(3n+1),.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(3n+1),.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_widget:nth-child(3n+1){clear:both}.et_pb_gutters3 .et_pb_column_3_4 .et_pb_grid_item.last_in_row,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_grid_item.last_in_row{margin-right:0}.et_pb_gutters3 .et_pb_column_3_4 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_grid_item.on_last_row{margin-bottom:0}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_grid_item.et_pb_portfolio_item:nth-child(2n),.et_pb_gutters3 .et_pb_column_1_2 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(2n),.et_pb_gutters3 .et_pb_column_1_2 .et_pb_widget:nth-child(2n),.et_pb_gutters3 .et_pb_column_2_3 .et_pb_grid_item.et_pb_portfolio_item:nth-child(2n),.et_pb_gutters3 .et_pb_column_2_3 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(2n),.et_pb_gutters3 .et_pb_column_2_3 .et_pb_widget:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_grid_item.et_pb_portfolio_item:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_widget:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_grid_item.et_pb_portfolio_item:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_widget:nth-child(2n){margin-right:0}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_grid_item.et_pb_portfolio_item:nth-child(odd),.et_pb_gutters3 .et_pb_column_1_2 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(odd),.et_pb_gutters3 .et_pb_column_1_2 .et_pb_widget:nth-child(odd),.et_pb_gutters3 .et_pb_column_2_3 .et_pb_grid_item.et_pb_portfolio_item:nth-child(odd),.et_pb_gutters3 .et_pb_column_2_3 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(odd),.et_pb_gutters3 .et_pb_column_2_3 .et_pb_widget:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_grid_item.et_pb_portfolio_item:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_widget:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_grid_item.et_pb_portfolio_item:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_widget:nth-child(odd){clear:both}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_grid_item.last_in_row,.et_pb_gutters3 .et_pb_column_2_3 .et_pb_grid_item.last_in_row,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_grid_item.last_in_row,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_grid_item.last_in_row{margin-right:0}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_grid_item.on_last_row,.et_pb_gutters3 .et_pb_column_2_3 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_grid_item.on_last_row{margin-bottom:0}.et_pb_gutters3 .et_pb_column_3_5 .et_pb_grid_item.et_pb_portfolio_item:nth-child(2n),.et_pb_gutters3 .et_pb_column_3_5 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(2n),.et_pb_gutters3 .et_pb_column_3_5 .et_pb_widget:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_grid_item.et_pb_portfolio_item:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_widget:nth-child(2n){margin-right:0}.et_pb_gutters3 .et_pb_column_3_5 .et_pb_grid_item.et_pb_portfolio_item:nth-child(odd),.et_pb_gutters3 .et_pb_column_3_5 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(odd),.et_pb_gutters3 .et_pb_column_3_5 .et_pb_widget:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_grid_item.et_pb_portfolio_item:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_shop_grid .woocommerce ul.products li.product:nth-child(odd),.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_widget:nth-child(odd){clear:both}.et_pb_gutters3 .et_pb_column_3_5 .et_pb_grid_item.last_in_row,.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_grid_item.last_in_row{margin-right:0}.et_pb_gutters3 .et_pb_column_1_3 .et_pb_grid_item.on_last_row,.et_pb_gutters3 .et_pb_column_1_4 .et_pb_grid_item.on_last_row,.et_pb_gutters3 .et_pb_column_1_5 .et_pb_grid_item.on_last_row,.et_pb_gutters3 .et_pb_column_1_6 .et_pb_grid_item.on_last_row,.et_pb_gutters3 .et_pb_column_3_5 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_1_3 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_1_4 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_1_5 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_1_6 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_3_5 .et_pb_grid_item.on_last_row{margin-bottom:0}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_blog_grid .column.size-1of2:nth-child(2n),.et_pb_gutters3 .et_pb_column_1_2 .et_pb_blog_grid .column.size-1of3:nth-child(3n),.et_pb_gutters3 .et_pb_column_1_2 .et_pb_grid_item.last_in_row,.et_pb_gutters3 .et_pb_column_2_3 .et_pb_blog_grid .column.size-1of2:nth-child(2n),.et_pb_gutters3 .et_pb_column_2_3 .et_pb_blog_grid .column.size-1of3:nth-child(3n),.et_pb_gutters3 .et_pb_column_2_3 .et_pb_grid_item.last_in_row,.et_pb_gutters3 .et_pb_column_3_4 .et_pb_blog_grid .column.size-1of2:nth-child(2n),.et_pb_gutters3 .et_pb_column_3_4 .et_pb_blog_grid .column.size-1of3:nth-child(3n),.et_pb_gutters3 .et_pb_column_3_4 .et_pb_grid_item.last_in_row,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_blog_grid .column.size-1of2:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_blog_grid .column.size-1of3:nth-child(3n),.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_grid_item.last_in_row,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_blog_grid .column.size-1of2:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_blog_grid .column.size-1of3:nth-child(3n),.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_grid_item.last_in_row,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_blog_grid .column.size-1of2:nth-child(2n),.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_blog_grid .column.size-1of3:nth-child(3n),.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_grid_item.last_in_row{margin-right:0}.et_pb_gutters3 .et_pb_column_1_2 .et_pb_grid_item.on_last_row,.et_pb_gutters3 .et_pb_column_2_3 .et_pb_grid_item.on_last_row,.et_pb_gutters3 .et_pb_column_3_4 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_1_2 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_2_3 .et_pb_grid_item.on_last_row,.et_pb_gutters3.et_pb_row .et_pb_column_3_4 .et_pb_grid_item.on_last_row{margin-bottom:0}}
.et_pb_widget{float:left;max-width:100%;word-wrap:break-word}.et_pb_widget a{text-decoration:none;color:#666}.et_pb_widget li a:hover{color:#82c0c7}.et_pb_widget ol li,.et_pb_widget ul li{margin-bottom:.5em}.et_pb_widget ol li ol li,.et_pb_widget ul li ul li{margin-left:15px}.et_pb_widget select{width:100%;height:28px;padding:0 5px}.et_pb_widget_area .et_pb_widget a{color:inherit}.et_pb_bg_layout_light .et_pb_widget li a{color:#666}.et_pb_bg_layout_dark .et_pb_widget li a{color:inherit}
.widget_search .screen-reader-text,.et_pb_widget .wp-block-search__label{display:none}.widget_search input#s,.widget_search input#searchsubmit,.et_pb_widget .wp-block-search__input,.et_pb_widget .wp-block-search__button{padding:.7em;height:40px !important;margin:0;font-size:14px;line-height:normal !important;border:1px solid #ddd;color:#666}.widget_search #s,.et_pb_widget .wp-block-search__input{width:100%;border-radius:3px}.widget_search #searchform,.et_pb_widget .wp-block-search{position:relative}.widget_search #searchsubmit,.et_pb_widget .wp-block-search__button{background-color:#ddd;-webkit-border-top-right-radius:3px;-webkit-border-bottom-right-radius:3px;-moz-border-radius-topright:3px;-moz-border-radius-bottomright:3px;border-top-right-radius:3px;border-bottom-right-radius:3px;position:absolute;right:0;top:0}#searchsubmit,.et_pb_widget .wp-block-search__button{cursor:pointer}
.et_pb_section{position:relative;background-color:#fff;background-position:50%;background-size:100%;background-size:cover}.et_pb_section--absolute,.et_pb_section--fixed{width:100%}.et_pb_section.et_section_transparent{background-color:transparent}.et_pb_fullwidth_section{padding:0}.et_pb_fullwidth_section>.et_pb_module:not(.et_pb_post_content):not(.et_pb_fullwidth_post_content) .et_pb_row{padding:0!important}.et_pb_inner_shadow{-webkit-box-shadow:inset 0 0 7px rgba(0,0,0,.07);box-shadow:inset 0 0 7px rgba(0,0,0,.07)}.et_pb_bottom_inside_divider,.et_pb_top_inside_divider{display:block;background-repeat-y:no-repeat;height:100%;position:absolute;pointer-events:none;width:100%;left:0;right:0}.et_pb_bottom_inside_divider.et-no-transition,.et_pb_top_inside_divider.et-no-transition{-webkit-transition:none!important;transition:none!important}.et-fb .section_has_divider.et_fb_element_controls_visible--child>.et_pb_bottom_inside_divider,.et-fb .section_has_divider.et_fb_element_controls_visible--child>.et_pb_top_inside_divider{z-index:1}.et_pb_section_video:not(.et_pb_section--with-menu){overflow:hidden;position:relative}.et_pb_column>.et_pb_section_video_bg{z-index:-1}.et_pb_section_video_bg{visibility:visible;position:absolute;top:0;left:0;width:100%;height:100%;overflow:hidden;display:block;pointer-events:none;-webkit-transition:display .3s;transition:display .3s}.et_pb_section_video_bg.et_pb_section_video_bg_hover,.et_pb_section_video_bg.et_pb_section_video_bg_phone,.et_pb_section_video_bg.et_pb_section_video_bg_tablet,.et_pb_section_video_bg.et_pb_section_video_bg_tablet_only{display:none}.et_pb_section_video_bg .mejs-controls,.et_pb_section_video_bg .mejs-overlay-play{display:none!important}.et_pb_section_video_bg embed,.et_pb_section_video_bg iframe,.et_pb_section_video_bg object,.et_pb_section_video_bg video{max-width:none}.et_pb_section_video_bg .mejs-video{left:50%;position:absolute;max-width:none}.et_pb_section_video_bg .mejs-overlay-loading{display:none!important}.et_pb_social_network_link .et_pb_section_video{overflow:visible}.et_pb_section_video_on_hover:hover>.et_pb_section_video_bg{display:none}.et_pb_section_video_on_hover:hover>.et_pb_section_video_bg_hover,.et_pb_section_video_on_hover:hover>.et_pb_section_video_bg_hover_inherit{display:block}@media (min-width:981px){.et_pb_section{padding:4% 0}body.et_pb_pagebuilder_layout.et_pb_show_title .post-password-required .et_pb_section,body:not(.et_pb_pagebuilder_layout) .post-password-required .et_pb_section{padding-top:0}.et_pb_fullwidth_section{padding:0}.et_pb_section_video_bg.et_pb_section_video_bg_desktop_only{display:block}}@media (max-width:980px){.et_pb_section{padding:50px 0}body.et_pb_pagebuilder_layout.et_pb_show_title .post-password-required .et_pb_section,body:not(.et_pb_pagebuilder_layout) .post-password-required .et_pb_section{padding-top:0}.et_pb_fullwidth_section{padding:0}.et_pb_section_video_bg.et_pb_section_video_bg_tablet{display:block}.et_pb_section_video_bg.et_pb_section_video_bg_desktop_only{display:none}}@media (min-width:768px){.et_pb_section_video_bg.et_pb_section_video_bg_desktop_tablet{display:block}}@media (min-width:768px) and (max-width:980px){.et_pb_section_video_bg.et_pb_section_video_bg_tablet_only{display:block}}@media (max-width:767px){.et_pb_section_video_bg.et_pb_section_video_bg_phone{display:block}.et_pb_section_video_bg.et_pb_section_video_bg_desktop_tablet{display:none}}
.et_pb_row{width:80%;max-width:1080px;margin:auto;position:relative}body.safari .section_has_divider,body.uiwebview .section_has_divider{-webkit-perspective:2000px;perspective:2000px}.section_has_divider .et_pb_row{z-index:5}.et_pb_row_inner{width:100%;position:relative}.et_pb_row.et_pb_row_empty,.et_pb_row_inner:nth-of-type(n+2).et_pb_row_empty{display:none}.et_pb_row:after,.et_pb_row_inner:after{content:"";display:block;clear:both;visibility:hidden;line-height:0;height:0;width:0}.et_pb_row_4col .et-last-child,.et_pb_row_4col .et-last-child-2,.et_pb_row_6col .et-last-child,.et_pb_row_6col .et-last-child-2,.et_pb_row_6col .et-last-child-3{margin-bottom:0}.et_pb_column{float:left;background-size:cover;background-position:50%;position:relative;z-index:2;min-height:1px}.et_pb_column--with-menu{z-index:3}.et_pb_column.et_pb_column_empty{min-height:1px}.et_pb_row .et_pb_column.et-last-child,.et_pb_row .et_pb_column:last-child,.et_pb_row_inner .et_pb_column.et-last-child,.et_pb_row_inner .et_pb_column:last-child{margin-right:0!important}.et_pb_column.et_pb_section_parallax{position:relative}.et_pb_column,.et_pb_row,.et_pb_row_inner{background-size:cover;background-position:50%;background-repeat:no-repeat}@media (min-width:981px){.et_pb_row{padding:2% 0}body.et_pb_pagebuilder_layout.et_pb_show_title .post-password-required .et_pb_row,body:not(.et_pb_pagebuilder_layout) .post-password-required .et_pb_row{padding:0;width:100%}.et_pb_column_3_4 .et_pb_row_inner{padding:3.735% 0}.et_pb_column_2_3 .et_pb_row_inner{padding:4.2415% 0}.et_pb_column_1_2 .et_pb_row_inner,.et_pb_column_3_5 .et_pb_row_inner{padding:5.82% 0}.et_section_specialty>.et_pb_row{padding:0}.et_pb_row_inner{width:100%}.et_pb_column_single{padding:2.855% 0}.et_pb_column_single .et_pb_module.et-first-child,.et_pb_column_single .et_pb_module:first-child{margin-top:0}.et_pb_column_single .et_pb_module.et-last-child,.et_pb_column_single .et_pb_module:last-child{margin-bottom:0}.et_pb_row .et_pb_column.et-last-child,.et_pb_row .et_pb_column:last-child,.et_pb_row_inner .et_pb_column.et-last-child,.et_pb_row_inner .et_pb_column:last-child{margin-right:0!important}.et_pb_row.et_pb_equal_columns,.et_pb_row_inner.et_pb_equal_columns,.et_pb_section.et_pb_equal_columns>.et_pb_row{display:-webkit-box;display:-ms-flexbox;display:flex}.rtl .et_pb_row.et_pb_equal_columns,.rtl .et_pb_row_inner.et_pb_equal_columns,.rtl .et_pb_section.et_pb_equal_columns>.et_pb_row{-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}.et_pb_row.et_pb_equal_columns>.et_pb_column,.et_pb_section.et_pb_equal_columns>.et_pb_row>.et_pb_column{-webkit-box-ordinal-group:2;-ms-flex-order:1;order:1}}@media (max-width:980px){.et_pb_row{max-width:1080px}body.et_pb_pagebuilder_layout.et_pb_show_title .post-password-required .et_pb_row,body:not(.et_pb_pagebuilder_layout) .post-password-required .et_pb_row{padding:0;width:100%}.et_pb_column .et_pb_row_inner,.et_pb_row{padding:30px 0}.et_section_specialty>.et_pb_row{padding:0}.et_pb_column{width:100%;margin-bottom:30px}.et_pb_bottom_divider .et_pb_row:nth-last-child(2) .et_pb_column:last-child,.et_pb_row .et_pb_column.et-last-child,.et_pb_row .et_pb_column:last-child{margin-bottom:0}.et_section_specialty .et_pb_row>.et_pb_column{padding-bottom:0}.et_pb_column.et_pb_column_empty{display:none}.et_pb_row_1-2_1-4_1-4,.et_pb_row_1-2_1-6_1-6_1-6,.et_pb_row_1-4_1-4,.et_pb_row_1-4_1-4_1-2,.et_pb_row_1-5_1-5_3-5,.et_pb_row_1-6_1-6_1-6,.et_pb_row_1-6_1-6_1-6_1-2,.et_pb_row_1-6_1-6_1-6_1-6,.et_pb_row_3-5_1-5_1-5,.et_pb_row_4col,.et_pb_row_5col,.et_pb_row_6col{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap}.et_pb_row_1-4_1-4>.et_pb_column.et_pb_column_1_4,.et_pb_row_1-4_1-4_1-2>.et_pb_column.et_pb_column_1_4,.et_pb_row_4col>.et_pb_column.et_pb_column_1_4{width:47.25%;margin-right:5.5%}.et_pb_row_1-4_1-4>.et_pb_column.et_pb_column_1_4:nth-child(2n),.et_pb_row_1-4_1-4_1-2>.et_pb_column.et_pb_column_1_4:nth-child(2n),.et_pb_row_4col>.et_pb_column.et_pb_column_1_4:nth-child(2n){margin-right:0}.et_pb_row_1-2_1-4_1-4>.et_pb_column.et_pb_column_1_4{width:47.25%;margin-right:5.5%}.et_pb_row_1-2_1-4_1-4>.et_pb_column.et_pb_column_1_2,.et_pb_row_1-2_1-4_1-4>.et_pb_column.et_pb_column_1_4:nth-child(odd){margin-right:0}.et_pb_row_1-2_1-4_1-4 .et_pb_column:nth-last-child(-n+2),.et_pb_row_1-4_1-4 .et_pb_column:nth-last-child(-n+2),.et_pb_row_4col .et_pb_column:nth-last-child(-n+2){margin-bottom:0}.et_pb_row_1-5_1-5_3-5>.et_pb_column.et_pb_column_1_5,.et_pb_row_5col>.et_pb_column.et_pb_column_1_5{width:47.25%;margin-right:5.5%}.et_pb_row_1-5_1-5_3-5>.et_pb_column.et_pb_column_1_5:nth-child(2n),.et_pb_row_5col>.et_pb_column.et_pb_column_1_5:nth-child(2n){margin-right:0}.et_pb_row_3-5_1-5_1-5>.et_pb_column.et_pb_column_1_5{width:47.25%;margin-right:5.5%}.et_pb_row_3-5_1-5_1-5>.et_pb_column.et_pb_column_1_5:nth-child(odd),.et_pb_row_3-5_1-5_1-5>.et_pb_column.et_pb_column_3_5{margin-right:0}.et_pb_row_3-5_1-5_1-5 .et_pb_column:nth-last-child(-n+2),.et_pb_row_5col .et_pb_column:last-child{margin-bottom:0}.et_pb_row_1-6_1-6_1-6_1-2>.et_pb_column.et_pb_column_1_6,.et_pb_row_6col>.et_pb_column.et_pb_column_1_6{width:29.666%;margin-right:5.5%}.et_pb_row_1-6_1-6_1-6_1-2>.et_pb_column.et_pb_column_1_6:nth-child(3n),.et_pb_row_6col>.et_pb_column.et_pb_column_1_6:nth-child(3n){margin-right:0}.et_pb_row_1-2_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6{width:29.666%;margin-right:5.5%}.et_pb_row_1-2_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_2,.et_pb_row_1-2_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6:last-child{margin-right:0}.et_pb_row_1-2_1-2 .et_pb_column.et_pb_column_1_2,.et_pb_row_1-2_1-6_1-6_1-6 .et_pb_column:nth-last-child(-n+3),.et_pb_row_6col .et_pb_column:nth-last-child(-n+3){margin-bottom:0}.et_pb_row_1-2_1-2 .et_pb_column.et_pb_column_1_2 .et_pb_column.et_pb_column_1_6{width:29.666%;margin-right:5.5%;margin-bottom:0}.et_pb_row_1-2_1-2 .et_pb_column.et_pb_column_1_2 .et_pb_column.et_pb_column_1_6:last-child{margin-right:0}.et_pb_row_1-6_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6{width:47.25%;margin-right:5.5%}.et_pb_row_1-6_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6:nth-child(2n){margin-right:0}.et_pb_row_1-6_1-6_1-6_1-6:nth-last-child(-n+3){margin-bottom:0}}@media (max-width:479px){.et_pb_row .et_pb_column.et_pb_column_1_4,.et_pb_row .et_pb_column.et_pb_column_1_5,.et_pb_row .et_pb_column.et_pb_column_1_6{width:100%;margin:0 0 30px}.et_pb_row .et_pb_column.et_pb_column_1_4.et-last-child,.et_pb_row .et_pb_column.et_pb_column_1_4:last-child,.et_pb_row .et_pb_column.et_pb_column_1_5.et-last-child,.et_pb_row .et_pb_column.et_pb_column_1_5:last-child,.et_pb_row .et_pb_column.et_pb_column_1_6.et-last-child,.et_pb_row .et_pb_column.et_pb_column_1_6:last-child{margin-bottom:0}.et_pb_row_1-2_1-2 .et_pb_column.et_pb_column_1_2 .et_pb_column.et_pb_column_1_6{width:100%;margin:0 0 30px}.et_pb_row_1-2_1-2 .et_pb_column.et_pb_column_1_2 .et_pb_column.et_pb_column_1_6.et-last-child,.et_pb_row_1-2_1-2 .et_pb_column.et_pb_column_1_2 .et_pb_column.et_pb_column_1_6:last-child{margin-bottom:0}.et_pb_column{width:100%!important}}
.et-menu li{display:inline-block;font-size:14px;padding-right:22px}.et-menu>li:last-child{padding-right:0}.et-menu a{color:rgba(0,0,0,.6);text-decoration:none;display:block;position:relative}.et-menu a,.et-menu a:hover{-webkit-transition:all .4s ease-in-out;transition:all .4s ease-in-out}.et-menu a:hover{opacity:.7}.et-menu li>a{padding-bottom:29px;word-wrap:break-word}a.et_pb_menu__icon,button.et_pb_menu__icon{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding:0;margin:0 11px;font-size:17px;line-height:normal;background:none;border:0;cursor:pointer;-webkit-box-orient:horizontal;-webkit-box-direction:reverse;-ms-flex-direction:row-reverse;flex-direction:row-reverse}a.et_pb_menu__icon:after,button.et_pb_menu__icon:after{font-family:ETmodules}a.et_pb_menu__icon__with_count:after,button.et_pb_menu__icon__with_count:after{margin-right:10px}.et_pb_menu__wrap .mobile_menu_bar{-webkit-transform:translateY(3%);transform:translateY(3%)}.et_pb_menu__wrap .mobile_menu_bar:before{top:0}.et_pb_menu__logo{overflow:hidden}.et_pb_menu__logo img{display:block}.et_pb_menu__logo img[src$=".svg"]{width:100%}.et_pb_menu__search-button:after{content:"U"}.et_pb_menu__cart-button:after{content:"\E07A"}@media (max-width:980px){.et-menu{display:none}.et_mobile_nav_menu{display:block;margin-top:-1px}}
.et_pb_with_border.et_pb_menu .et_pb_menu__logo img{border:0 solid #333}.et_pb_menu.et_hover_enabled:hover{z-index:auto}.et_pb_menu .et-menu-nav,.et_pb_menu .et-menu-nav>ul{float:none}.et_pb_menu .et-menu-nav>ul{padding:0!important;line-height:1.7em}.et_pb_menu .et-menu-nav>ul ul{padding:20px 0;text-align:left}.et_pb_bg_layout_dark.et_pb_menu ul li a{color:#fff}.et_pb_bg_layout_dark.et_pb_menu ul li a:hover{color:hsla(0,0%,100%,.8)}.et-menu li li.menu-item-has-children>a:first-child:after{top:12px}.et_pb_menu .et-menu-nav>ul.upwards li ul{bottom:100%;top:auto;border-top:none;border-bottom:3px solid #2ea3f2;-webkit-box-shadow:2px -2px 5px rgba(0,0,0,.1);box-shadow:2px -2px 5px rgba(0,0,0,.1)}.et_pb_menu .et-menu-nav>ul.upwards li ul li ul{bottom:-23px}.et_pb_menu .et-menu-nav>ul.upwards li.mega-menu ul ul{bottom:0;top:auto;border:none}.et_pb_menu_inner_container{position:relative}.et_pb_menu .et_pb_menu__wrap{-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;-ms-flex-wrap:wrap;flex-wrap:wrap;opacity:1}.et_pb_menu .et_pb_menu__wrap--visible{-webkit-animation:fadeInBottom 1s cubic-bezier(.77,0,.175,1) 1;animation:fadeInBottom 1s cubic-bezier(.77,0,.175,1) 1}.et_pb_menu .et_pb_menu__wrap--hidden{opacity:0;-webkit-animation:fadeOutBottom 1s cubic-bezier(.77,0,.175,1) 1;animation:fadeOutBottom 1s cubic-bezier(.77,0,.175,1) 1}.et_pb_menu .et_pb_menu__menu{-webkit-box-flex:0;-ms-flex:0 1 auto;flex:0 1 auto;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.et_pb_menu .et_pb_menu__menu,.et_pb_menu .et_pb_menu__menu>nav,.et_pb_menu .et_pb_menu__menu>nav>ul{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch}.et_pb_menu .et_pb_menu__menu>nav>ul{-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-box-pack:start;-ms-flex-pack:start;justify-content:flex-start}.et_pb_menu .et_pb_menu__menu>nav>ul>li{position:relative;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch;margin:0}.et_pb_menu .et_pb_menu__menu>nav>ul>li.mega-menu{position:static}.et_pb_menu .et_pb_menu__menu>nav>ul>li>ul{top:calc(100% - 1px);left:0}.et_pb_menu .et_pb_menu__menu>nav>ul.upwards>li>ul{top:auto;bottom:calc(100% - 1px)}.et_pb_menu--with-logo .et_pb_menu__menu>nav>ul>li>a{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center;padding:31px 0;white-space:nowrap}.et_pb_menu--with-logo .et_pb_menu__menu>nav>ul>li>a:after{top:50%!important;-webkit-transform:translateY(-50%);transform:translateY(-50%)}.et_pb_menu--without-logo .et_pb_menu__menu>nav>ul{padding:0!important}.et_pb_menu--without-logo .et_pb_menu__menu>nav>ul>li{margin-top:8px}.et_pb_menu--without-logo .et_pb_menu__menu>nav>ul>li>a{padding-bottom:8px}.et_pb_menu--without-logo .et_pb_menu__menu>nav>ul.upwards>li{margin-top:0;margin-bottom:8px}.et_pb_menu--without-logo .et_pb_menu__menu>nav>ul.upwards>li>a{padding-top:8px;padding-bottom:0}.et_pb_menu--without-logo .et_pb_menu__menu>nav>ul.upwards>li>a:after{top:auto;bottom:0}.et_pb_menu .et_pb_menu__icon{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto}.et_pb_menu .et-menu{margin-left:-11px;margin-right:-11px}.et_pb_menu .et-menu>li{padding-left:11px;padding-right:11px}.et_pb_menu--style-left_aligned .et_pb_menu_inner_container,.et_pb_menu--style-left_aligned .et_pb_row{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:stretch;-ms-flex-align:stretch;align-items:stretch}.et_pb_menu--style-left_aligned .et_pb_menu__logo-wrap{-webkit-box-flex:0;-ms-flex:0 1 auto;flex:0 1 auto;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.et_pb_menu--style-left_aligned .et_pb_menu__logo{margin-right:30px}.rtl .et_pb_menu--style-left_aligned .et_pb_menu__logo{margin-right:0;margin-left:30px}.et_pb_menu--style-left_aligned.et_pb_text_align_center .et_pb_menu__menu>nav>ul,.et_pb_menu--style-left_aligned.et_pb_text_align_center .et_pb_menu__wrap{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.et_pb_menu--style-left_aligned.et_pb_text_align_right .et_pb_menu__menu>nav>ul,.et_pb_menu--style-left_aligned.et_pb_text_align_right .et_pb_menu__wrap{-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}.et_pb_menu--style-left_aligned.et_pb_text_align_justified .et_pb_menu__menu,.et_pb_menu--style-left_aligned.et_pb_text_align_justified .et_pb_menu__menu>nav,.et_pb_menu--style-left_aligned.et_pb_text_align_justified .et_pb_menu__wrap{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1}.et_pb_menu--style-left_aligned.et_pb_text_align_justified .et_pb_menu__menu>nav>ul{-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}.et_pb_menu--style-centered .et_pb_menu__logo-wrap{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.et_pb_menu--style-centered .et_pb_menu__logo-wrap,.et_pb_menu--style-centered .et_pb_menu__logo img{margin:0 auto}.et_pb_menu--style-centered .et_pb_menu__menu>nav>ul,.et_pb_menu--style-centered .et_pb_menu__wrap{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.et_pb_menu--style-inline_centered_logo .et_pb_menu_inner_container>.et_pb_menu__logo-wrap,.et_pb_menu--style-inline_centered_logo .et_pb_row>.et_pb_menu__logo-wrap{display:none;margin-bottom:30px}.et_pb_menu--style-inline_centered_logo .et_pb_menu__logo{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.et_pb_menu--style-inline_centered_logo .et_pb_menu__logo,.et_pb_menu--style-inline_centered_logo .et_pb_menu__logo img{margin:0 auto}.et_pb_menu--style-inline_centered_logo .et_pb_menu__wrap{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.et_pb_menu--style-inline_centered_logo .et_pb_menu__logo-slot{-webkit-box-align:center!important;-ms-flex-align:center!important;align-items:center!important}.et_pb_menu--style-inline_centered_logo .et_pb_menu__logo-slot .et_pb_menu__logo,.et_pb_menu--style-inline_centered_logo .et_pb_menu__logo-slot .et_pb_menu__logo-wrap{width:100%;height:100%}.et_pb_menu--style-inline_centered_logo .et_pb_menu__logo-slot img{max-height:100%}.et_pb_menu .et_pb_menu__logo-slot .et-fb-content-placeholder{min-width:96px}.et_pb_menu .et_pb_menu__search-container{position:absolute;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:stretch;-ms-flex-pack:stretch;justify-content:stretch;-ms-flex-line-pack:stretch;align-content:stretch;left:0;bottom:0;width:100%;height:100%;opacity:0;z-index:999}.et_pb_menu .et_pb_menu__search-container--visible{opacity:1;-webkit-animation:fadeInTop 1s cubic-bezier(.77,0,.175,1) 1;animation:fadeInTop 1s cubic-bezier(.77,0,.175,1) 1}.et_pb_menu .et_pb_menu__search-container--hidden{-webkit-animation:fadeOutTop 1s cubic-bezier(.77,0,.175,1) 1;animation:fadeOutTop 1s cubic-bezier(.77,0,.175,1) 1}.et_pb_menu .et_pb_menu__search-container--disabled{display:none}.et_pb_menu .et_pb_menu__search{-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-pack:stretch;-ms-flex-pack:stretch;justify-content:stretch;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.et_pb_menu .et_pb_menu__search-form{-webkit-box-flex:1;-ms-flex:1 1 auto;flex:1 1 auto}.et_pb_menu .et_pb_menu__search-input{border:0;width:100%;color:#333;background:transparent}.et_pb_menu .et_pb_menu__close-search-button{-webkit-box-flex:0;-ms-flex:0 0 auto;flex:0 0 auto}.et_pb_menu .et_pb_menu__close-search-button:after{content:"M";font-size:1.7em}@media (min-width:981px){.et_dropdown_animation_fade.et_pb_menu ul li:hover>ul{-webkit-transition:all .2s ease-in-out;transition:all .2s ease-in-out}.et_dropdown_animation_slide.et_pb_menu ul li:hover>ul{-webkit-animation:fadeLeft .4s ease-in-out;animation:fadeLeft .4s ease-in-out}.et_dropdown_animation_expand.et_pb_menu ul li:hover>ul{-webkit-transform-origin:0 0;-webkit-animation:Grow .4s ease-in-out;animation:Grow .4s ease-in-out;-webkit-backface-visibility:visible!important;backface-visibility:visible!important}.et_dropdown_animation_flip.et_pb_menu ul li ul li:hover>ul{-webkit-animation:flipInX .6s ease-in-out;animation:flipInX .6s ease-in-out;-webkit-backface-visibility:visible!important;backface-visibility:visible!important}.et_dropdown_animation_flip.et_pb_menu ul li:hover>ul{-webkit-animation:flipInY .6s ease-in-out;animation:flipInY .6s ease-in-out;-webkit-backface-visibility:visible!important;backface-visibility:visible!important}.et_pb_menu.et_pb_menu_fullwidth .et_pb_row{width:100%;max-width:100%;padding:0 30px!important}}@media (max-width:980px){.et_pb_menu--style-left_aligned .et_pb_menu_inner_container,.et_pb_menu--style-left_aligned .et_pb_row{-webkit-box-align:center;-ms-flex-align:center;align-items:center}.et_pb_menu--style-left_aligned .et_pb_menu__wrap{-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}.et_pb_menu--style-left_aligned.et_pb_text_align_center .et_pb_menu__wrap{-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center}.et_pb_menu--style-left_aligned.et_pb_text_align_right .et_pb_menu__wrap{-webkit-box-pack:end;-ms-flex-pack:end;justify-content:flex-end}.et_pb_menu--style-left_aligned.et_pb_text_align_justified .et_pb_menu__wrap{-webkit-box-pack:justify;-ms-flex-pack:justify;justify-content:space-between}.et_pb_menu--style-inline_centered_logo .et_pb_menu_inner_container>.et_pb_menu__logo-wrap,.et_pb_menu--style-inline_centered_logo .et_pb_row>.et_pb_menu__logo-wrap{display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.et_pb_menu--style-inline_centered_logo .et_pb_menu_inner_container>.et_pb_menu__logo,.et_pb_menu--style-inline_centered_logo .et_pb_row>.et_pb_menu__logo{margin:0 auto}.et_pb_menu--style-inline_centered_logo .et_pb_menu__logo-slot{display:none}.et_pb_menu .et_pb_row{min-height:81px}.et_pb_menu .et_pb_menu__menu{display:none}.et_pb_menu .et_mobile_nav_menu{float:none;margin:0 6px;display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-align:center;-ms-flex-align:center;align-items:center}.et_pb_menu .et_mobile_menu{top:100%;padding:5%}.et_pb_menu .et_mobile_menu,.et_pb_menu .et_mobile_menu ul{list-style:none!important;text-align:left}.et_pb_menu .et_mobile_menu ul{padding:0}.et_pb_menu .et_pb_mobile_menu_upwards .et_mobile_menu{top:auto;bottom:100%}}
@-webkit-keyframes fadeOutTop{0%{opacity:1;-webkit-transform:translatey(0);transform:translatey(0)}to{opacity:0;-webkit-transform:translatey(-60%);transform:translatey(-60%)}}@keyframes fadeOutTop{0%{opacity:1;-webkit-transform:translatey(0);transform:translatey(0)}to{opacity:0;-webkit-transform:translatey(-60%);transform:translatey(-60%)}}@-webkit-keyframes fadeInTop{0%{opacity:0;-webkit-transform:translatey(-60%);transform:translatey(-60%)}to{opacity:1;-webkit-transform:translatey(0);transform:translatey(0)}}@keyframes fadeInTop{0%{opacity:0;-webkit-transform:translatey(-60%);transform:translatey(-60%)}to{opacity:1;-webkit-transform:translatey(0);transform:translatey(0)}}@-webkit-keyframes fadeInBottom{0%{opacity:0;-webkit-transform:translatey(60%);transform:translatey(60%)}to{opacity:1;-webkit-transform:translatey(0);transform:translatey(0)}}@keyframes fadeInBottom{0%{opacity:0;-webkit-transform:translatey(60%);transform:translatey(60%)}to{opacity:1;-webkit-transform:translatey(0);transform:translatey(0)}}@-webkit-keyframes fadeOutBottom{0%{opacity:1;-webkit-transform:translatey(0);transform:translatey(0)}to{opacity:0;-webkit-transform:translatey(60%);transform:translatey(60%)}}@keyframes fadeOutBottom{0%{opacity:1;-webkit-transform:translatey(0);transform:translatey(0)}to{opacity:0;-webkit-transform:translatey(60%);transform:translatey(60%)}}@-webkit-keyframes Grow{0%{opacity:0;-webkit-transform:scaleY(.5);transform:scaleY(.5)}to{opacity:1;-webkit-transform:scale(1);transform:scale(1)}}@keyframes Grow{0%{opacity:0;-webkit-transform:scaleY(.5);transform:scaleY(.5)}to{opacity:1;-webkit-transform:scale(1);transform:scale(1)}}/*!
	  * Animate.css - http://daneden.me/animate
	  * Licensed under the MIT license - http://opensource.org/licenses/MIT
	  * Copyright (c) 2015 Daniel Eden
	 */@-webkit-keyframes flipInX{0%{-webkit-transform:perspective(400px) rotateX(90deg);transform:perspective(400px) rotateX(90deg);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;opacity:0}40%{-webkit-transform:perspective(400px) rotateX(-20deg);transform:perspective(400px) rotateX(-20deg);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in}60%{-webkit-transform:perspective(400px) rotateX(10deg);transform:perspective(400px) rotateX(10deg);opacity:1}80%{-webkit-transform:perspective(400px) rotateX(-5deg);transform:perspective(400px) rotateX(-5deg)}to{-webkit-transform:perspective(400px);transform:perspective(400px)}}@keyframes flipInX{0%{-webkit-transform:perspective(400px) rotateX(90deg);transform:perspective(400px) rotateX(90deg);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;opacity:0}40%{-webkit-transform:perspective(400px) rotateX(-20deg);transform:perspective(400px) rotateX(-20deg);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in}60%{-webkit-transform:perspective(400px) rotateX(10deg);transform:perspective(400px) rotateX(10deg);opacity:1}80%{-webkit-transform:perspective(400px) rotateX(-5deg);transform:perspective(400px) rotateX(-5deg)}to{-webkit-transform:perspective(400px);transform:perspective(400px)}}@-webkit-keyframes flipInY{0%{-webkit-transform:perspective(400px) rotateY(90deg);transform:perspective(400px) rotateY(90deg);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;opacity:0}40%{-webkit-transform:perspective(400px) rotateY(-20deg);transform:perspective(400px) rotateY(-20deg);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in}60%{-webkit-transform:perspective(400px) rotateY(10deg);transform:perspective(400px) rotateY(10deg);opacity:1}80%{-webkit-transform:perspective(400px) rotateY(-5deg);transform:perspective(400px) rotateY(-5deg)}to{-webkit-transform:perspective(400px);transform:perspective(400px)}}@keyframes flipInY{0%{-webkit-transform:perspective(400px) rotateY(90deg);transform:perspective(400px) rotateY(90deg);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in;opacity:0}40%{-webkit-transform:perspective(400px) rotateY(-20deg);transform:perspective(400px) rotateY(-20deg);-webkit-animation-timing-function:ease-in;animation-timing-function:ease-in}60%{-webkit-transform:perspective(400px) rotateY(10deg);transform:perspective(400px) rotateY(10deg);opacity:1}80%{-webkit-transform:perspective(400px) rotateY(-5deg);transform:perspective(400px) rotateY(-5deg)}to{-webkit-transform:perspective(400px);transform:perspective(400px)}}
#main-header{line-height:23px;font-weight:500;top:0;background-color:#fff;width:100%;-webkit-box-shadow:0 1px 0 rgba(0,0,0,.1);box-shadow:0 1px 0 rgba(0,0,0,.1);position:relative;z-index:99999}.nav li li{padding:0 20px;margin:0}.et-menu li li a{padding:6px 20px;width:200px}.nav li{position:relative;line-height:1em}.nav li li{position:relative;line-height:2em}.nav li ul{position:absolute;padding:20px 0;z-index:9999;width:240px;background:#fff;visibility:hidden;opacity:0;border-top:3px solid #2ea3f2;box-shadow:0 2px 5px rgba(0,0,0,.1);-moz-box-shadow:0 2px 5px rgba(0,0,0,.1);-webkit-box-shadow:0 2px 5px rgba(0,0,0,.1);-webkit-transform:translateZ(0);text-align:left}.nav li.et-hover>ul{visibility:visible}.nav li.et-touch-hover>ul,.nav li:hover>ul{opacity:1;visibility:visible}.nav li li ul{z-index:1000;top:-23px;left:240px}.nav li.et-reverse-direction-nav li ul{left:auto;right:240px}.nav li:hover{visibility:inherit}.et_mobile_menu li a,.nav li li a{font-size:14px;-webkit-transition:opacity .2s ease-in-out,background-color .2s ease-in-out;transition:opacity .2s ease-in-out,background-color .2s ease-in-out}.et_mobile_menu li a:hover,.nav ul li a:hover{background-color:rgba(0,0,0,.03);opacity:.7}.et-dropdown-removing>ul{display:none}.mega-menu .et-dropdown-removing>ul{display:block}.et-menu .menu-item-has-children>a:first-child:after{font-family:ETmodules;content:"3";font-size:16px;position:absolute;right:0;top:0;font-weight:800}.et-menu .menu-item-has-children>a:first-child{padding-right:20px}.et-menu li li.menu-item-has-children>a:first-child:after{right:20px;top:6px}.et-menu-nav li.mega-menu{position:inherit}.et-menu-nav li.mega-menu>ul{padding:30px 20px;position:absolute!important;width:100%;left:0!important}.et-menu-nav li.mega-menu ul li{margin:0;float:left!important;display:block!important;padding:0!important}.et-menu-nav li.mega-menu li>ul{-webkit-animation:none!important;animation:none!important;padding:0;border:none;left:auto;top:auto;width:240px!important;position:relative;box-shadow:none;-webkit-box-shadow:none}.et-menu-nav li.mega-menu li ul{visibility:visible;opacity:1;display:none}.et-menu-nav li.mega-menu.et-hover li ul,.et-menu-nav li.mega-menu:hover li ul{display:block}.et-menu-nav li.mega-menu:hover>ul{opacity:1!important;visibility:visible!important}.et-menu-nav li.mega-menu>ul>li>a:first-child{padding-top:0!important;font-weight:700;border-bottom:1px solid rgba(0,0,0,.03)}.et-menu-nav li.mega-menu>ul>li>a:first-child:hover{background-color:transparent!important}.et-menu-nav li.mega-menu li>a{width:200px!important}.et-menu-nav li.mega-menu.mega-menu-parent li>a,.et-menu-nav li.mega-menu.mega-menu-parent li li{width:100%!important}.et-menu-nav li.mega-menu.mega-menu-parent li>.sub-menu{float:left;width:100%!important}.et-menu-nav li.mega-menu>ul>li{width:25%;margin:0}.et-menu-nav li.mega-menu.mega-menu-parent-3>ul>li{width:33.33%}.et-menu-nav li.mega-menu.mega-menu-parent-2>ul>li{width:50%}.et-menu-nav li.mega-menu.mega-menu-parent-1>ul>li{width:100%}.et_pb_fullwidth_menu li.mega-menu .menu-item-has-children>a:first-child:after,.et_pb_menu li.mega-menu .menu-item-has-children>a:first-child:after{display:none}.et_fullwidth_nav #top-menu li.mega-menu>ul{width:auto;left:30px!important;right:30px!important}.et_mobile_menu{position:absolute;left:0;padding:5%;background:#fff;width:100%;visibility:visible;opacity:1;display:none;z-index:9999;border-top:3px solid #2ea3f2;box-shadow:0 2px 5px rgba(0,0,0,.1);-moz-box-shadow:0 2px 5px rgba(0,0,0,.1);-webkit-box-shadow:0 2px 5px rgba(0,0,0,.1)}#main-header .et_mobile_menu li ul,.et_pb_fullwidth_menu .et_mobile_menu li ul,.et_pb_menu .et_mobile_menu li ul{visibility:visible!important;display:block!important;padding-left:10px}.et_mobile_menu li li{padding-left:5%}.et_mobile_menu li a{border-bottom:1px solid rgba(0,0,0,.03);color:#666;padding:10px 5%;display:block}.et_mobile_menu .menu-item-has-children>a{font-weight:700;background-color:rgba(0,0,0,.03)}.et_mobile_menu li .menu-item-has-children>a{background-color:transparent}.et_mobile_nav_menu{float:right;display:none}.mobile_menu_bar{position:relative;display:block;line-height:0}.mobile_menu_bar:before{content:"a";font-size:32px;position:relative;left:0;top:0;cursor:pointer}.et_pb_module .mobile_menu_bar:before{top:2px}.mobile_nav .select_page{display:none}
.et_pb_text{word-wrap:break-word}.et_pb_text ol,.et_pb_text ul{padding-bottom:1em}.et_pb_text>:last-child{padding-bottom:0}.et_pb_text_inner{position:relative}
.et_pb_widget_area_left{border-right:1px solid rgba(0,0,0,.1);padding-right:30px}.et_pb_widget_area_right{border-left:1px solid rgba(0,0,0,.1);padding-left:30px}.et_pb_sidebar_no_border{border:none;padding:0}.et_pb_widget_area ul{list-style:none!important;padding:0!important;line-height:inherit!important}@media (max-width:980px){.et_pb_bg_layout_dark_tablet .et_pb_widget li a{color:inherit}.et_pb_widget_area_left{padding-right:0;border-right:none}.et_pb_widget_area_right{padding-left:0;border-left:none}.et_pb_column .et_pb_widget{margin:0 5.5% 7.5% 0;width:47.25%;clear:none;float:left}.et_pb_column .et_pb_widget:nth-child(2n){margin-right:0}.et_pb_column .et_pb_widget:nth-child(odd){clear:both}.et_pb_row_1-2_1-4_1-4>.et_pb_column.et_pb_column_1_4 .et_pb_widget,.et_pb_row_1-2_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6 .et_pb_widget,.et_pb_row_1-4_1-4>.et_pb_column.et_pb_column_1_4 .et_pb_widget,.et_pb_row_1-4_1-4_1-2>.et_pb_column.et_pb_column_1_4 .et_pb_widget,.et_pb_row_1-5_1-5_3-5>.et_pb_column.et_pb_column_1_5 .et_pb_widget,.et_pb_row_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6 .et_pb_widget,.et_pb_row_1-6_1-6_1-6_1-2>.et_pb_column.et_pb_column_1_6 .et_pb_widget,.et_pb_row_1-6_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6 .et_pb_widget,.et_pb_row_3-5_1-5_1-5>.et_pb_column.et_pb_column_1_5 .et_pb_widget,.et_pb_row_4col>.et_pb_column.et_pb_column_1_4 .et_pb_widget,.et_pb_row_5col>.et_pb_column.et_pb_column_1_5 .et_pb_widget,.et_pb_row_6col>.et_pb_column.et_pb_column_1_6 .et_pb_widget{margin:0 0 11.5%;width:100%}}@media (max-width:767px){.et_pb_column .et_pb_widget{margin-right:0;width:100%}}@media (max-width:479px){.et_pb_column .et_pb_widget{margin-right:0;margin-bottom:11.5%;width:100%}.et_pb_row_1-2_1-4_1-4>.et_pb_column.et_pb_column_1_4 .et_pb_widget,.et_pb_row_1-2_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6 .et_pb_widget,.et_pb_row_1-4_1-4>.et_pb_column.et_pb_column_1_4 .et_pb_widget,.et_pb_row_1-4_1-4_1-2>.et_pb_column.et_pb_column_1_4 .et_pb_widget,.et_pb_row_1-5_1-5_3-5>.et_pb_column.et_pb_column_1_5 .et_pb_widget,.et_pb_row_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6 .et_pb_widget,.et_pb_row_1-6_1-6_1-6_1-2>.et_pb_column.et_pb_column_1_6 .et_pb_widget,.et_pb_row_1-6_1-6_1-6_1-6>.et_pb_column.et_pb_column_1_6 .et_pb_widget,.et_pb_row_3-5_1-5_1-5>.et_pb_column.et_pb_column_1_5 .et_pb_widget,.et_pb_row_4col>.et_pb_column.et_pb_column_1_4 .et_pb_widget,.et_pb_row_5col>.et_pb_column.et_pb_column_1_5 .et_pb_widget,.et_pb_row_6col>.et_pb_column.et_pb_column_1_6 .et_pb_widget{margin:0 0 11.5%;width:100%}}.et_pb_no_sidebar_vertical_divider .et_pb_widget_area_left{border-right:none}.et_pb_no_sidebar_vertical_divider .et_pb_widget_area_right{border-left:none}
.et_pb_with_border .et_pb_image_wrap{border:0 solid #333}.et_pb_image{margin-left:auto;margin-right:auto;line-height:0}.et_pb_image.aligncenter{text-align:center}.et_pb_image.et_pb_has_overlay a.et_pb_lightbox_image{display:block;position:relative}.et_pb_image{display:block}.et_pb_image .et_pb_image_wrap{display:inline-block;position:relative;max-width:100%}.et_pb_image .et_pb_image_wrap img[src*=".svg"]{width:auto}.et_pb_image img{position:relative}.et_pb_image_sticky{margin-bottom:0!important;display:inherit}.et_pb_image.et_pb_has_overlay .et_pb_image_wrap:hover .et_overlay{z-index:3;opacity:1}@media (min-width:981px){.et_pb_section_sticky,.et_pb_section_sticky.et_pb_bottom_divider .et_pb_row:nth-last-child(2),.et_pb_section_sticky .et_pb_column_single,.et_pb_section_sticky .et_pb_row.et-last-child,.et_pb_section_sticky .et_pb_row:last-child,.et_pb_section_sticky .et_pb_specialty_column .et_pb_row_inner.et-last-child,.et_pb_section_sticky .et_pb_specialty_column .et_pb_row_inner:last-child{padding-bottom:0!important}}@media (max-width:980px){.et_pb_image_sticky_tablet{margin-bottom:0!important;display:inherit}.et_pb_section_sticky_mobile,.et_pb_section_sticky_mobile.et_pb_bottom_divider .et_pb_row:nth-last-child(2),.et_pb_section_sticky_mobile .et_pb_column_single,.et_pb_section_sticky_mobile .et_pb_row.et-last-child,.et_pb_section_sticky_mobile .et_pb_row:last-child,.et_pb_section_sticky_mobile .et_pb_specialty_column .et_pb_row_inner.et-last-child,.et_pb_section_sticky_mobile .et_pb_specialty_column .et_pb_row_inner:last-child{padding-bottom:0!important}.et_pb_section_sticky .et_pb_row.et-last-child .et_pb_column.et_pb_row_sticky.et-last-child,.et_pb_section_sticky .et_pb_row:last-child .et_pb_column.et_pb_row_sticky:last-child{margin-bottom:0}.et_pb_image_bottom_space_tablet{margin-bottom:30px!important;display:block}.et_always_center_on_mobile{text-align:center!important;margin-left:auto!important;margin-right:auto!important}}@media (max-width:767px){.et_pb_image_sticky_phone{margin-bottom:0!important;display:inherit}.et_pb_image_bottom_space_phone{margin-bottom:30px!important;display:block}}
.et_overlay{z-index:-1;position:absolute;top:0;left:0;display:block;width:100%;height:100%;background:hsla(0,0%,100%,.9);opacity:0;pointer-events:none;-webkit-transition:all .3s;transition:all .3s;border:1px solid #e5e5e5;-webkit-box-sizing:border-box;box-sizing:border-box;-webkit-backface-visibility:hidden;backface-visibility:hidden;-webkit-font-smoothing:antialiased}.et_overlay:before{color:#2ea3f2;content:"\E050";position:absolute;top:50%;left:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);font-size:32px;-webkit-transition:all .4s;transition:all .4s}.et_portfolio_image,.et_shop_image{position:relative;display:block}.et_pb_has_overlay:not(.et_pb_image):hover .et_overlay,.et_portfolio_image:hover .et_overlay,.et_shop_image:hover .et_overlay{z-index:3;opacity:1}#ie7 .et_overlay,#ie8 .et_overlay{display:none}.et_pb_module.et_pb_has_overlay{position:relative}.et_pb_module.et_pb_has_overlay .et_overlay,article.et_pb_has_overlay{border:none}
</style>
<link rel='stylesheet' id='et-builder-googlefonts-cached-css' href='https://fonts.googleapis.com/css?family=Montserrat:100,200,300,regular,500,600,700,800,900,100italic,200italic,300italic,italic,500italic,600italic,700italic,800italic,900italic&#038;subset=latin,latin-ext&#038;display=swap' type='text/css' media='all' />
<link rel='stylesheet' id='directorist-openstreet-map-leaflet-css' href='https://fcmc.org/wp-content/plugins/directorist/assets/vendor-css/openstreet-map/leaflet.min.css?ver=7.12.7' type='text/css' media='all' />
<link rel='stylesheet' id='directorist-openstreet-map-openstreet-css' href='https://fcmc.org/wp-content/plugins/directorist/assets/vendor-css/openstreet-map/openstreet.min.css?ver=7.12.7' type='text/css' media='all' />
<link rel='stylesheet' id='directorist-main-style-css' href='https://fcmc.org/wp-content/plugins/directorist/assets/css/public-main.min.css?ver=7.12.7' type='text/css' media='all' />
<style id='directorist-main-style-inline-css' type='text/css'>
.pricing .price_action .price_action--btn,#directorist.atbd_wrapper .btn-primary,.default-ad-search .submit_btn .btn-default,.atbd_content_active #directorist.atbd_wrapper.dashboard_area .user_pro_img_area .user_img .choose_btn #upload_pro_pic,#directorist.atbd_wrapper .at-modal .at-modal-close,.atbdp_login_form_shortcode #loginform p input[type=submit],.atbd_manage_fees_wrapper .table tr .action p .btn-block,#directorist.atbd_wrapper #atbdp-checkout-form #atbdp_checkout_submit_btn,#directorist.atbd_wrapper .ezmu__btn,.default-ad-search .submit_btn .btn-primary,.directorist-btn.directorist-btn-primary,.directorist-content-active .widget.atbd_widget .directorist .btn,.directorist-btn.directorist-btn-dark,.atbd-add-payment-method form .atbd-save-card,#bhCopyTime,#bhAddNew,.bdb-select-hours .bdb-remove,.directorist-form-image-upload-field .ezmu__btn.ezmu__input-label,.directorist-content-active .widget.atbd_widget .atbd_author_info_widget .btn{color:#fff!important}.pricing .price_action .price_action--btn:hover,#directorist.atbd_wrapper .btn-primary:hover,.default-ad-search .submit_btn .btn-default:hover,.atbd_content_active #directorist.atbd_wrapper.dashboard_area .user_pro_img_area .user_img .choose_btn #upload_pro_pic:hover,#directorist.atbd_wrapper .at-modal .at-modal-close:hover,.atbdp_login_form_shortcode #loginform p input[type=submit]:hover,.atbd_manage_fees_wrapper .table tr .action p .btn-block:hover,#directorist.atbd_wrapper #atbdp-checkout-form #atbdp_checkout_submit_btn:hover,#directorist.atbd_wrapper .ezmu__btn:hover,.default-ad-search .submit_btn .btn-primary:hover,.directorist-btn.directorist-btn-primary:hover,.directorist-content-active .widget.atbd_widget .directorist .btn:hover,.directorist-btn.directorist-btn-dark:hover,.atbd-add-payment-method form .atbd-save-card:hover,#bhCopyTime:hover,#bhAddNew:hover,.bdb-select-hours .bdb-remove:hover,.directorist-form-image-upload-field .ezmu__btn.ezmu__input-label:hover,.directorist-content-active .widget.atbd_widget .atbd_author_info_widget .btn:hover{color:#fff!important}.pricing .price_action .price_action--btn,#directorist.atbd_wrapper .btn-primary,.default-ad-search .submit_btn .btn-default,.atbd_content_active #directorist.atbd_wrapper.dashboard_area .user_pro_img_area .user_img .choose_btn #upload_pro_pic,#directorist.atbd_wrapper .at-modal .at-modal-close,.atbdp_login_form_shortcode #loginform p input[type=submit],.atbd_manage_fees_wrapper .table tr .action p .btn-block,#directorist.atbd_wrapper #atbdp-checkout-form #atbdp_checkout_submit_btn,#directorist.atbd_wrapper .ezmu__btn,.default-ad-search .submit_btn .btn-primary,.directorist-btn.directorist-btn-primary,.directorist-content-active .widget.atbd_widget .directorist .btn,.directorist-btn.directorist-btn-dark,.atbd-add-payment-method form .atbd-save-card,#bhCopyTime,#bhAddNew,.bdb-select-hours .bdb-remove,.directorist-form-image-upload-field .ezmu__btn.ezmu__input-label,.directorist-content-active .widget.atbd_widget .atbd_author_info_widget .btn{background:#444752!important}.pricing .price_action .price_action--btn:hover,#directorist.atbd_wrapper .btn-primary:hover,#directorist.atbd_wrapper .at-modal .at-modal-close:hover,.default-ad-search .submit_btn .btn-default:hover,.atbd_content_active #directorist.atbd_wrapper.dashboard_area .user_pro_img_area .user_img .choose_btn #upload_pro_pic:hover,.atbdp_login_form_shortcode #loginform p input[type=submit]:hover,#directorist.atbd_wrapper .ezmu__btn:hover,.default-ad-search .submit_btn .btn-primary:hover,.directorist-btn.directorist-btn-primary:hover,.directorist-content-active .widget.atbd_widget .directorist .btn:hover,.directorist-btn.directorist-btn-dark:hover,.atbd-add-payment-method form .atbd-save-card:hover,#bhCopyTime:hover,#bhAddNew:hover,.bdb-select-hours .bdb-remove:hover,.directorist-form-image-upload-field .ezmu__btn.ezmu__input-label:hover,.directorist-content-active .widget.atbd_widget .atbd_author_info_widget .btn:hover{background:#222!important}#directorist.atbd_wrapper .btn-primary,.default-ad-search .submit_btn .btn-default,.atbdp_login_form_shortcode #loginform p input[type=submit],.default-ad-search .submit_btn .btn-primary,.directorist-btn.directorist-btn-primary,.directorist-content-active .widget.atbd_widget .directorist .btn,.atbd-add-payment-method form .atbd-save-card,.directorist-content-active .widget.atbd_widget .atbd_author_info_widget .btn{border-color:#444752!important}#directorist.atbd_wrapper .btn-primary:hover,.default-ad-search .submit_btn .btn-default:hover,.atbdp_login_form_shortcode #loginform p input[type=submit]:hover,.default-ad-search .submit_btn .btn-primary:hover,.directorist-btn.directorist-btn-primary:hover,.directorist-content-active .widget.atbd_widget .directorist .btn:hover,.atbd-add-payment-method form .atbd-save-card:hover,.directorist-content-active .widget.atbd_widget .atbd_author_info_widget .btn:hover{border-color:#222!important}#directorist.atbd_wrapper .btn-secondary,.directorist-btn.directorist-btn-secondary{color:#fff!important}#directorist.atbd_wrapper .btn-secondary:hover,.directorist-btn.directorist-btn-secondary:hover{color:#fff!important}#directorist.atbd_wrapper .btn-secondary,.directorist-btn.directorist-btn-secondary{background:#122069!important}#directorist.atbd_wrapper .btn-secondary:hover,.directorist-btn.directorist-btn-secondary:hover{background:#131469!important}#directorist.atbd_wrapper .btn-secondary,.directorist-btn.directorist-btn-secondary{border-color:#131469!important}#directorist.atbd_wrapper .btn-secondary:hover,.directorist-btn.directorist-btn-secondary:hover{border-color:#131469!important}#directorist.atbd_wrapper .btn-danger,.atbd_content_active #directorist.atbd_wrapper.dashboard_area .user_pro_img_area .user_img #remove_pro_pic,.sweet-alert button.confirm,.directorist-form-social-fields__remove,.directorist-btn.directorist-btn-danger{color:#fff!important}#directorist.atbd_wrapper .btn-danger:hover,.atbd_content_active #directorist.atbd_wrapper.dashboard_area .user_pro_img_area .user_img #remove_pro_pic,.sweet-alert button.confirm:hover,.directorist-form-social-fields__remove:hover,.directorist-btn.directorist-btn-danger:hover{color:#fff!important}#directorist.atbd_wrapper .btn-danger,.atbd_content_active #directorist.atbd_wrapper.dashboard_area .user_pro_img_area .user_img #remove_pro_pic,.sweet-alert button.confirm,.directorist-form-social-fields__remove,.directorist-btn.directorist-btn-danger{background:#e23636!important}#directorist.atbd_wrapper .btn-danger:hover,.atbd_content_active #directorist.atbd_wrapper.dashboard_area .user_pro_img_area .user_img #remove_pro_pic:hover,.sweet-alert button.confirm:hover,.directorist-form-social-fields__remove:hover,.directorist-btn.directorist-btn-danger:hover{background:#c5001e!important}#directorist.atbd_wrapper .btn-danger,.directorist-btn.directorist-btn-danger{border-color:#e23636!important}#directorist.atbd_wrapper .btn-danger:hover,.directorist-btn.directorist-btn-danger:hover{border-color:#c5001e!important}#directorist.atbd_wrapper .btn-success{color:#fff!important}#directorist.atbd_wrapper .btn-success:hover{color:#fff!important}#directorist.atbd_wrapper .btn-success{background:#32cc6f!important}#directorist.atbd_wrapper .btn-success:hover{background:#2ba251!important}#directorist.atbd_wrapper .btn-success{border-color:#32cc6f!important}#directorist.atbd_wrapper .btn-success:hover{border-color:#2ba251!important}.atbd_content_active #directorist.atbd_wrapper .atbd_submit_btn_wrapper .more-filter,#directorist.atbd_wrapper .btn-outline-primary,.atbd_dropdown .atbd_dropdown-toggle,.directorist-btn.directorist-btn-outline-dark,.directorist-btn.directorist-btn-outline-primary{color:#444752!important}.atbd_content_active #directorist.atbd_wrapper .atbd_submit_btn_wrapper .more-filter:hover,#directorist.atbd_wrapper .btn-outline-primary:hover,.atbd_dropdown .atbd_dropdown-toggle:hover,.directorist-btn.directorist-btn-outline-dark:hover,.directorist-btn.directorist-btn-outline-primary:hover{color:#444752!important}.atbd_content_active #directorist.atbd_wrapper .atbd_submit_btn_wrapper .more-filter,#directorist.atbd_wrapper .btn-outline-primary,.atbd_dropdown .atbd_dropdown-toggle,.directorist-btn.directorist-btn-outline-dark,.directorist-btn.directorist-btn-outline-primary{border:1px solid #444752!important}.atbd_dropdown .atbd_dropdown-toggle .atbd_drop-caret:before{border-left:1px solid #444752!important;border-bottom:1px solid #444752!important}.atbd_content_active #directorist.atbd_wrapper .atbd_submit_btn_wrapper .more-filter:hover,#directorist.atbd_wrapper .btn-outline-primary:hover,.atbd_dropdown .atbd_dropdown-toggle:hover,.directorist-btn.directorist-btn-outline-dark:hover,.directorist-btn.directorist-btn-outline-primary:hover{border-color:#9299b8!important}.atbd_dropdown .atbd_dropdown-toggle:hover .atbd_drop-caret:before{border-left-color:#9299b8!important;border-bottom-color:#9299b8!important}.atbd_content_active #directorist.atbd_wrapper .atbd_submit_btn_wrapper .more-filter,#directorist.atbd_wrapper .btn-outline-primary,.atbd_dropdown .atbd_dropdown-toggle,.directorist-btn.directorist-btn-outline-dark,.directorist-btn.directorist-btn-outline-primary{background:#fff!important}.atbd_content_active #directorist.atbd_wrapper .atbd_submit_btn_wrapper .more-filter:hover,#directorist.atbd_wrapper .btn-outline-primary:hover,.atbd_dropdown .atbd_dropdown-toggle:hover,.directorist-btn.directorist-btn-outline-dark:hover,.directorist-btn.directorist-btn-outline-primary:hover{background:#fff!important}.atbdp_float_none .btn.btn-outline-light,.atbd_content_active #directorist.atbd_wrapper .atbd_content_module__tittle_area .atbd_listing_action_area .atbd_action,.atbd_content_active #directorist.atbd_wrapper .atbd_content_module__tittle_area .atbd_listing_action_area .atbd_action a,.directorist-signle-listing-top__btn-edit.directorist-btn.directorist-btn-outline-light{color:#444752!important}.atbdp_float_none .btn.btn-outline-light:hover,.atbd_content_active #directorist.atbd_wrapper .atbd_content_module__tittle_area .atbd_listing_action_area .atbd_action:hover,.atbd_content_active #directorist.atbd_wrapper .atbd_content_module__tittle_area .atbd_listing_action_area .atbd_action a:hover,.directorist-signle-listing-top__btn-edit.directorist-btn.directorist-btn-outline-light:hover{color:#fff!important}.atbdp_float_none .btn.btn-outline-light,.atbd_content_active #directorist.atbd_wrapper .atbd_content_module__tittle_area .atbd_listing_action_area .atbd_action,.directorist-signle-listing-top__btn-edit.directorist-btn.directorist-btn-outline-light{border:1px solid #e3e6ef!important}.atbdp_float_none .btn.btn-outline-light:hover,.atbd_content_active #directorist.atbd_wrapper .atbd_content_module__tittle_area .atbd_listing_action_area .atbd_action:hover,.directorist-signle-listing-top__btn-edit.directorist-btn.directorist-btn-outline-light:hover{border-color:#444752!important}.atbdp_float_none .btn.btn-outline-light,.atbd_content_active #directorist.atbd_wrapper .atbd_content_module__tittle_area .atbd_listing_action_area .atbd_action,.directorist-signle-listing-top__btn-edit.directorist-btn.directorist-btn-outline-light{background:#fff!important}.atbdp_float_none .btn.btn-outline-light:hover,.atbd_content_active #directorist.atbd_wrapper .atbd_content_module__tittle_area .atbd_listing_action_area .atbd_action:hover,.directorist-signle-listing-top__btn-edit.directorist-btn.directorist-btn-outline-light:hover{background:#444752!important}#directorist.atbd_wrapper .btn-outline-danger{color:#e23636!important}#directorist.atbd_wrapper .btn-outline-danger:hover{color:#fff!important}#directorist.atbd_wrapper .btn-outline-danger{border:1px solid #e23636!important}#directorist.atbd_wrapper .btn-outline-danger:hover{border-color:#e23636!important}#directorist.atbd_wrapper .btn-outline-danger{background:#fff!important}#directorist.atbd_wrapper .btn-outline-danger:hover{background:#e23636!important}.directorist-btn.directorist-btn-lighter{color:#1A1B29!important}.directorist-btn.directorist-btn-lighter:hover{color:#1A1B29!important}.directorist-btn.directorist-btn-lighter{border:1px solid #F6F7F9!important}.directorist-btn.directorist-btn-lighter:hover{border-color:#F6F7F9!important}.directorist-btn.directorist-btn-lighter{background:#F6F7F9!important}.directorist-btn.directorist-btn-lighter:hover{background:#1A1B29!important}.atbd_bg-success,.atbd_content_active #directorist.atbd_wrapper .atbd_badge.atbd_badge_open,.atbd_content_active .widget.atbd_widget[id^=bd] .atbd_badge.atbd_badge_open,.atbd_content_active .widget.atbd_widget[id^=dcl] .atbd_badge.atbd_badge_open,.atbd_content_active #directorist.atbd_wrapper .widget.atbd_widget .atbd_badge.atbd_badge_open,.directorist-badge-open,.directorist-badge.directorist-badge-success{background:#32cc6f!important}.atbd_bg-danger,.atbd_content_active #directorist.atbd_wrapper .atbd_give_review_area #atbd_up_preview .atbd_up_prev .rmrf:hover,.atbd_content_active #directorist.atbd_wrapper .atbd_badge.atbd_badge_close,.atbd_content_active .widget.atbd_widget[id^=bd] .atbd_badge.atbd_badge_close,.atbd_content_active .widget.atbd_widget[id^=dcl] .atbd_badge.atbd_badge_close,.atbd_content_active #directorist.atbd_wrapper .widget.atbd_widget .atbd_badge.atbd_badge_close,.directorist-badge.directorist-badge-danger,.directorist-listing-single .directorist-badge.directorist-badge-closejhg{background:#e23636!important}.atbd_bg-badge-feature,.atbd_content_active #directorist.atbd_wrapper .atbd_badge.atbd_badge_featured,.atbd_content_active .widget.atbd_widget[id^=bd] .atbd_badge.atbd_badge_featured,.atbd_content_active .widget.atbd_widget[id^=dcl] .atbd_badge.atbd_badge_featured,.atbd_content_active #directorist.atbd_wrapper .widget.atbd_widget .atbd_badge.atbd_badge_featured,.directorist-listing-single .directorist-badge.directorist-badge-featured{background:#fa8b0c!important}.atbd_bg-badge-popular,.atbd_content_active #directorist.atbd_wrapper .atbd_badge.atbd_badge_popular,.atbd_content_active .widget.atbd_widget[id^=bd] .atbd_badge.atbd_badge_popular,.atbd_content_active .widget.atbd_widget[id^=dcl] .atbd_badge.atbd_badge_popular,.atbd_content_active #directorist.atbd_wrapper .widget.atbd_widget .atbd_badge.atbd_badge_popular,.directorist-listing-single .directorist-badge.directorist-badge-popular{background:#f51957!important}.atbd_content_active #directorist.atbd_wrapper .atbd_badge.atbd_badge_new,.directorist-listing-single .directorist-badge.directorist-badge-new{background:#122069!important}.ads-advanced .price-frequency .pf-btn input:checked+span,.btn-checkbox label input:checked+span,.atbdpr-range .ui-slider-horizontal .ui-slider-range,.custom-control .custom-control-input:checked~.check--select,#directorist.atbd_wrapper .pagination .nav-links .current,.atbd_director_social_wrap a,.widget.atbd_widget[id^=bd] .atbd_author_info_widget .atbd_social_wrap p a,.widget.atbd_widget[id^=dcl] .atbd_author_info_widget .atbd_social_wrap p a,.directorist-mark-as-favorite__btn.directorist-added-to-favorite,.atbd_content_active #directorist.atbd_wrapper .widget.atbd_widget .atbdp-widget-categories>ul.atbdp_parent_category>li:hover>a span,.atbd_content_active #directorist.atbd_wrapper .widget.atbd_widget .atbdp.atbdp-widget-tags ul li a:hover{background:#444752!important}.ads-advanced .price-frequency .pf-btn input:checked+span,.btn-checkbox label input:checked+span,.directorist-content-active .directorist-type-nav__list .current .directorist-type-nav__link,.atbdpr-range .ui-slider-horizontal .ui-slider-handle,.custom-control .custom-control-input:checked~.check--select,.custom-control .custom-control-input:checked~.radio--select,#atpp-plan-change-modal .atm-contents-inner .dcl_pricing_plan input:checked+label:before,#dwpp-plan-renew-modal .atm-contents-inner .dcl_pricing_plan input:checked+label:before{border-color:#444752!important}.atbd_map_shape{background:#444752!important}.atbd_map_shape:before{border-top-color:#444752!important}.map-icon-label i,.atbd_map_shape>span{color:#444752!important}
</style>
<link rel='stylesheet' id='directorist-select2-style-css' href='https://fcmc.org/wp-content/plugins/directorist/assets/vendor-css/select2.min.css?ver=7.12.7' type='text/css' media='all' />
<link rel='stylesheet' id='directorist-ez-media-uploader-style-css' href='https://fcmc.org/wp-content/plugins/directorist/assets/vendor-css/ez-media-uploader.min.css?ver=7.12.7' type='text/css' media='all' />
<link rel='stylesheet' id='directorist-slick-style-css' href='https://fcmc.org/wp-content/plugins/directorist/assets/vendor-css/slick.min.css?ver=7.12.7' type='text/css' media='all' />
<link rel='stylesheet' id='directorist-sweetalert-style-css' href='https://fcmc.org/wp-content/plugins/directorist/assets/vendor-css/sweetalert.min.css?ver=7.12.7' type='text/css' media='all' />
<link rel='stylesheet' id='divi-style-css' href='https://fcmc.org/wp-content/themes/franklin-county-medical-center/style.css?ver=4.25.1' type='text/css' media='all' />
<link rel="https://api.w.org/" href="https://fcmc.org/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://fcmc.org/wp-json/wp/v2/pages/54" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://fcmc.org/xmlrpc.php?rsd" />
<meta name="generator" content="WordPress 6.6.2" />
<link rel='shortlink' href='https://fcmc.org/?p=54' />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://fcmc.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ffcmc.org%2Fservices%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://fcmc.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ffcmc.org%2Fservices%2F&#038;format=xml" />
	<script data-name="dbdb-head-js">
	    function db014_update_icon(icon_id, icon_url) {
    db014_update_icons(jQuery(document), icon_id, icon_url);
    var $app_frame = jQuery("#et-fb-app-frame");
    if ($app_frame) {
    db014_update_icons($app_frame.contents(), icon_id, icon_url);
    }
    }

    function db014_update_icons(doc, icon_id, icon_url) {
    db014_update_custom_icons(doc, icon_id, icon_url);
    db014_update_custom_inline_icons(doc, icon_id, icon_url);
    }

    function db014_update_custom_icons(doc, icon_id, icon_url) {
    var $custom_icons = doc.find(".et-pb-icon,.dsm_icon,.dsm_icon_list_icon,.dsm_content_icon,.dsm_faq-item-open_icon,.dsm_faq-item-close_icon,.dsm_open_icon,.dsm_close_icon").filter(':contains("'+icon_id+'")');
    var icon_visible = (icon_url !== '');
    var $icons = $custom_icons.filter(function(){ return jQuery(this).text().trim() == icon_id; });
    $icons.addClass('db-custom-icon');
    $icons.html('<img class="dbdb-custom-icon-img" src="'+icon_url+'" />');
    $icons.toggle(icon_visible);
    }

    function db014_update_custom_inline_icons(doc, icon_id, icon_url) {
    var $custom_inline_icons = doc.find(".et_pb_inline_icon,.swiper-button-prev,.swiper-button-next").filter('[data-icon="'+icon_id+'"]');
    var icon_visible = (icon_url !== '');
    var $icons_inline = $custom_inline_icons.filter(function(){ return jQuery(this).attr('data-icon') == icon_id; });
    $icons_inline.addClass('db-custom-icon');
    $icons_inline.each(function(){
    $this = jQuery(this);
    if ($this.children('.db014_custom_hover_icon').length === 0) {
    if ($this.closest('.et_pb_dmb_breadcrumbs').length === 0) {
    $this.html('<img class="db014_custom_hover_icon" />');
    } else {
    $this.prepend(jQuery('<img class="db014_custom_hover_icon" />'));
    $this.addClass('db014_breadcrumb_with_custom_icon');
    }
    }
    $this.children('.db014_custom_hover_icon').attr('src', icon_url);
    });
    $icons_inline.toggle(icon_visible);
    }
 
	</script>
<style>
.db_title, .db_tagline { 
    margin-right: 30px;
    margin-top: 0px;
    line-height: 1em;
}
.db_title_and_tagline {
    display: flex;
    align-items: flex-start;
}
.db_tagline_below_title_on .db_title_and_tagline {
    flex-direction: column;
}
.db_tagline_below_title_on .db_tagline {
    margin-top: 8px;
}
.db_title_and_tagline_valign_middle .db_title_and_tagline {
    align-items: center;
}
.db_title_and_tagline_valign_bottom .db_title_and_tagline {
    align-items: flex-end;
}
.db_title_and_tagline_below_logo_on .db_title_and_tagline {
    position: absolute;
    bottom: 0px;
    left: 0px;
    transform: translateY(100%);
}
</style>
    <style>
/* Display the team member icons */
.db_pb_team_member_website_icon:before{content:"\e0e3";}
.db_pb_team_member_email_icon:before{content:"\e010";}
.db_pb_team_member_instagram_icon:before{content:"\e09a";}

/* Fix email icon hidden by Email Address Encoder plugin */
ul.et_pb_member_social_links li > span { 
	display: inline-block !important; 
}
</style>
<style>
@media only screen and (min-width: 981px) {
    .et_pb_module.db_inline_form .et_pb_newsletter_fields > p { 
        flex: auto !important;
    }
    .et_pb_module.db_inline_form .et_pb_newsletter_fields p.et_pb_newsletter_field {
        margin-right: 2%; 
    }
}
</style>
    <style>
        .et_pb_slider.dbdb_slider_random .et-pb-active-slide {
            visibility: hidden;
        }
    </style>
    <style>
        .et_pb_gallery .et-pb-slider-arrows a {
            margin-top: 0;
            transform: translateY(-50%);
        }
    </style>
    <style>
        .et_pb_gallery .et-pb-controllers a {
            border-style: solid;
        }
    </style>
    <style>
        /* Custom icons */
        .db-custom-icon {
            line-height: unset !important;
        }

        .db-custom-icon img {
            height: 1em;
        }

        .et_pb_blurb_position_left .db-custom-icon,
        .et_pb_blurb_position_right .db-custom-icon {
            width: 1em;
            display: block;
        }

        .et_pb_blurb_position_left .dbdb-custom-icon-img,
        .et_pb_blurb_position_right .dbdb-custom-icon-img {
            height: auto;
            vertical-align: top;
        }

        /* Custom button icons */
        .et_pb_custom_button_icon[data-icon^="wtfdivi014-url"]:before,
        .et_pb_custom_button_icon[data-icon^="wtfdivi014-url"]:after,
        .db-custom-extended-icon:before,
        .db-custom-extended-icon:after {
            background-size: auto 1em;
            background-repeat: no-repeat;
            min-width: 20em;
            height: 100%;
            content: "" !important;
            position: absolute;
            top: 0;
        }

        .et_pb_custom_button_icon[data-icon^="wtfdivi014-url"]:before,
        .et_pb_custom_button_icon[data-icon^="wtfdivi014-url"]:after {
            background-position: left center;
        }

        .et_pb_custom_button_icon[data-icon^="wtfdivi014-url"],
        .db-custom-extended-icon {
            overflow: hidden;
        }

        .db-custom-extended-icon:before {
            left: 0;
            background-position: 2em;
        }

        .db-custom-extended-icon:after {
            right: 0;
            background-position: right 0.7em center;
        }

        .dbdb-icon-on-hover-off .db-custom-extended-icon:after {
            transition: none !important;
        }

        /* Inline icons */
        .et_pb_posts .et_pb_inline_icon[data-icon^="wtfdivi014-url"]:before,
        .et_pb_portfolio_item .et_pb_inline_icon[data-icon^="wtfdivi014-url"]:before {
            content: '' !important;
            -webkit-transition: all 0.4s;
            -moz-transition: all 0.4s;
            transition: all 0.4s;
        }

        .et_pb_posts .entry-featured-image-url:hover .et_pb_inline_icon[data-icon^="wtfdivi014-url"] img,
        .et_pb_portfolio_item .et_portfolio_image:hover .et_pb_inline_icon[data-icon^="wtfdivi014-url"] img {
            margin-top: 0px;
            transition: all 0.4s;
        }

        .et_pb_posts .entry-featured-image-url .et_pb_inline_icon[data-icon^="wtfdivi014-url"] img,
        .et_pb_portfolio_item .et_portfolio_image .et_pb_inline_icon[data-icon^="wtfdivi014-url"] img {
            margin-top: 14px;
        }

        /* Custom hover icons */
        .db014_custom_hover_icon {
            width: auto !important;
            max-width: 32px !important;
            min-width: 0 !important;
            height: auto !important;
            max-height: 32px !important;
            min-height: 0 !important;
            position: absolute;
            top: 50%;
            left: 50%;
            -webkit-transform: translate(-50%, -50%);
            -moz-transform: translate(-50%, -50%);
            -ms-transform: translate(-50%, -50%);
            transform: translate(-50%, -50%);
        }

        .et_pb_dmb_breadcrumbs a:first-child .db014_custom_hover_icon,
        .et_pb_dmb_breadcrumbs li .db014_custom_hover_icon {
            position: relative !important;
            left: 0%;
            transform: none;
            vertical-align: middle;
            margin-right: 8px;
        }

        .et_pb_dmb_breadcrumbs li .db014_custom_hover_icon {
            margin-left: 4px;
        }

        .et_pb_fullwidth_portfolio .et_overlay .db014_custom_hover_icon {
            top: 45%;
            -webkit-transition: all .3s;
            transition: all .3s;
        }

        .et_pb_fullwidth_portfolio .et_pb_portfolio_image:hover .et_overlay .db014_custom_hover_icon {
            top: 33%;
        }

        /* Hide extra icons */
        .et_pb_gallery .et_pb_gallery_image .et_pb_inline_icon[data-icon^="wtfdivi014-url"]:before,
        .et_pb_blog_grid .et_pb_inline_icon[data-icon^="wtfdivi014-url"]:before,
        .et_pb_image .et_pb_image_wrap .et_pb_inline_icon[data-icon^="wtfdivi014-url"]:before,
        .et_pb_dmb_breadcrumbs ol>li>a:first-child[data-icon^="wtfdivi014-url"]:before,
        .et_pb_dmb_breadcrumbs ol>li[data-icon^="wtfdivi014-url"]:before,
        .et_pb_module.et_pb_dmb_breadcrumbs li.db014_breadcrumb_with_custom_icon:before {
            display: none !important;
        }

        span.db-custom-icon {
            color: rgba(0, 0, 0, 0) !important;
        }

        /* Override styles added by customizer button section */
        .et_button_no_icon .db-custom-extended-icon.et_pb_button:after {
            display: inline-block;
        }

        .et_button_no_icon .et_pb_module:not(.dbdb-has-custom-padding) .db-custom-extended-icon.et_pb_button:hover {
            padding: .3em 2em .3em .7em !important;
        }
    </style>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" />			<style>
			.et_pb_custom_button_icon[data-icon="wtfdivi014-url0"]:before, 
			.et_pb_custom_button_icon[data-icon="wtfdivi014-url0"]:after,
            .et_pb_button[data-icon="ࠀ"]:before,
            .et_pb_button[data-icon="ࠀ"]:after {
				background-image: url('http://fcmc.org/wp-content/uploads/2023/09/AdobeStock_151266003_Preview-doctor.png');		
			}
			</style>			<style>
			.et_pb_custom_button_icon[data-icon="wtfdivi014-url1"]:before, 
			.et_pb_custom_button_icon[data-icon="wtfdivi014-url1"]:after,
            .et_pb_button[data-icon="ࠁ"]:before,
            .et_pb_button[data-icon="ࠁ"]:after {
				background-image: url('http://fcmc.org/wp-content/uploads/2023/09/AdobeStock_151266003_Preview-cross150.png');		
			}
			</style>			<style>
			.et_pb_custom_button_icon[data-icon="wtfdivi014-url2"]:before, 
			.et_pb_custom_button_icon[data-icon="wtfdivi014-url2"]:after,
            .et_pb_button[data-icon="ࠂ"]:before,
            .et_pb_button[data-icon="ࠂ"]:after {
				background-image: url('http://fcmc.org/wp-content/uploads/2024/02/medical-icon.png');		
			}
			</style>			<style>
			.et_pb_custom_button_icon[data-icon="wtfdivi014-url3"]:before, 
			.et_pb_custom_button_icon[data-icon="wtfdivi014-url3"]:after,
            .et_pb_button[data-icon="ࠃ"]:before,
            .et_pb_button[data-icon="ࠃ"]:after {
				background-image: url('http://fcmc.org/wp-content/uploads/2024/02/doctor-icon.png');		
			}
			</style><!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-QYWF8FN34Z"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-QYWF8FN34Z');
</script>

<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-PR6GQ39');</script>
<!-- End Google Tag Manager --><link rel="icon" href="https://fcmc.org/wp-content/uploads/2023/09/cropped-icon-32x32.png" sizes="32x32" />
<link rel="icon" href="https://fcmc.org/wp-content/uploads/2023/09/cropped-icon-192x192.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://fcmc.org/wp-content/uploads/2023/09/cropped-icon-180x180.png" />
<meta name="msapplication-TileImage" content="https://fcmc.org/wp-content/uploads/2023/09/cropped-icon-270x270.png" />
<style id="et-critical-inline-css">body,.et_pb_column_1_2 .et_quote_content blockquote cite,.et_pb_column_1_2 .et_link_content a.et_link_main_url,.et_pb_column_1_3 .et_quote_content blockquote cite,.et_pb_column_3_8 .et_quote_content blockquote cite,.et_pb_column_1_4 .et_quote_content blockquote cite,.et_pb_blog_grid .et_quote_content blockquote cite,.et_pb_column_1_3 .et_link_content a.et_link_main_url,.et_pb_column_3_8 .et_link_content a.et_link_main_url,.et_pb_column_1_4 .et_link_content a.et_link_main_url,.et_pb_blog_grid .et_link_content a.et_link_main_url,body .et_pb_bg_layout_light .et_pb_post p,body .et_pb_bg_layout_dark .et_pb_post p{font-size:16px}.et_pb_slide_content,.et_pb_best_value{font-size:18px}body{color:#000000}h1,h2,h3,h4,h5,h6{color:#245885}body{line-height:1.8em}#et_search_icon:hover,.mobile_menu_bar:before,.mobile_menu_bar:after,.et_toggle_slide_menu:after,.et-social-icon a:hover,.et_pb_sum,.et_pb_pricing li a,.et_pb_pricing_table_button,.et_overlay:before,.entry-summary p.price ins,.et_pb_member_social_links a:hover,.et_pb_widget li a:hover,.et_pb_filterable_portfolio .et_pb_portfolio_filters li a.active,.et_pb_filterable_portfolio .et_pb_portofolio_pagination ul li a.active,.et_pb_gallery .et_pb_gallery_pagination ul li a.active,.wp-pagenavi span.current,.wp-pagenavi a:hover,.nav-single a,.tagged_as a,.posted_in a{color:#245885}.et_pb_contact_submit,.et_password_protected_form .et_submit_button,.et_pb_bg_layout_light .et_pb_newsletter_button,.comment-reply-link,.form-submit .et_pb_button,.et_pb_bg_layout_light .et_pb_promo_button,.et_pb_bg_layout_light .et_pb_more_button,.et_pb_contact p input[type="checkbox"]:checked+label i:before,.et_pb_bg_layout_light.et_pb_module.et_pb_button{color:#245885}.footer-widget h4{color:#245885}.et-search-form,.nav li ul,.et_mobile_menu,.footer-widget li:before,.et_pb_pricing li:before,blockquote{border-color:#245885}.et_pb_counter_amount,.et_pb_featured_table .et_pb_pricing_heading,.et_quote_content,.et_link_content,.et_audio_content,.et_pb_post_slider.et_pb_bg_layout_dark,.et_slide_in_menu_container,.et_pb_contact p input[type="radio"]:checked+label i:before{background-color:#245885}a{color:#245885}.nav li ul{border-color:#2ea3f2}#page-container #top-header{background-color:#245885!important}#et-secondary-nav li ul{background-color:#245885}#main-header .nav li ul a{color:rgba(0,0,0,0.7)}#main-footer{background-color:#f4f4f4}#footer-widgets .footer-widget a,#footer-widgets .footer-widget li a,#footer-widgets .footer-widget li a:hover{color:#245885}.footer-widget{color:#000000}#main-footer .footer-widget h4,#main-footer .widget_block h1,#main-footer .widget_block h2,#main-footer .widget_block h3,#main-footer .widget_block h4,#main-footer .widget_block h5,#main-footer .widget_block h6{color:#245885}.footer-widget li:before{border-color:rgba(36,88,133,0)}.footer-widget,.footer-widget li,.footer-widget li a,#footer-info{font-size:14px}.footer-widget .et_pb_widget div,.footer-widget .et_pb_widget ul,.footer-widget .et_pb_widget ol,.footer-widget .et_pb_widget label{line-height:1.7em}.bottom-nav,.bottom-nav a,.bottom-nav li.current-menu-item a{color:#000000}#et-footer-nav .bottom-nav li.current-menu-item a{color:#000000}#footer-bottom{background-color:#ffffff}#footer-info,#footer-info a{color:#000000}body .et_pb_button{font-size:18px;background-color:#245885;font-weight:normal;font-style:normal;text-transform:uppercase;text-decoration:none;}body.et_pb_button_helper_class .et_pb_button,body.et_pb_button_helper_class .et_pb_module.et_pb_button{color:#ffffff}body .et_pb_button:after{font-size:28.8px}body .et_pb_bg_layout_light.et_pb_button:hover,body .et_pb_bg_layout_light .et_pb_button:hover,body .et_pb_button:hover{color:#ffffff!important;background-color:#4786b4;border-radius:0px}h1,h2,h3,h4,h5,h6,.et_quote_content blockquote p,.et_pb_slide_description .et_pb_slide_title{font-weight:normal;font-style:normal;text-transform:uppercase;text-decoration:none}@media only screen and (min-width:981px){#main-footer .footer-widget h4,#main-footer .widget_block h1,#main-footer .widget_block h2,#main-footer .widget_block h3,#main-footer .widget_block h4,#main-footer .widget_block h5,#main-footer .widget_block h6{font-size:18px}.et_header_style_centered.et_hide_primary_logo #main-header:not(.et-fixed-header) .logo_container,.et_header_style_centered.et_hide_fixed_logo #main-header.et-fixed-header .logo_container{height:11.88px}}@media only screen and (min-width:1350px){.et_pb_row{padding:27px 0}.et_pb_section{padding:54px 0}.single.et_pb_pagebuilder_layout.et_full_width_page .et_post_meta_wrapper{padding-top:81px}.et_pb_fullwidth_section{padding:0}}h1,h1.et_pb_contact_main_title,.et_pb_title_container h1{font-size:48px}h2,.product .related h2,.et_pb_column_1_2 .et_quote_content blockquote p{font-size:41px}h3{font-size:35px}h4,.et_pb_circle_counter h3,.et_pb_number_counter h3,.et_pb_column_1_3 .et_pb_post h2,.et_pb_column_1_4 .et_pb_post h2,.et_pb_blog_grid h2,.et_pb_column_1_3 .et_quote_content blockquote p,.et_pb_column_3_8 .et_quote_content blockquote p,.et_pb_column_1_4 .et_quote_content blockquote p,.et_pb_blog_grid .et_quote_content blockquote p,.et_pb_column_1_3 .et_link_content h2,.et_pb_column_3_8 .et_link_content h2,.et_pb_column_1_4 .et_link_content h2,.et_pb_blog_grid .et_link_content h2,.et_pb_column_1_3 .et_audio_content h2,.et_pb_column_3_8 .et_audio_content h2,.et_pb_column_1_4 .et_audio_content h2,.et_pb_blog_grid .et_audio_content h2,.et_pb_column_3_8 .et_pb_audio_module_content h2,.et_pb_column_1_3 .et_pb_audio_module_content h2,.et_pb_gallery_grid .et_pb_gallery_item h3,.et_pb_portfolio_grid .et_pb_portfolio_item h2,.et_pb_filterable_portfolio_grid .et_pb_portfolio_item h2{font-size:28px}h5{font-size:25px}h6{font-size:22px}.et_pb_slide_description .et_pb_slide_title{font-size:73px}.et_pb_gallery_grid .et_pb_gallery_item h3,.et_pb_portfolio_grid .et_pb_portfolio_item h2,.et_pb_filterable_portfolio_grid .et_pb_portfolio_item h2,.et_pb_column_1_4 .et_pb_audio_module_content h2{font-size:25px}	h1,h2,h3,h4,h5,h6{font-family:'Montserrat',Helvetica,Arial,Lucida,sans-serif}body,input,textarea,select{font-family:'Montserrat',Helvetica,Arial,Lucida,sans-serif}.et_pb_section_0_tb_header.et_pb_section{padding-top:17px;padding-bottom:17px}.et_pb_row_0_tb_header.et_pb_row{padding-top:0px!important;padding-right:35px!important;padding-bottom:0px!important;padding-left:35px!important;padding-top:0px;padding-right:35px;padding-bottom:0px;padding-left:35px}.et_pb_row_0_tb_header,body #page-container .et-db #et-boc .et-l .et_pb_row_0_tb_header.et_pb_row,body.et_pb_pagebuilder_layout.single #page-container #et-boc .et-l .et_pb_row_0_tb_header.et_pb_row,body.et_pb_pagebuilder_layout.single.et_full_width_page #page-container #et-boc .et-l .et_pb_row_0_tb_header.et_pb_row{width:100%;max-width:2560px}.et_pb_menu_0_tb_header.et_pb_menu ul li a{text-transform:uppercase;font-size:16px}.et_pb_menu_0_tb_header.et_pb_menu{background-color:#ffffff}.et_pb_menu_0_tb_header{padding-top:0px;padding-bottom:0px;margin-top:0px!important;margin-bottom:0px!important}.et_pb_menu_0_tb_header.et_pb_menu ul li.current-menu-item a,.et_pb_menu_0_tb_header.et_pb_menu .nav li ul.sub-menu li.current-menu-item a{color:#245885!important}.et_pb_menu_0_tb_header.et_pb_menu .nav li ul{background-color:#FFFFFF!important;border-color:#245885}.et_pb_menu_0_tb_header.et_pb_menu .et_mobile_menu{border-color:#245885}.et_pb_menu_0_tb_header.et_pb_menu .nav li ul.sub-menu a,.et_pb_menu_0_tb_header.et_pb_menu .et_mobile_menu a{color:#000000!important}.et_pb_menu_0_tb_header.et_pb_menu .et_mobile_menu,.et_pb_menu_0_tb_header.et_pb_menu .et_mobile_menu ul{background-color:#FFFFFF!important}.et_pb_menu_0_tb_header .et_pb_menu_inner_container>.et_pb_menu__logo-wrap,.et_pb_menu_0_tb_header .et_pb_menu__logo-slot{width:10%;max-width:100%}.et_pb_menu_0_tb_header .et_pb_menu_inner_container>.et_pb_menu__logo-wrap .et_pb_menu__logo img,.et_pb_menu_0_tb_header .et_pb_menu__logo-slot .et_pb_menu__logo-wrap img{height:auto;max-height:none}.et_pb_menu_0_tb_header .mobile_nav .mobile_menu_bar:before,.et_pb_menu_0_tb_header .et_pb_menu__icon.et_pb_menu__cart-button{color:#245885}.et_pb_menu_0_tb_header .et_pb_menu__icon.et_pb_menu__search-button,.et_pb_menu_0_tb_header .et_pb_menu__icon.et_pb_menu__close-search-button{color:#939598}@media only screen and (max-width:980px){.et_pb_menu_0_tb_header .et_pb_menu_inner_container>.et_pb_menu__logo-wrap,.et_pb_menu_0_tb_header .et_pb_menu__logo-slot{width:20%}}@media only screen and (max-width:767px){.et_pb_menu_0_tb_header .et_pb_menu_inner_container>.et_pb_menu__logo-wrap,.et_pb_menu_0_tb_header .et_pb_menu__logo-slot{width:50%}}.et_pb_section_0_tb_footer{border-top-width:2px;border-bottom-width:2px;border-top-color:#245885;border-bottom-color:#245885}.et_pb_section_0_tb_footer.et_pb_section{background-color:#F4F4F4!important}.et_pb_text_0_tb_footer h1,.et_pb_text_2_tb_footer h1,.et_pb_text_4_tb_footer h1{font-size:72px}.et_pb_text_0_tb_footer h3,.et_pb_text_2_tb_footer h3,.et_pb_text_4_tb_footer h3{font-size:30px}.et_pb_text_0_tb_footer h6,.et_pb_text_2_tb_footer h6,.et_pb_text_4_tb_footer h6{font-size:22px}.et_pb_text_0_tb_footer,.et_pb_text_4_tb_footer{margin-bottom:5px!important}.et_pb_text_1_tb_footer h1,.et_pb_text_3_tb_footer h1,.et_pb_text_5_tb_footer h1{font-weight:700;font-size:26px}.et_pb_text_1_tb_footer,.et_pb_text_3_tb_footer,.et_pb_text_5_tb_footer{border-left-width:2px;border-left-color:#245885;padding-top:0px!important;padding-left:15px!important;margin-top:0px!important;margin-left:5px!important}.et_pb_text_2_tb_footer{padding-top:40px!important;margin-bottom:5px!important}.et_pb_image_0_tb_footer{padding-top:50px;text-align:left;margin-left:0}@media only screen and (min-width:981px){.et_pb_image_0_tb_footer{width:50%}}@media only screen and (max-width:980px){.et_pb_section_0_tb_footer{border-top-width:2px;border-bottom-width:2px;border-top-color:#245885;border-bottom-color:#245885}.et_pb_text_0_tb_footer h1,.et_pb_text_2_tb_footer h1,.et_pb_text_4_tb_footer h1{font-size:56px}.et_pb_text_1_tb_footer,.et_pb_text_3_tb_footer,.et_pb_text_5_tb_footer{border-left-width:2px;border-left-color:#245885}.et_pb_text_4_tb_footer{padding-top:40px!important}.et_pb_image_0_tb_footer{width:50%}.et_pb_image_0_tb_footer .et_pb_image_wrap img{width:auto}}@media only screen and (max-width:767px){.et_pb_section_0_tb_footer{border-top-width:2px;border-bottom-width:2px;border-top-color:#245885;border-bottom-color:#245885}.et_pb_text_0_tb_footer h1,.et_pb_text_2_tb_footer h1,.et_pb_text_4_tb_footer h1{font-size:42px}.et_pb_text_1_tb_footer,.et_pb_text_3_tb_footer,.et_pb_text_5_tb_footer{border-left-width:2px;border-left-color:#245885}.et_pb_text_4_tb_footer{padding-top:40px!important}.et_pb_image_0_tb_footer{width:80%;text-align:center;margin-left:auto;margin-right:auto}.et_pb_image_0_tb_footer .et_pb_image_wrap img{width:auto}}.et_pb_text_1 h1{font-weight:700;font-size:26px}</style>
<link rel="stylesheet" id="et-core-unified-54-cached-inline-styles" href="https://fcmc.org/wp-content/et-cache/54/et-core-unified-54.min.css?ver=1728225605" /><link rel="preload" as="style" id="et-core-unified-tb-124-tb-137-deferred-54-cached-inline-styles" href="https://fcmc.org/wp-content/et-cache/54/et-core-unified-tb-124-tb-137-deferred-54.min.css?ver=1728225605" onload="this.onload=null;this.rel='stylesheet';" /></head>
<body class="page-template-default page page-id-54 et-tb-has-template et-tb-has-header et-tb-has-footer dbdb_divi_2_4_up desktop et_button_no_icon et_pb_button_helper_class et_cover_background et_pb_gutter windows et_pb_gutters3 et_pb_pagebuilder_layout et_no_sidebar et_divi_theme et-db directorist-content-active directorist-preload">
	<div id="page-container">
<div id="et-boc" class="et-boc">
			
		<header class="et-l et-l--header">
			<div class="et_builder_inner_content et_pb_gutters3">
		<div class="et_pb_section et_pb_section_0_tb_header et_section_regular et_pb_section--with-menu" >
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_0_tb_header et_pb_row--with-menu">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_0_tb_header  et_pb_css_mix_blend_mode_passthrough et-last-child et_pb_column--with-menu">
				
				
				
				
				<div class="et_pb_module et_pb_menu et_pb_menu_0_tb_header et_pb_bg_layout_light  et_pb_text_align_right et_dropdown_animation_fade et_pb_menu--with-logo et_pb_menu--style-left_aligned db_title_off db_title_use_link_off db_tagline_off db_tagline_below_title_off db_title_and_tagline_valign_top db_title_and_tagline_below_logo_off">
					
					
					
					
					<div class="et_pb_menu_inner_container clearfix">
						<div class="et_pb_menu__logo-wrap">
			  <div class="et_pb_menu__logo">
				<a href="https://fcmc.org/" ><img fetchpriority="high" decoding="async" width="650" height="267" src="http://fcmc.org/wp-content/uploads/2023/09/main-logo.png" alt="" srcset="https://fcmc.org/wp-content/uploads/2023/09/main-logo.png 650w, https://fcmc.org/wp-content/uploads/2023/09/main-logo-480x197.png 480w" sizes="(min-width: 0px) and (max-width: 480px) 480px, (min-width: 481px) 650px, 100vw" class="wp-image-71" /></a>
			  </div>
			</div>
						<div class="et_pb_menu__wrap">
							<div class="et_pb_menu__menu">
								<nav class="et-menu-nav"><ul id="menu-main-menu" class="et-menu nav"><li class="et_pb_menu_page_id-home menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-97"><a href="https://fcmc.org/">Home</a></li>
<li class="et_pb_menu_page_id-54 menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-54 current_page_item menu-item-58"><a href="https://fcmc.org/services/" aria-current="page">Services</a></li>
<li class="et_pb_menu_page_id-205 menu-item menu-item-type-post_type menu-item-object-page menu-item-208"><a href="https://fcmc.org/find-a-doctor/">Find a Doctor</a></li>
<li class="no-click et_pb_menu_page_id-930 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-930"><a href="#">Locations</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-900 menu-item menu-item-type-post_type menu-item-object-page menu-item-903"><a href="https://fcmc.org/adult-developmental-disabilities-agency/">Adult Developmental Disabilities Agency</a></li>
	<li class="et_pb_menu_page_id-931 menu-item menu-item-type-post_type menu-item-object-page menu-item-933"><a href="https://fcmc.org/child-developmental-disabilities/">Child Developmental Disabilities</a></li>
	<li class="et_pb_menu_page_id-937 menu-item menu-item-type-post_type menu-item-object-page menu-item-939"><a href="https://fcmc.org/franklin-county-medical-center/">Franklin County Medical Center</a></li>
	<li class="et_pb_menu_page_id-943 menu-item menu-item-type-post_type menu-item-object-page menu-item-945"><a href="https://fcmc.org/franklin-county-medical-clinic/">Franklin County Medical Clinic</a></li>
	<li class="et_pb_menu_page_id-950 menu-item menu-item-type-post_type menu-item-object-page menu-item-952"><a href="https://fcmc.org/franklin-county-specialty-clinic/">Franklin County Specialty Clinic</a></li>
	<li class="et_pb_menu_page_id-956 menu-item menu-item-type-post_type menu-item-object-page menu-item-957"><a href="https://fcmc.org/home-health-and-hospice/">Home Health and Hospice</a></li>
	<li class="et_pb_menu_page_id-963 menu-item menu-item-type-post_type menu-item-object-page menu-item-965"><a href="https://fcmc.org/physical-therapy/">Physical Therapy</a></li>
	<li class="et_pb_menu_page_id-971 menu-item menu-item-type-post_type menu-item-object-page menu-item-973"><a href="https://fcmc.org/transitional-care-unit/">Transitional Care Unit</a></li>
</ul>
</li>
<li class="no-click et_pb_menu_page_id-1005 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1005"><a href="#">Resources</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-980 menu-item menu-item-type-post_type menu-item-object-page menu-item-983"><a href="https://fcmc.org/visitor-policy/">Visitor Policy</a></li>
	<li class="et_pb_menu_page_id-989 menu-item menu-item-type-post_type menu-item-object-page menu-item-991"><a href="https://fcmc.org/covid-19-information/">COVID-19 Information</a></li>
	<li class="no-click et_pb_menu_page_id-1017 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1017"><a href="#">Patient Information</a>
	<ul class="sub-menu">
		<li class="et_pb_menu_page_id-1006 menu-item menu-item-type-post_type menu-item-object-page menu-item-1008"><a href="https://fcmc.org/patient-portal/">Patient Portal</a></li>
		<li class="et_pb_menu_page_id-1018 menu-item menu-item-type-post_type menu-item-object-page menu-item-1020"><a href="https://fcmc.org/patient-feedback/">Patient Feedback</a></li>
		<li class="et_pb_menu_page_id-1024 menu-item menu-item-type-post_type menu-item-object-page menu-item-1026"><a href="https://fcmc.org/medical-records/">Medical Records</a></li>
		<li class="et_pb_menu_page_id-1034 menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-1036"><a href="https://fcmc.org/billing-and-payments/">Billing and Payments</a>
		<ul class="sub-menu">
			<li class="et_pb_menu_page_id-1505 menu-item menu-item-type-post_type menu-item-object-page menu-item-1509"><a href="https://fcmc.org/billing-and-payments/financial-services/">Financial Services</a></li>
		</ul>
</li>
		<li class="et_pb_menu_page_id-1042 menu-item menu-item-type-post_type menu-item-object-page menu-item-1044"><a href="https://fcmc.org/rights-and-responsibilities/">Rights and Responsibilities</a></li>
		<li class="et_pb_menu_page_id-1328 menu-item menu-item-type-post_type menu-item-object-page menu-item-1330"><a href="https://fcmc.org/contact-us/">Contact Us</a></li>
	</ul>
</li>
	<li class="et_pb_menu_page_id-1061 menu-item menu-item-type-post_type menu-item-object-page menu-item-1063"><a href="https://fcmc.org/about-us/">About Us</a></li>
	<li class="et_pb_menu_page_id-1080 menu-item menu-item-type-post_type menu-item-object-page menu-item-1083"><a href="https://fcmc.org/apply-for-sponsorship/">Apply For Sponsorship</a></li>
</ul>
</li>
<li class="no-click et_pb_menu_page_id-1086 menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-1086"><a href="#">Careers and Volunteers</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-1087 menu-item menu-item-type-post_type menu-item-object-page menu-item-1089"><a href="https://fcmc.org/volunteers/">Volunteers</a></li>
	<li class="et_pb_menu_page_id-1093 menu-item menu-item-type-post_type menu-item-object-page menu-item-1095"><a href="https://fcmc.org/careers/">Careers</a></li>
</ul>
</li>
<li class="et_pb_menu_page_id-1100 menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-1102"><a href="https://fcmc.org/foundation/">Foundation</a>
<ul class="sub-menu">
	<li class="et_pb_menu_page_id-1108 menu-item menu-item-type-post_type menu-item-object-page menu-item-1265"><a href="https://fcmc.org/foundation/foundation-leadership/">Foundation Leadership</a></li>
</ul>
</li>
</ul></nav>
							</div>
							
							<button type="button" class="et_pb_menu__icon et_pb_menu__search-button"></button>
							<div class="et_mobile_nav_menu">
				<div class="mobile_nav closed">
					<span class="mobile_menu_bar"></span>
				</div>
			</div>
						</div>
						<div class="et_pb_menu__search-container et_pb_menu__search-container--disabled">
				<div class="et_pb_menu__search">
					<form role="search" method="get" class="et_pb_menu__search-form" action="https://fcmc.org/">
						<input type="search" class="et_pb_menu__search-input" placeholder="Search &hellip;" name="s" title="Search for:" />
					</form>
					<button type="button" class="et_pb_menu__icon et_pb_menu__close-search-button"></button>
				</div>
			</div>
					</div>
				</div><style>
.et_pb_menu_0_tb_header .et-menu.nav > li + li > a:before {
    position: absolute;
    left:-11px;
    transform: translateX(-50%);
    content: '|';
    font-size: smaller;
}
</style>
			</div>
				
				
				
				
			</div>
				
				
			</div>		</div>
	</header>
	<div id="et-main-area">
	
<div id="main-content">


			
				<article id="post-54" class="post-54 page type-page status-publish hentry">

				
					<div class="entry-content">
					<div class="et-l et-l--post">
			<div class="et_builder_inner_content et_pb_gutters3">
		<div class="et_pb_section et_pb_section_0 et_pb_with_background et_section_regular" >
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_0">
				<div class="et_pb_column et_pb_column_1_2 et_pb_column_0  et_pb_css_mix_blend_mode_passthrough">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_0  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><h1>Find A Service</h1></div>
			</div><div class="et_pb_module et_pb_sidebar_0 et_pb_widget_area clearfix et_pb_widget_area_left et_pb_bg_layout_light et_pb_sidebar_no_border">
				
				
				
				
				<div id="bcn_widget-3" class="et_pb_widget widget_breadcrumb_navxt"><div class="breadcrumbs" vocab="https://schema.org/" typeof="BreadcrumbList"><!-- Breadcrumb NavXT 7.3.1 -->
<span property="itemListElement" typeof="ListItem"><a property="item" typeof="WebPage" title="Home" href="https://fcmc.org" class="home" ><span property="name">Home</span></a><meta property="position" content="1"></span> &gt; <span property="itemListElement" typeof="ListItem"><a property="item" typeof="WebPage" title="Go to Services." href="https://fcmc.org/services/" class="post post-page current-item" aria-current="page"><span property="name">Services</span></a><meta property="position" content="2"></span></div></div>
			</div>
			</div><div class="et_pb_column et_pb_column_1_2 et_pb_column_1  et_pb_css_mix_blend_mode_passthrough et-last-child et_pb_column_empty">
				
				
				
				
				
			</div>
				
				
				
				
			</div>
				
				
			</div><div class="et_pb_section et_pb_section_1 et_section_regular" >
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_1">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_2  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_1  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><div id="fcmc-services-wrapper">
    <div id="fcmc-services-groups">
        <a href='#fcmc-services-group-A'>A</a>&nbsp;<a href='#fcmc-services-group-B'>B</a>&nbsp;<a href='#fcmc-services-group-C'>C</a>&nbsp;<a href='#fcmc-services-group-D'>D</a>&nbsp;<a href='#fcmc-services-group-E'>E</a>&nbsp;<a href='#fcmc-services-group-F'>F</a>&nbsp;<a href='#fcmc-services-group-G'>G</a>&nbsp;<a href='#fcmc-services-group-H'>H</a>&nbsp;<a href='#fcmc-services-group-I'>I</a>&nbsp;<a href='#fcmc-services-group-K'>K</a>&nbsp;<a href='#fcmc-services-group-L'>L</a>&nbsp;<a href='#fcmc-services-group-M'>M</a>&nbsp;<a href='#fcmc-services-group-O'>O</a>&nbsp;<a href='#fcmc-services-group-P'>P</a>&nbsp;<a href='#fcmc-services-group-R'>R</a>&nbsp;<a href='#fcmc-services-group-S'>S</a>&nbsp;<a href='#fcmc-services-group-U'>U</a>&nbsp;<a href='#fcmc-services-group-V'>V</a>&nbsp;<a href='#fcmc-services-group-W'>W</a>&nbsp;    </div>
    <div id="fcmc-services-filter">
        <input type="text" 
            placeholder="Filter by Keyword"
            data-bind="value: serviceFilter, valueUpdate: 'keyup'"></input>
    </div>
    <div id="fcmc-services-list">
        <ul>
            <div id='fcmc-services-group-A' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>A</span></div>                        <li data-bind="visible: showService('ACL Repair')">
                            <a href="https://fcmc.org/fcmc_service/acl-repair/">ACL Repair</a>
                        </li>
                                            <li data-bind="visible: showService('Arthritis: Osteoarthritis and Rheumatoid')">
                            <a href="https://fcmc.org/fcmc_service/osteoarthritis-rheumatoid-arthritis/">Arthritis: Osteoarthritis and Rheumatoid</a>
                        </li>
                    <div id='fcmc-services-group-B' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>B</span></div>                        <li data-bind="visible: showService('Benign Prostatic Hyperplasia (BPH)')">
                            <a href="https://fcmc.org/fcmc_service/benign-prostatic-hyperplasia/">Benign Prostatic Hyperplasia (BPH)</a>
                        </li>
                                            <li data-bind="visible: showService('Bulkamid')">
                            <a href="https://fcmc.org/fcmc_service/bulkamid/">Bulkamid</a>
                        </li>
                    <div id='fcmc-services-group-C' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>C</span></div>                        <li data-bind="visible: showService('Carpal Tunnel Syndrome')">
                            <a href="https://fcmc.org/fcmc_service/carpal-tunnel-syndrome/">Carpal Tunnel Syndrome</a>
                        </li>
                                            <li data-bind="visible: showService('Colonoscopies')">
                            <a href="https://fcmc.org/fcmc_service/colonoscopies/">Colonoscopies</a>
                        </li>
                    <div id='fcmc-services-group-D' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>D</span></div>                        <li data-bind="visible: showService('Developmental Disability Agency')">
                            <a href="https://fcmc.org/fcmc_service/developmental-disability-agency/">Developmental Disability Agency</a>
                        </li>
                    <div id='fcmc-services-group-E' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>E</span></div>                        <li data-bind="visible: showService('Ear, Nose and Throat (ENT)')">
                            <a href="https://fcmc.org/fcmc_service/ear-nose-and-throat/">Ear, Nose and Throat (ENT)</a>
                        </li>
                                            <li data-bind="visible: showService('ECoin')">
                            <a href="https://fcmc.org/fcmc_service/ecoin/">ECoin</a>
                        </li>
                                            <li data-bind="visible: showService('Elbow Pain')">
                            <a href="https://fcmc.org/fcmc_service/elbow-pain/">Elbow Pain</a>
                        </li>
                                            <li data-bind="visible: showService('Emergency Care')">
                            <a href="https://fcmc.org/fcmc_service/emergency-care/">Emergency Care</a>
                        </li>
                                            <li data-bind="visible: showService('Extended Care and Recovery')">
                            <a href="https://fcmc.org/fcmc_service/extended-care-and-recovery/">Extended Care and Recovery</a>
                        </li>
                    <div id='fcmc-services-group-F' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>F</span></div>                        <li data-bind="visible: showService('Female Incontinence')">
                            <a href="https://fcmc.org/fcmc_service/female-incontinence/">Female Incontinence</a>
                        </li>
                    <div id='fcmc-services-group-G' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>G</span></div>                        <li data-bind="visible: showService('Gastroenterology')">
                            <a href="https://fcmc.org/fcmc_service/gastroenterology/">Gastroenterology</a>
                        </li>
                                            <li data-bind="visible: showService('General Cardiology')">
                            <a href="https://fcmc.org/fcmc_service/general-cardiology/">General Cardiology</a>
                        </li>
                                            <li data-bind="visible: showService('General Surgery')">
                            <a href="https://fcmc.org/fcmc_service/general-surgery/">General Surgery</a>
                        </li>
                    <div id='fcmc-services-group-H' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>H</span></div>                        <li data-bind="visible: showService('Hip Pain')">
                            <a href="https://fcmc.org/fcmc_service/hip-pain/">Hip Pain</a>
                        </li>
                                            <li data-bind="visible: showService('Home Health')">
                            <a href="https://fcmc.org/fcmc_service/home-health/">Home Health</a>
                        </li>
                                            <li data-bind="visible: showService('Hospice')">
                            <a href="https://fcmc.org/fcmc_service/hospice/">Hospice</a>
                        </li>
                    <div id='fcmc-services-group-I' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>I</span></div>                        <li data-bind="visible: showService('Internal Medicine')">
                            <a href="https://fcmc.org/fcmc_service/internal-medicine/">Internal Medicine</a>
                        </li>
                                            <li data-bind="visible: showService('Interpretation Services')">
                            <a href="https://fcmc.org/fcmc_service/interpretation-services/">Interpretation Services</a>
                        </li>
                    <div id='fcmc-services-group-K' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>K</span></div>                        <li data-bind="visible: showService('Kidney Stones')">
                            <a href="https://fcmc.org/fcmc_service/kidney-stones/">Kidney Stones</a>
                        </li>
                                            <li data-bind="visible: showService('Knee Pain')">
                            <a href="https://fcmc.org/fcmc_service/knee-pain/">Knee Pain</a>
                        </li>
                    <div id='fcmc-services-group-L' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>L</span></div>                        <li data-bind="visible: showService('Laboratory')">
                            <a href="https://fcmc.org/fcmc_service/laboratory/">Laboratory</a>
                        </li>
                    <div id='fcmc-services-group-M' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>M</span></div>                        <li data-bind="visible: showService('Mammograms')">
                            <a href="https://fcmc.org/fcmc_service/mammograms/">Mammograms</a>
                        </li>
                                            <li data-bind="visible: showService('Meniscus Tear')">
                            <a href="https://fcmc.org/fcmc_service/meniscus-tear/">Meniscus Tear</a>
                        </li>
                                            <li data-bind="visible: showService('Mental Health')">
                            <a href="https://fcmc.org/fcmc_service/mental-health/">Mental Health</a>
                        </li>
                                            <li data-bind="visible: showService('MRI')">
                            <a href="https://fcmc.org/fcmc_service/mri/">MRI</a>
                        </li>
                    <div id='fcmc-services-group-O' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>O</span></div>                        <li data-bind="visible: showService('Obstetrics')">
                            <a href="https://fcmc.org/fcmc_service/obstetrics/">Obstetrics</a>
                        </li>
                                            <li data-bind="visible: showService('Occupational Therapy')">
                            <a href="https://fcmc.org/fcmc_service/occupational-therapy/">Occupational Therapy</a>
                        </li>
                                            <li data-bind="visible: showService('Orthopedics')">
                            <a href="https://fcmc.org/fcmc_service/orthopedics/">Orthopedics</a>
                        </li>
                    <div id='fcmc-services-group-P' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>P</span></div>                        <li data-bind="visible: showService('Pediatrics')">
                            <a href="https://fcmc.org/fcmc_service/pediatrics/">Pediatrics</a>
                        </li>
                                            <li data-bind="visible: showService('Physical Therapy')">
                            <a href="https://fcmc.org/fcmc_service/physical-therapy/">Physical Therapy</a>
                        </li>
                                            <li data-bind="visible: showService('Podiatry')">
                            <a href="https://fcmc.org/fcmc_service/podiatry/">Podiatry</a>
                        </li>
                                            <li data-bind="visible: showService('Primary Care')">
                            <a href="https://fcmc.org/fcmc_service/primary-care/">Primary Care</a>
                        </li>
                    <div id='fcmc-services-group-R' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>R</span></div>                        <li data-bind="visible: showService('Radiology')">
                            <a href="https://fcmc.org/fcmc_service/radiology/">Radiology</a>
                        </li>
                                            <li data-bind="visible: showService('Respiratory Therapy')">
                            <a href="https://fcmc.org/fcmc_service/respiratory-therapy/">Respiratory Therapy</a>
                        </li>
                    <div id='fcmc-services-group-S' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>S</span></div>                        <li data-bind="visible: showService('Shoulder Pain')">
                            <a href="https://fcmc.org/fcmc_service/shoulder-pain/">Shoulder Pain</a>
                        </li>
                                            <li data-bind="visible: showService('Skilled Nursing')">
                            <a href="https://fcmc.org/fcmc_service/skilled-nursing/">Skilled Nursing</a>
                        </li>
                                            <li data-bind="visible: showService('Sleep Medicine')">
                            <a href="https://fcmc.org/fcmc_service/sleep-medicine/">Sleep Medicine</a>
                        </li>
                                            <li data-bind="visible: showService('Speech Therapy')">
                            <a href="https://fcmc.org/fcmc_service/speech-therapy/">Speech Therapy</a>
                        </li>
                                            <li data-bind="visible: showService('Sports Medicine')">
                            <a href="https://fcmc.org/fcmc_service/sports-medicine/">Sports Medicine</a>
                        </li>
                    <div id='fcmc-services-group-U' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>U</span></div>                        <li data-bind="visible: showService('Upper Gastrointestinal Endoscopy')">
                            <a href="https://fcmc.org/fcmc_service/upper-gastrointestinal-endoscopy/">Upper Gastrointestinal Endoscopy</a>
                        </li>
                                            <li data-bind="visible: showService('Urology')">
                            <a href="https://fcmc.org/fcmc_service/urology/">Urology</a>
                        </li>
                    <div id='fcmc-services-group-V' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>V</span></div>                        <li data-bind="visible: showService('Vaccinations')">
                            <a href="https://fcmc.org/fcmc_service/vaccinations/">Vaccinations</a>
                        </li>
                                            <li data-bind="visible: showService('Vasectomy')">
                            <a href="https://fcmc.org/fcmc_service/vasectomy/">Vasectomy</a>
                        </li>
                    <div id='fcmc-services-group-W' class='fcmc-services-group' data-bind='visible: showGroups'><hr /><span>W</span></div>                        <li data-bind="visible: showService('Wellness Checks')">
                            <a href="https://fcmc.org/fcmc_service/wellness/">Wellness Checks</a>
                        </li>
                                            <li data-bind="visible: showService('Women’s Health')">
                            <a href="https://fcmc.org/fcmc_service/womens-health/">Women’s Health</a>
                        </li>
                                            <li data-bind="visible: showService('Wrist Pain')">
                            <a href="https://fcmc.org/fcmc_service/wrist-pain/">Wrist Pain</a>
                        </li>
                            </ul>
    </div>
</div></div>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div>		</div>
	</div>
						</div>

				
				</article>

			

</div>

	<footer class="et-l et-l--footer">
			<div class="et_builder_inner_content et_pb_gutters3">
		<div id="footer" class="et_pb_with_border et_pb_section et_pb_section_0_tb_footer et_pb_with_background et_section_regular et_pb_section--with-menu" >
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_0_tb_footer et_pb_row--with-menu">
				<div class="et_pb_column et_pb_column_2_3 et_pb_column_0_tb_footer  et_pb_css_mix_blend_mode_passthrough">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_0_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><h6>ABOUT FCMC</h6></div>
			</div><div class="et_pb_with_border et_pb_module et_pb_text et_pb_text_1_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p style="text-align: left;"><span>Franklin County Medical Center (FCMC) is your local hub for rural and critical healthcare access for Southeastern Idaho, since 1929. Located in the heart of Preston, Idaho, FCMC has seven departments to provide quality healthcare at any stage of life, for your expected and unexpected healthcare needs. FCMC provides a range of services and specialties including community health and specialty clinics, inpatient and outpatient services, labor and delivery, surgery, home care programs, rehabilitation, skilled nursing care, urgent care, emergency services, and more.</span></p>
<p style="text-align: left;"><a href="http://fcmc.org/about-us">READ MORE ABOUT US</a></p></div>
			</div><div class="et_pb_module et_pb_text et_pb_text_2_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><h6>NON DISCRIMINATION<br />
</h6></div>
			</div><div class="et_pb_with_border et_pb_module et_pb_text et_pb_text_3_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p style="text-align: left;"><span>Franklin County Medical Center (FCMC) complies with applicable Federal civil rights laws and does not discriminate on the basis of race, color, national origin, age, disability, or sex. FCMC does not exclude people or treat them differently because of race, color, national origin, age, disability, or sex.</span></p>
<p style="text-align: left;"><a href="https://docs.google.com/document/d/1N5Ife8vzlfftt8MqXbR7MPn5Soo7OrOSOjmkVMlRn7I/edit?usp=sharing">VIEW &amp; DOWNLOAD OUR NON-DISCRIMINATION POLICY HERE</a></p></div>
			</div>
			</div><div class="et_pb_column et_pb_column_1_3 et_pb_column_1_tb_footer  et_pb_css_mix_blend_mode_passthrough et-last-child et_pb_column--with-menu">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_4_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><h6>Helpful Links</h6></div>
			</div><div class="et_pb_with_border et_pb_module et_pb_text et_pb_text_5_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner"><p style="text-align: left;"><a href="/billing-and-payments/">Billing &amp; Payments</a><br /><a href="/medical-records/">Medical Records</a><br /><a href="/careers/">Careers</a><br /><a href="/contact-us">Contact Us</a><br /><a href="/category/news/">News</a><br /><a href="https://www.hospitalpricelists.org/Franklin-County-Medical-Center">Price Transparency</a></p></div>
			</div><div class="et_pb_module et_pb_image et_pb_image_0_tb_footer">
				
				
				
				
				<span class="et_pb_image_wrap "><img loading="lazy" decoding="async" width="650" height="267" src="http://fcmc.org/wp-content/uploads/2023/09/main-logo.png" alt="" title="main-logo" srcset="https://fcmc.org/wp-content/uploads/2023/09/main-logo.png 650w, https://fcmc.org/wp-content/uploads/2023/09/main-logo-480x197.png 480w" sizes="(min-width: 0px) and (max-width: 480px) 480px, (min-width: 481px) 650px, 100vw" class="wp-image-71" /></span>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div><div class="et_pb_section et_pb_section_1_tb_footer et_section_regular" >
				
				
				
				
				
				
				<div class="et_pb_row et_pb_row_1_tb_footer">
				<div class="et_pb_column et_pb_column_4_4 et_pb_column_2_tb_footer  et_pb_css_mix_blend_mode_passthrough et-last-child">
				
				
				
				
				<div class="et_pb_module et_pb_text et_pb_text_6_tb_footer  et_pb_text_align_left et_pb_bg_layout_light">
				
				
				
				
				<div class="et_pb_text_inner">© 2024 Franklin County Medical Center. All rights reserved. Website by <a href="https://arvigmedia.com/" target="_blank" rel="noopener">Arvig Media</a>.</div>
			</div>
			</div>
				
				
				
				
			</div>
				
				
			</div>		</div>
	</footer>
		</div>

			
		</div>
		</div>

			    <script>
        jQuery(document).ready(function($) {
            $('.et_pb_slider.dbdb_slider_random').each(function() {
                var $slider = $(this);
                var $slidesContainer = $slider.find('.et_pb_slides');

                // Randomize the slides
                var $slides = $slidesContainer.children().sort(function() {
                    return Math.random() - 0.5;
                }).detach().appendTo($slidesContainer);

                // Remove the active class from existing slide
                $slides.removeClass('et-pb-active-slide');

                // Restore visibility to the slides
                $slides.css('visibility', 'visible');


                // Add the active class to the first slide
                $slides.first().addClass('et-pb-active-slide');
            });
        });
    </script>
<style>
.et_pb_newsletter .et_pb_newsletter_button.et_pb_button[data-db-button-animation="rocking"] {
    animation: dbRockingEffect 2s linear infinite;
    transition: transform 0.3s ease-in-out;
}
.et_pb_newsletter .et_pb_newsletter_button.et_pb_button[data-db-button-animation="rocking"]:hover {
    animation: none;
    transform: rotate(0deg);
}
@keyframes dbRockingEffect {
    0%, 60%, 100% { transform: rotate(0deg); }
    15% { transform: rotate(1.5deg); }
    45% { transform: rotate(-1.5deg); }
}
</style>
    <script>
        jQuery(function($) {

            // Trigger counter refresh on first load
            $('.dbdb-gallery-with-image-count').each(function() {
                triggerSlideChanged($(this));
            });

            // Trigger counter refresh when the slide changes (due to arrow button clicked)
            $(document).on('mouseup', '.dbdb-gallery-with-image-count .et-pb-slider-arrows a, .dbdb-gallery-with-image-count .et-pb-controllers a', function() {
                var $gallery = $(this).closest('.dbdb-gallery-with-image-count');
                triggerSlideChanged($gallery);
            });

            function triggerSlideChanged($gallery) {
                $gallery.trigger('divi-booster:gallery-slide-changed');
            }

            // Update the counter when the slide has changed
            $(document).on('divi-booster:gallery-slide-changed', '.dbdb-gallery-with-image-count', function() {
                var $gallery = $(this);
                setTimeout(function() {
                    var currentIndex = $gallery.find('.et-pb-active-slide').index() + 1;
                    $gallery.find('.dbdb-slide-counter-active').text(currentIndex);
                }, 50);
            });

            // Set separator on lightbox count
            setTimeout(
                function() {
                    $('.et_pb_gallery_items').each(function() {
                        if ($(this).data('magnificPopup') && $(this).data('dbdb-image-count-separator')) {
                            $(this).data('magnificPopup').gallery.tCounter = '%curr%' + $(this).data('dbdb-image-count-separator') + '%total%';
                        }
                    });
                },
                0
            );
        });
    </script>
    <style>
        .dbdb-gallery-with-image-count .dbdb-slide-counter {
            position: absolute;
            width: 100%;
        }

        .dbdb-gallery-with-image-count {
            overflow: visible !important;
        }

        .dbdb-gallery-with-image-count .et_pb_gallery_items {
            overflow: hidden;
        }

        /* Fix divi gallery layout change on first slide change bug (as this causes the counter to jump too) */
        .dbdb-gallery-with-image-count .et_pb_gallery_item.et_slide_transition {
            display: block !important;
        }
    </style>
    <script>
        jQuery(document).ready(function($) {
            $(document).on('click', '.et_pb_gallery .et_pb_gallery_image a', function() {

                // Remove the old class
                $('body').removeClass(function(index, className) {
                    return (className.match(/(^|\s)et_pb_gallery_\d+_dbdb_lightbox_open/g) || []).join(' ');
                });

                // Add the new class
                var gallery_module_order = $(this).closest('.et_pb_gallery').attr('class').match(/et_pb_gallery_\d+/)[0];
                $('body').addClass(gallery_module_order + '_dbdb_lightbox_open');
            });
        });
    </script>

            <script data-name="dbdb-update-custom-icons">
                jQuery(function($) {

                                            setTimeout(
                            function() {
                                update_all_icons();
                            }, 100
                        );
                                        $(document).on('db_vb_custom_icons_updated', function() {
                        update_all_icons();
                    });

                    // Handle hover over modules with hover state
                    $(document).on('mouseenter mouseleave', '.et_multi_view__hover_selector', function() {
                        update_all_icons();
                    });

                    // Handle hover module redraw when leaving main area
                    $(document).on('mouseleave', '#et-main-area', function() {
                        setTimeout(
                            function() {
                                update_all_icons();
                            }, 0
                        );
                    });


                    function update_all_icons() {

                        // Add Extended Icon class to buttons with custom icons
                        $('.et_pb_button[data-icon="\u0800"]').addClass('db-custom-extended-icon');

                        $('.dbdb-icon-on-left.dbdb-icon-on-hover-off .db-custom-extended-icon').each(function() {
                            add_padding_to_icon(this, 'left', false);
                        });
                        $('.dbdb-icon-on-left.dbdb-icon-on-hover .db-custom-extended-icon:hover').each(function() {
                            add_padding_to_icon(this, 'left', true);
                        });
                        $('.dbdb-icon-on-right.dbdb-icon-on-hover-off .db-custom-extended-icon').each(function() {
                            add_padding_to_icon(this, 'right', false);
                        });
                        $('.dbdb-icon-on-right.dbdb-icon-on-hover .db-custom-extended-icon:hover').each(function() {
                            add_padding_to_icon(this, 'right', true);
                        });

                        db014_update_icon("wtfdivi014-url0", "http:\/\/fcmc.org\/wp-content\/uploads\/2023\/09\/AdobeStock_151266003_Preview-doctor.png");
                        db014_update_icon("\u0800", "http:\/\/fcmc.org\/wp-content\/uploads\/2023\/09\/AdobeStock_151266003_Preview-doctor.png");
                    }

                    function add_padding_to_icon(button, side = 'left', hoverOnly = false) {
                        var $button = $(button);
                        var icon = window.getComputedStyle($button[0], (side === 'left') ? '::before' : '::after');
                        if (typeof window.Image === 'function') {
                            var img = new Image();
                            img.src = icon.getPropertyValue('background-image').replace(/^url\(['"]?/, '').replace(/['"]?\)$/, '');;
                            img.onload = function() {
                                var $button = $(button);
                                set_padding_css($button, icon_padding(this), side);
                                if (hoverOnly) {
                                    $button.hover(
                                        function() {
                                            set_padding_css($button, icon_padding(this), side);
                                        },
                                        function() {
                                            setTimeout(function() {
                                                set_padding_css($button, '1em', side);
                                            }, 100);
                                        }
                                    );
                                }
                            }
                        }
                    }

                    function icon_padding(icon) {
                        var icon_standard_padding_in_em = 1.3;
                        var icon_rendered_height_in_em = 1;
                        return icon_standard_padding_in_em + (icon.width / icon.height) * icon_rendered_height_in_em + 'em';
                    }

                    function set_padding_css($button, padding, side = 'left') {
                        $button.css('padding-' + side, padding);
                    }
                });
            </script>
            <script data-name="dbdb-update-custom-icons">
                jQuery(function($) {

                                            setTimeout(
                            function() {
                                update_all_icons();
                            }, 100
                        );
                                        $(document).on('db_vb_custom_icons_updated', function() {
                        update_all_icons();
                    });

                    // Handle hover over modules with hover state
                    $(document).on('mouseenter mouseleave', '.et_multi_view__hover_selector', function() {
                        update_all_icons();
                    });

                    // Handle hover module redraw when leaving main area
                    $(document).on('mouseleave', '#et-main-area', function() {
                        setTimeout(
                            function() {
                                update_all_icons();
                            }, 0
                        );
                    });


                    function update_all_icons() {

                        // Add Extended Icon class to buttons with custom icons
                        $('.et_pb_button[data-icon="\u0801"]').addClass('db-custom-extended-icon');

                        $('.dbdb-icon-on-left.dbdb-icon-on-hover-off .db-custom-extended-icon').each(function() {
                            add_padding_to_icon(this, 'left', false);
                        });
                        $('.dbdb-icon-on-left.dbdb-icon-on-hover .db-custom-extended-icon:hover').each(function() {
                            add_padding_to_icon(this, 'left', true);
                        });
                        $('.dbdb-icon-on-right.dbdb-icon-on-hover-off .db-custom-extended-icon').each(function() {
                            add_padding_to_icon(this, 'right', false);
                        });
                        $('.dbdb-icon-on-right.dbdb-icon-on-hover .db-custom-extended-icon:hover').each(function() {
                            add_padding_to_icon(this, 'right', true);
                        });

                        db014_update_icon("wtfdivi014-url1", "http:\/\/fcmc.org\/wp-content\/uploads\/2023\/09\/AdobeStock_151266003_Preview-cross150.png");
                        db014_update_icon("\u0801", "http:\/\/fcmc.org\/wp-content\/uploads\/2023\/09\/AdobeStock_151266003_Preview-cross150.png");
                    }

                    function add_padding_to_icon(button, side = 'left', hoverOnly = false) {
                        var $button = $(button);
                        var icon = window.getComputedStyle($button[0], (side === 'left') ? '::before' : '::after');
                        if (typeof window.Image === 'function') {
                            var img = new Image();
                            img.src = icon.getPropertyValue('background-image').replace(/^url\(['"]?/, '').replace(/['"]?\)$/, '');;
                            img.onload = function() {
                                var $button = $(button);
                                set_padding_css($button, icon_padding(this), side);
                                if (hoverOnly) {
                                    $button.hover(
                                        function() {
                                            set_padding_css($button, icon_padding(this), side);
                                        },
                                        function() {
                                            setTimeout(function() {
                                                set_padding_css($button, '1em', side);
                                            }, 100);
                                        }
                                    );
                                }
                            }
                        }
                    }

                    function icon_padding(icon) {
                        var icon_standard_padding_in_em = 1.3;
                        var icon_rendered_height_in_em = 1;
                        return icon_standard_padding_in_em + (icon.width / icon.height) * icon_rendered_height_in_em + 'em';
                    }

                    function set_padding_css($button, padding, side = 'left') {
                        $button.css('padding-' + side, padding);
                    }
                });
            </script>
            <script data-name="dbdb-update-custom-icons">
                jQuery(function($) {

                                            setTimeout(
                            function() {
                                update_all_icons();
                            }, 100
                        );
                                        $(document).on('db_vb_custom_icons_updated', function() {
                        update_all_icons();
                    });

                    // Handle hover over modules with hover state
                    $(document).on('mouseenter mouseleave', '.et_multi_view__hover_selector', function() {
                        update_all_icons();
                    });

                    // Handle hover module redraw when leaving main area
                    $(document).on('mouseleave', '#et-main-area', function() {
                        setTimeout(
                            function() {
                                update_all_icons();
                            }, 0
                        );
                    });


                    function update_all_icons() {

                        // Add Extended Icon class to buttons with custom icons
                        $('.et_pb_button[data-icon="\u0802"]').addClass('db-custom-extended-icon');

                        $('.dbdb-icon-on-left.dbdb-icon-on-hover-off .db-custom-extended-icon').each(function() {
                            add_padding_to_icon(this, 'left', false);
                        });
                        $('.dbdb-icon-on-left.dbdb-icon-on-hover .db-custom-extended-icon:hover').each(function() {
                            add_padding_to_icon(this, 'left', true);
                        });
                        $('.dbdb-icon-on-right.dbdb-icon-on-hover-off .db-custom-extended-icon').each(function() {
                            add_padding_to_icon(this, 'right', false);
                        });
                        $('.dbdb-icon-on-right.dbdb-icon-on-hover .db-custom-extended-icon:hover').each(function() {
                            add_padding_to_icon(this, 'right', true);
                        });

                        db014_update_icon("wtfdivi014-url2", "http:\/\/fcmc.org\/wp-content\/uploads\/2024\/02\/medical-icon.png");
                        db014_update_icon("\u0802", "http:\/\/fcmc.org\/wp-content\/uploads\/2024\/02\/medical-icon.png");
                    }

                    function add_padding_to_icon(button, side = 'left', hoverOnly = false) {
                        var $button = $(button);
                        var icon = window.getComputedStyle($button[0], (side === 'left') ? '::before' : '::after');
                        if (typeof window.Image === 'function') {
                            var img = new Image();
                            img.src = icon.getPropertyValue('background-image').replace(/^url\(['"]?/, '').replace(/['"]?\)$/, '');;
                            img.onload = function() {
                                var $button = $(button);
                                set_padding_css($button, icon_padding(this), side);
                                if (hoverOnly) {
                                    $button.hover(
                                        function() {
                                            set_padding_css($button, icon_padding(this), side);
                                        },
                                        function() {
                                            setTimeout(function() {
                                                set_padding_css($button, '1em', side);
                                            }, 100);
                                        }
                                    );
                                }
                            }
                        }
                    }

                    function icon_padding(icon) {
                        var icon_standard_padding_in_em = 1.3;
                        var icon_rendered_height_in_em = 1;
                        return icon_standard_padding_in_em + (icon.width / icon.height) * icon_rendered_height_in_em + 'em';
                    }

                    function set_padding_css($button, padding, side = 'left') {
                        $button.css('padding-' + side, padding);
                    }
                });
            </script>
            <script data-name="dbdb-update-custom-icons">
                jQuery(function($) {

                                            setTimeout(
                            function() {
                                update_all_icons();
                            }, 100
                        );
                                        $(document).on('db_vb_custom_icons_updated', function() {
                        update_all_icons();
                    });

                    // Handle hover over modules with hover state
                    $(document).on('mouseenter mouseleave', '.et_multi_view__hover_selector', function() {
                        update_all_icons();
                    });

                    // Handle hover module redraw when leaving main area
                    $(document).on('mouseleave', '#et-main-area', function() {
                        setTimeout(
                            function() {
                                update_all_icons();
                            }, 0
                        );
                    });


                    function update_all_icons() {

                        // Add Extended Icon class to buttons with custom icons
                        $('.et_pb_button[data-icon="\u0803"]').addClass('db-custom-extended-icon');

                        $('.dbdb-icon-on-left.dbdb-icon-on-hover-off .db-custom-extended-icon').each(function() {
                            add_padding_to_icon(this, 'left', false);
                        });
                        $('.dbdb-icon-on-left.dbdb-icon-on-hover .db-custom-extended-icon:hover').each(function() {
                            add_padding_to_icon(this, 'left', true);
                        });
                        $('.dbdb-icon-on-right.dbdb-icon-on-hover-off .db-custom-extended-icon').each(function() {
                            add_padding_to_icon(this, 'right', false);
                        });
                        $('.dbdb-icon-on-right.dbdb-icon-on-hover .db-custom-extended-icon:hover').each(function() {
                            add_padding_to_icon(this, 'right', true);
                        });

                        db014_update_icon("wtfdivi014-url3", "http:\/\/fcmc.org\/wp-content\/uploads\/2024\/02\/doctor-icon.png");
                        db014_update_icon("\u0803", "http:\/\/fcmc.org\/wp-content\/uploads\/2024\/02\/doctor-icon.png");
                    }

                    function add_padding_to_icon(button, side = 'left', hoverOnly = false) {
                        var $button = $(button);
                        var icon = window.getComputedStyle($button[0], (side === 'left') ? '::before' : '::after');
                        if (typeof window.Image === 'function') {
                            var img = new Image();
                            img.src = icon.getPropertyValue('background-image').replace(/^url\(['"]?/, '').replace(/['"]?\)$/, '');;
                            img.onload = function() {
                                var $button = $(button);
                                set_padding_css($button, icon_padding(this), side);
                                if (hoverOnly) {
                                    $button.hover(
                                        function() {
                                            set_padding_css($button, icon_padding(this), side);
                                        },
                                        function() {
                                            setTimeout(function() {
                                                set_padding_css($button, '1em', side);
                                            }, 100);
                                        }
                                    );
                                }
                            }
                        }
                    }

                    function icon_padding(icon) {
                        var icon_standard_padding_in_em = 1.3;
                        var icon_rendered_height_in_em = 1;
                        return icon_standard_padding_in_em + (icon.width / icon.height) * icon_rendered_height_in_em + 'em';
                    }

                    function set_padding_css($button, padding, side = 'left') {
                        $button.css('padding-' + side, padding);
                    }
                });
            </script>
    <style>
        .et-fb-no-vb-support-warning {
            display: none !important;
        }
    </style>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PR6GQ39" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) --><script type="text/javascript" id="jquery-core-js-extra">
/* <![CDATA[ */
var directorist = {"nonce":"3438171991","directorist_nonce":"ec3c2fbb3a","ajax_nonce":"bfcb5f1b60","is_admin":"","ajaxurl":"https:\/\/fcmc.org\/wp-admin\/admin-ajax.php","assets_url":"https:\/\/fcmc.org\/wp-content\/plugins\/directorist\/assets\/","home_url":"https:\/\/fcmc.org","rest_url":"https:\/\/fcmc.org\/wp-json\/","nonceName":"atbdp_nonce_js","login_alert_message":"Sorry, you need to login first.","rtl":"false","warning":"WARNING!","success":"SUCCESS!","not_add_more_than_one":"You can not add more than one review. Refresh the page to edit or delete your review!,","duplicate_review_error":"Sorry! your review already in process.","review_success":"Reviews Saved Successfully!","review_approval_text":"Your review has been received. It requires admin approval to publish.","review_error":"Something went wrong. Check the form and try again!!!","review_loaded":"Reviews Loaded!","review_not_available":"NO MORE REVIEWS AVAILABLE!,","review_have_not_for_delete":"You do not have any review to delete. Refresh the page to submit new review!!!,","review_sure_msg":"Are you sure?","review_want_to_remove":"Do you really want to remove this review!","review_delete_msg":"Yes, Delete it!","review_cancel_btn_text":"Cancel","review_wrong_msg":"Something went wrong!, Try again","listing_remove_title":"Are you sure?","listing_remove_text":"Do you really want to delete this item?!","listing_remove_confirm_text":"Yes, Delete it!","listing_delete":"Deleted!!","listing_error_title":"ERROR!!","listing_error_text":"Something went wrong!!!, Try again","upload_pro_pic_title":"Select or Upload a profile picture","upload_pro_pic_text":"Use this Image","payNow":"Pay Now","completeSubmission":"Complete Submission","waiting_msg":"Sending the message, please wait...","plugin_url":"https:\/\/fcmc.org\/wp-content\/plugins\/directorist\/","currentDate":"September 11, 2023","enable_reviewer_content":"1","add_listing_data":{"nonce":"3438171991","ajaxurl":"https:\/\/fcmc.org\/wp-admin\/admin-ajax.php","nonceName":"atbdp_nonce_js","is_admin":false,"media_uploader":[{"element_id":"directorist-image-upload","meta_name":"listing_img","files_meta_name":"files_meta","error_msg":"Listing gallery has invalid files"}],"i18n_text":{"see_more_text":"See More","see_less_text":"See Less","confirmation_text":"Are you sure","ask_conf_sl_lnk_del_txt":"Do you really want to remove this Social Link!","ask_conf_faqs_del_txt":"Do you really want to remove this FAQ!","confirm_delete":"Yes, Delete it!","deleted":"Deleted!","max_location_creation":"","max_location_msg":"You can only use ","submission_wait_msg":"Please wait, your submission is being processed.","image_uploading_msg":"Please wait, your selected images being uploaded."},"create_new_tag":"","create_new_loc":"","create_new_cat":"","image_notice":"Sorry! You have crossed the maximum image limit"},"lazy_load_taxonomy_fields":"","current_page_id":"54","icon_markup":"<i class=\"directorist-icon-mask ##CLASS##\" aria-hidden=\"true\" style=\"--directorist-icon: url(##URL##)\"><\/i>","script_debugging":"1","ajax_url":"https:\/\/fcmc.org\/wp-admin\/admin-ajax.php","redirect_url":"https:\/\/fcmc.org\/","loading_message":"Sending user info, please wait...","login_error_message":"Wrong username or password.","i18n_text":{"category_selection":"Select a category","location_selection":"Select a location","show_more":"Show More","show_less":"Show Less","added_favourite":"Added to favorite","please_login":"Please login first","select_listing_map":"openstreet","Miles":" Miles"},"args":{"directory_type_id":"","search_max_radius_distance":1000},"directory_type":"","directory_type_term_data":{"submission_form_fields":false,"search_form_fields":false},"miles":" Miles","default_val":"0","countryRestriction":"","restricted_countries":"","use_def_lat_long":"","ajaxnonce":"bfcb5f1b60"};
/* ]]> */
</script>
<script type="text/javascript" src="https://fcmc.org/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>
<script type="text/javascript" src="https://fcmc.org/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" id="jquery-migrate-js"></script>
<script type="text/javascript" id="jquery-js-after">
/* <![CDATA[ */
jqueryParams.length&&$.each(jqueryParams,function(e,r){if("function"==typeof r){var n=String(r);n.replace("$","jQuery");var a=new Function("return "+n)();$(document).ready(a)}});
/* ]]> */
</script>
<script type="text/javascript" id="divi-custom-script-js-extra">
/* <![CDATA[ */
var DIVI = {"item_count":"%d Item","items_count":"%d Items"};
var et_builder_utils_params = {"condition":{"diviTheme":true,"extraTheme":false},"scrollLocations":["app","top"],"builderScrollLocations":{"desktop":"app","tablet":"app","phone":"app"},"onloadScrollLocation":"app","builderType":"fe"};
var et_frontend_scripts = {"builderCssContainerPrefix":"#et-boc","builderCssLayoutPrefix":"#et-boc .et-l"};
var et_pb_custom = {"ajaxurl":"https:\/\/fcmc.org\/wp-admin\/admin-ajax.php","images_uri":"https:\/\/fcmc.org\/wp-content\/themes\/Divi\/images","builder_images_uri":"https:\/\/fcmc.org\/wp-content\/themes\/Divi\/includes\/builder\/images","et_frontend_nonce":"57e20c9734","subscription_failed":"Please, check the fields below to make sure you entered the correct information.","et_ab_log_nonce":"49d582b1be","fill_message":"Please, fill in the following fields:","contact_error_message":"Please, fix the following errors:","invalid":"Invalid email","captcha":"Captcha","prev":"Prev","previous":"Previous","next":"Next","wrong_captcha":"You entered the wrong number in captcha.","wrong_checkbox":"Checkbox","ignore_waypoints":"no","is_divi_theme_used":"1","widget_search_selector":".widget_search","ab_tests":[],"is_ab_testing_active":"","page_id":"54","unique_test_id":"","ab_bounce_rate":"5","is_cache_plugin_active":"yes","is_shortcode_tracking":"","tinymce_uri":"https:\/\/fcmc.org\/wp-content\/themes\/Divi\/includes\/builder\/frontend-builder\/assets\/vendors","accent_color":"#245885","waypoints_options":[]};
var et_pb_box_shadow_elements = [];
/* ]]> */
</script>
<script type="text/javascript" src="https://fcmc.org/wp-content/themes/Divi/js/scripts.min.js?ver=4.25.1" id="divi-custom-script-js"></script>
<script type="text/javascript" src="https://fcmc.org/wp-content/themes/Divi/core/admin/js/common.js?ver=4.25.1" id="et-core-common-js"></script>
<script type="text/javascript" src="https://fcmc.org/wp-content/plugins/fcmc-services/assets/js/knockout.min.js?ver=6.6.2" id="fcmc-knockout-js"></script>
<script type="text/javascript" src="https://fcmc.org/wp-content/plugins/fcmc-services/assets/js/main.js?ver=6.6.2" id="fcmc-main-js"></script>
	
	</body>
</html>
"""
    r = translator.web_trans(source)
    print(r)
