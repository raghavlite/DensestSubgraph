DensestSubgraph
===============


Densest Subgraph problem on Undirected graphs implemented using the 

Graph Tool python module
http://graph-tool.skewed.de/

The Working_part.ipynb is the implemented code 


Refer to the file for more info

:Working_part.ipynb is a ipython notebook file


The Working_part.py is the script version of this implementaion 




<!DOCTYPE html>
<html>
<head>

<meta charset="utf-8" />
<title>Notebook</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    .clearfix{*zoom:1}.clearfix:before,.clearfix:after{display:table;content:"";line-height:0}
.clearfix:after{clear:both}
.hide-text{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}
.input-block-level{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}
article,aside,details,figcaption,figure,footer,header,hgroup,nav,section{display:block}
audio,canvas,video{display:inline-block;*display:inline;*zoom:1}
audio:not([controls]){display:none}
html{font-size:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}
a:focus{outline:thin dotted #333;outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}
a:hover,a:active{outline:0}
sub,sup{position:relative;font-size:75%;line-height:0;vertical-align:baseline}
sup{top:-0.5em}
sub{bottom:-0.25em}
img{max-width:100%;width:auto\9;height:auto;vertical-align:middle;border:0;-ms-interpolation-mode:bicubic}
#map_canvas img,.google-maps img{max-width:none}
button,input,select,textarea{margin:0;font-size:100%;vertical-align:middle}
button,input{*overflow:visible;line-height:normal}
button::-moz-focus-inner,input::-moz-focus-inner{padding:0;border:0}
button,html input[type="button"],input[type="reset"],input[type="submit"]{-webkit-appearance:button;cursor:pointer}
label,select,button,input[type="button"],input[type="reset"],input[type="submit"],input[type="radio"],input[type="checkbox"]{cursor:pointer}
input[type="search"]{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;-webkit-appearance:textfield}
input[type="search"]::-webkit-search-decoration,input[type="search"]::-webkit-search-cancel-button{-webkit-appearance:none}
textarea{overflow:auto;vertical-align:top}
@media print{*{text-shadow:none !important;color:#000 !important;background:transparent !important;box-shadow:none !important} a,a:visited{text-decoration:underline} a[href]:after{content:" (" attr(href) ")"} abbr[title]:after{content:" (" attr(title) ")"} .ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""} pre,blockquote{border:1px solid #999;page-break-inside:avoid} thead{display:table-header-group} tr,img{page-break-inside:avoid} img{max-width:100% !important} @page {margin:.5cm}p,h2,h3{orphans:3;widows:3} h2,h3{page-break-after:avoid}}body{margin:0;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;line-height:20px;color:#000;background-color:#fff}
a{color:#08c;text-decoration:none}
a:hover,a:focus{color:#005580;text-decoration:underline}
.img-rounded{border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.img-polaroid{padding:4px;background-color:#fff;border:1px solid #ccc;border:1px solid rgba(0,0,0,0.2);-webkit-box-shadow:0 1px 3px rgba(0,0,0,0.1);-moz-box-shadow:0 1px 3px rgba(0,0,0,0.1);box-shadow:0 1px 3px rgba(0,0,0,0.1)}
.img-circle{border-radius:500px;-webkit-border-radius:500px;-moz-border-radius:500px;border-radius:500px}
.row{margin-left:-20px;*zoom:1}.row:before,.row:after{display:table;content:"";line-height:0}
.row:after{clear:both}
[class*="span"]{float:left;min-height:1px;margin-left:20px}
.container,.navbar-static-top .container,.navbar-fixed-top .container,.navbar-fixed-bottom .container{width:940px}
.span12{width:940px}
.span11{width:860px}
.span10{width:780px}
.span9{width:700px}
.span8{width:620px}
.span7{width:540px}
.span6{width:460px}
.span5{width:380px}
.span4{width:300px}
.span3{width:220px}
.span2{width:140px}
.span1{width:60px}
.offset12{margin-left:980px}
.offset11{margin-left:900px}
.offset10{margin-left:820px}
.offset9{margin-left:740px}
.offset8{margin-left:660px}
.offset7{margin-left:580px}
.offset6{margin-left:500px}
.offset5{margin-left:420px}
.offset4{margin-left:340px}
.offset3{margin-left:260px}
.offset2{margin-left:180px}
.offset1{margin-left:100px}
.row-fluid{width:100%;*zoom:1}.row-fluid:before,.row-fluid:after{display:table;content:"";line-height:0}
.row-fluid:after{clear:both}
.row-fluid [class*="span"]{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;float:left;margin-left:2.127659574468085%;*margin-left:2.074468085106383%}
.row-fluid [class*="span"]:first-child{margin-left:0}
.row-fluid .controls-row [class*="span"]+[class*="span"]{margin-left:2.127659574468085%}
.row-fluid .span12{width:100%;*width:99.94680851063829%}
.row-fluid .span11{width:91.48936170212765%;*width:91.43617021276594%}
.row-fluid .span10{width:82.97872340425532%;*width:82.92553191489361%}
.row-fluid .span9{width:74.46808510638297%;*width:74.41489361702126%}
.row-fluid .span8{width:65.95744680851064%;*width:65.90425531914893%}
.row-fluid .span7{width:57.44680851063829%;*width:57.39361702127659%}
.row-fluid .span6{width:48.93617021276595%;*width:48.88297872340425%}
.row-fluid .span5{width:40.42553191489362%;*width:40.37234042553192%}
.row-fluid .span4{width:31.914893617021278%;*width:31.861702127659576%}
.row-fluid .span3{width:23.404255319148934%;*width:23.351063829787233%}
.row-fluid .span2{width:14.893617021276595%;*width:14.840425531914894%}
.row-fluid .span1{width:6.382978723404255%;*width:6.329787234042553%}
.row-fluid .offset12{margin-left:104.25531914893617%;*margin-left:104.14893617021275%}
.row-fluid .offset12:first-child{margin-left:102.12765957446808%;*margin-left:102.02127659574467%}
.row-fluid .offset11{margin-left:95.74468085106382%;*margin-left:95.6382978723404%}
.row-fluid .offset11:first-child{margin-left:93.61702127659574%;*margin-left:93.51063829787232%}
.row-fluid .offset10{margin-left:87.23404255319149%;*margin-left:87.12765957446807%}
.row-fluid .offset10:first-child{margin-left:85.1063829787234%;*margin-left:84.99999999999999%}
.row-fluid .offset9{margin-left:78.72340425531914%;*margin-left:78.61702127659572%}
.row-fluid .offset9:first-child{margin-left:76.59574468085106%;*margin-left:76.48936170212764%}
.row-fluid .offset8{margin-left:70.2127659574468%;*margin-left:70.10638297872339%}
.row-fluid .offset8:first-child{margin-left:68.08510638297872%;*margin-left:67.9787234042553%}
.row-fluid .offset7{margin-left:61.70212765957446%;*margin-left:61.59574468085106%}
.row-fluid .offset7:first-child{margin-left:59.574468085106375%;*margin-left:59.46808510638297%}
.row-fluid .offset6{margin-left:53.191489361702125%;*margin-left:53.085106382978715%}
.row-fluid .offset6:first-child{margin-left:51.063829787234035%;*margin-left:50.95744680851063%}
.row-fluid .offset5{margin-left:44.68085106382979%;*margin-left:44.57446808510638%}
.row-fluid .offset5:first-child{margin-left:42.5531914893617%;*margin-left:42.4468085106383%}
.row-fluid .offset4{margin-left:36.170212765957444%;*margin-left:36.06382978723405%}
.row-fluid .offset4:first-child{margin-left:34.04255319148936%;*margin-left:33.93617021276596%}
.row-fluid .offset3{margin-left:27.659574468085104%;*margin-left:27.5531914893617%}
.row-fluid .offset3:first-child{margin-left:25.53191489361702%;*margin-left:25.425531914893618%}
.row-fluid .offset2{margin-left:19.148936170212764%;*margin-left:19.04255319148936%}
.row-fluid .offset2:first-child{margin-left:17.02127659574468%;*margin-left:16.914893617021278%}
.row-fluid .offset1{margin-left:10.638297872340425%;*margin-left:10.53191489361702%}
.row-fluid .offset1:first-child{margin-left:8.51063829787234%;*margin-left:8.404255319148938%}
[class*="span"].hide,.row-fluid [class*="span"].hide{display:none}
[class*="span"].pull-right,.row-fluid [class*="span"].pull-right{float:right}
.container{margin-right:auto;margin-left:auto;*zoom:1}.container:before,.container:after{display:table;content:"";line-height:0}
.container:after{clear:both}
.container-fluid{padding-right:20px;padding-left:20px;*zoom:1}.container-fluid:before,.container-fluid:after{display:table;content:"";line-height:0}
.container-fluid:after{clear:both}
p{margin:0 0 10px}
.lead{margin-bottom:20px;font-size:19.5px;font-weight:200;line-height:30px}
small{font-size:85%}
strong{font-weight:bold}
em{font-style:italic}
cite{font-style:normal}
.muted{color:#999}
a.muted:hover,a.muted:focus{color:#808080}
.text-warning{color:#c09853}
a.text-warning:hover,a.text-warning:focus{color:#a47e3c}
.text-error{color:#b94a48}
a.text-error:hover,a.text-error:focus{color:#953b39}
.text-info{color:#3a87ad}
a.text-info:hover,a.text-info:focus{color:#2d6987}
.text-success{color:#468847}
a.text-success:hover,a.text-success:focus{color:#356635}
.text-left{text-align:left}
.text-right{text-align:right}
.text-center{text-align:center}
h1,h2,h3,h4,h5,h6{margin:10px 0;font-family:inherit;font-weight:bold;line-height:20px;color:inherit;text-rendering:optimizelegibility}h1 small,h2 small,h3 small,h4 small,h5 small,h6 small{font-weight:normal;line-height:1;color:#999}
h1,h2,h3{line-height:40px}
h1{font-size:35.75px}
h2{font-size:29.25px}
h3{font-size:22.75px}
h4{font-size:16.25px}
h5{font-size:13px}
h6{font-size:11.049999999999999px}
h1 small{font-size:22.75px}
h2 small{font-size:16.25px}
h3 small{font-size:13px}
h4 small{font-size:13px}
.page-header{padding-bottom:9px;margin:20px 0 30px;border-bottom:1px solid #eee}
ul,ol{padding:0;margin:0 0 10px 25px}
ul ul,ul ol,ol ol,ol ul{margin-bottom:0}
li{line-height:20px}
ul.unstyled,ol.unstyled{margin-left:0;list-style:none}
ul.inline,ol.inline{margin-left:0;list-style:none}ul.inline>li,ol.inline>li{display:inline-block;*display:inline;*zoom:1;padding-left:5px;padding-right:5px}
dl{margin-bottom:20px}
dt,dd{line-height:20px}
dt{font-weight:bold}
dd{margin-left:10px}
.dl-horizontal{*zoom:1}.dl-horizontal:before,.dl-horizontal:after{display:table;content:"";line-height:0}
.dl-horizontal:after{clear:both}
.dl-horizontal dt{float:left;width:160px;clear:left;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.dl-horizontal dd{margin-left:180px}
hr{margin:20px 0;border:0;border-top:1px solid #eee;border-bottom:1px solid #fff}
abbr[title],abbr[data-original-title]{cursor:help;border-bottom:1px dotted #999}
abbr.initialism{font-size:90%;text-transform:uppercase}
blockquote{padding:0 0 0 15px;margin:0 0 20px;border-left:5px solid #eee}blockquote p{margin-bottom:0;font-size:16.25px;font-weight:300;line-height:1.25}
blockquote small{display:block;line-height:20px;color:#999}blockquote small:before{content:'\2014 \00A0'}
blockquote.pull-right{float:right;padding-right:15px;padding-left:0;border-right:5px solid #eee;border-left:0}blockquote.pull-right p,blockquote.pull-right small{text-align:right}
blockquote.pull-right small:before{content:''}
blockquote.pull-right small:after{content:'\00A0 \2014'}
q:before,q:after,blockquote:before,blockquote:after{content:""}
address{display:block;margin-bottom:20px;font-style:normal;line-height:20px}
code,pre{padding:0 3px 2px;font-family:monospace;font-size:11px;color:#333;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
code{padding:2px 4px;color:#d14;background-color:#f7f7f9;border:1px solid #e1e1e8;white-space:nowrap}
pre{display:block;padding:9.5px;margin:0 0 10px;font-size:12px;line-height:20px;word-break:break-all;word-wrap:break-word;white-space:pre;white-space:pre-wrap;background-color:#f5f5f5;border:1px solid #ccc;border:1px solid rgba(0,0,0,0.15);border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}pre.prettyprint{margin-bottom:20px}
pre code{padding:0;color:inherit;white-space:pre;white-space:pre-wrap;background-color:transparent;border:0}
.pre-scrollable{max-height:340px;overflow-y:scroll}
form{margin:0 0 20px}
fieldset{padding:0;margin:0;border:0}
legend{display:block;width:100%;padding:0;margin-bottom:20px;font-size:19.5px;line-height:40px;color:#333;border:0;border-bottom:1px solid #e5e5e5}legend small{font-size:15px;color:#999}
label,input,button,select,textarea{font-size:13px;font-weight:normal;line-height:20px}
input,button,select,textarea{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}
label{display:block;margin-bottom:5px}
select,textarea,input[type="text"],input[type="password"],input[type="datetime"],input[type="datetime-local"],input[type="date"],input[type="month"],input[type="time"],input[type="week"],input[type="number"],input[type="email"],input[type="url"],input[type="search"],input[type="tel"],input[type="color"],.uneditable-input{display:inline-block;height:20px;padding:4px 6px;margin-bottom:10px;font-size:13px;line-height:20px;color:#555;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;vertical-align:middle}
input,textarea,.uneditable-input{width:206px}
textarea{height:auto}
textarea,input[type="text"],input[type="password"],input[type="datetime"],input[type="datetime-local"],input[type="date"],input[type="month"],input[type="time"],input[type="week"],input[type="number"],input[type="email"],input[type="url"],input[type="search"],input[type="tel"],input[type="color"],.uneditable-input{background-color:#fff;border:1px solid #ccc;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-webkit-transition:border linear .2s, box-shadow linear .2s;-moz-transition:border linear .2s, box-shadow linear .2s;-o-transition:border linear .2s, box-shadow linear .2s;transition:border linear .2s, box-shadow linear .2s}textarea:focus,input[type="text"]:focus,input[type="password"]:focus,input[type="datetime"]:focus,input[type="datetime-local"]:focus,input[type="date"]:focus,input[type="month"]:focus,input[type="time"]:focus,input[type="week"]:focus,input[type="number"]:focus,input[type="email"]:focus,input[type="url"]:focus,input[type="search"]:focus,input[type="tel"]:focus,input[type="color"]:focus,.uneditable-input:focus{border-color:rgba(82,168,236,0.8);outline:0;outline:thin dotted \9;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6);box-shadow:inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6)}
input[type="radio"],input[type="checkbox"]{margin:4px 0 0;*margin-top:0;margin-top:1px \9;line-height:normal}
input[type="file"],input[type="image"],input[type="submit"],input[type="reset"],input[type="button"],input[type="radio"],input[type="checkbox"]{width:auto}
select,input[type="file"]{height:30px;*margin-top:4px;line-height:30px}
select{width:220px;border:1px solid #ccc;background-color:#fff}
select[multiple],select[size]{height:auto}
select:focus,input[type="file"]:focus,input[type="radio"]:focus,input[type="checkbox"]:focus{outline:thin dotted #333;outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}
.uneditable-input,.uneditable-textarea{color:#999;background-color:#fcfcfc;border-color:#ccc;-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,0.025);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.025);box-shadow:inset 0 1px 2px rgba(0,0,0,0.025);cursor:not-allowed}
.uneditable-input{overflow:hidden;white-space:nowrap}
.uneditable-textarea{width:auto;height:auto}
input:-moz-placeholder,textarea:-moz-placeholder{color:#999}
input:-ms-input-placeholder,textarea:-ms-input-placeholder{color:#999}
input::-webkit-input-placeholder,textarea::-webkit-input-placeholder{color:#999}
.radio,.checkbox{min-height:20px;padding-left:20px}
.radio input[type="radio"],.checkbox input[type="checkbox"]{float:left;margin-left:-20px}
.controls>.radio:first-child,.controls>.checkbox:first-child{padding-top:5px}
.radio.inline,.checkbox.inline{display:inline-block;padding-top:5px;margin-bottom:0;vertical-align:middle}
.radio.inline+.radio.inline,.checkbox.inline+.checkbox.inline{margin-left:10px}
.input-mini{width:60px}
.input-small{width:90px}
.input-medium{width:150px}
.input-large{width:210px}
.input-xlarge{width:270px}
.input-xxlarge{width:530px}
input[class*="span"],select[class*="span"],textarea[class*="span"],.uneditable-input[class*="span"],.row-fluid input[class*="span"],.row-fluid select[class*="span"],.row-fluid textarea[class*="span"],.row-fluid .uneditable-input[class*="span"]{float:none;margin-left:0}
.input-append input[class*="span"],.input-append .uneditable-input[class*="span"],.input-prepend input[class*="span"],.input-prepend .uneditable-input[class*="span"],.row-fluid input[class*="span"],.row-fluid select[class*="span"],.row-fluid textarea[class*="span"],.row-fluid .uneditable-input[class*="span"],.row-fluid .input-prepend [class*="span"],.row-fluid .input-append [class*="span"]{display:inline-block}
input,textarea,.uneditable-input{margin-left:0}
.controls-row [class*="span"]+[class*="span"]{margin-left:20px}
input.span12,textarea.span12,.uneditable-input.span12{width:926px}
input.span11,textarea.span11,.uneditable-input.span11{width:846px}
input.span10,textarea.span10,.uneditable-input.span10{width:766px}
input.span9,textarea.span9,.uneditable-input.span9{width:686px}
input.span8,textarea.span8,.uneditable-input.span8{width:606px}
input.span7,textarea.span7,.uneditable-input.span7{width:526px}
input.span6,textarea.span6,.uneditable-input.span6{width:446px}
input.span5,textarea.span5,.uneditable-input.span5{width:366px}
input.span4,textarea.span4,.uneditable-input.span4{width:286px}
input.span3,textarea.span3,.uneditable-input.span3{width:206px}
input.span2,textarea.span2,.uneditable-input.span2{width:126px}
input.span1,textarea.span1,.uneditable-input.span1{width:46px}
.controls-row{*zoom:1}.controls-row:before,.controls-row:after{display:table;content:"";line-height:0}
.controls-row:after{clear:both}
.controls-row [class*="span"],.row-fluid .controls-row [class*="span"]{float:left}
.controls-row .checkbox[class*="span"],.controls-row .radio[class*="span"]{padding-top:5px}
input[disabled],select[disabled],textarea[disabled],input[readonly],select[readonly],textarea[readonly]{cursor:not-allowed;background-color:#eee}
input[type="radio"][disabled],input[type="checkbox"][disabled],input[type="radio"][readonly],input[type="checkbox"][readonly]{background-color:transparent}
.control-group.warning .control-label,.control-group.warning .help-block,.control-group.warning .help-inline{color:#c09853}
.control-group.warning .checkbox,.control-group.warning .radio,.control-group.warning input,.control-group.warning select,.control-group.warning textarea{color:#c09853}
.control-group.warning input,.control-group.warning select,.control-group.warning textarea{border-color:#c09853;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.control-group.warning input:focus,.control-group.warning select:focus,.control-group.warning textarea:focus{border-color:#a47e3c;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #dbc59e;-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #dbc59e;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #dbc59e}
.control-group.warning .input-prepend .add-on,.control-group.warning .input-append .add-on{color:#c09853;background-color:#fcf8e3;border-color:#c09853}
.control-group.error .control-label,.control-group.error .help-block,.control-group.error .help-inline{color:#b94a48}
.control-group.error .checkbox,.control-group.error .radio,.control-group.error input,.control-group.error select,.control-group.error textarea{color:#b94a48}
.control-group.error input,.control-group.error select,.control-group.error textarea{border-color:#b94a48;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.control-group.error input:focus,.control-group.error select:focus,.control-group.error textarea:focus{border-color:#953b39;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #d59392;-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #d59392;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #d59392}
.control-group.error .input-prepend .add-on,.control-group.error .input-append .add-on{color:#b94a48;background-color:#f2dede;border-color:#b94a48}
.control-group.success .control-label,.control-group.success .help-block,.control-group.success .help-inline{color:#468847}
.control-group.success .checkbox,.control-group.success .radio,.control-group.success input,.control-group.success select,.control-group.success textarea{color:#468847}
.control-group.success input,.control-group.success select,.control-group.success textarea{border-color:#468847;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.control-group.success input:focus,.control-group.success select:focus,.control-group.success textarea:focus{border-color:#356635;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7aba7b;-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7aba7b;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7aba7b}
.control-group.success .input-prepend .add-on,.control-group.success .input-append .add-on{color:#468847;background-color:#dff0d8;border-color:#468847}
.control-group.info .control-label,.control-group.info .help-block,.control-group.info .help-inline{color:#3a87ad}
.control-group.info .checkbox,.control-group.info .radio,.control-group.info input,.control-group.info select,.control-group.info textarea{color:#3a87ad}
.control-group.info input,.control-group.info select,.control-group.info textarea{border-color:#3a87ad;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075);box-shadow:inset 0 1px 1px rgba(0,0,0,0.075)}.control-group.info input:focus,.control-group.info select:focus,.control-group.info textarea:focus{border-color:#2d6987;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7ab5d3;-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7ab5d3;box-shadow:inset 0 1px 1px rgba(0,0,0,0.075),0 0 6px #7ab5d3}
.control-group.info .input-prepend .add-on,.control-group.info .input-append .add-on{color:#3a87ad;background-color:#d9edf7;border-color:#3a87ad}
input:focus:invalid,textarea:focus:invalid,select:focus:invalid{color:#b94a48;border-color:#ee5f5b}input:focus:invalid:focus,textarea:focus:invalid:focus,select:focus:invalid:focus{border-color:#e9322d;-webkit-box-shadow:0 0 6px #f8b9b7;-moz-box-shadow:0 0 6px #f8b9b7;box-shadow:0 0 6px #f8b9b7}
.form-actions{padding:19px 20px 20px;margin-top:20px;margin-bottom:20px;background-color:#f5f5f5;border-top:1px solid #e5e5e5;*zoom:1}.form-actions:before,.form-actions:after{display:table;content:"";line-height:0}
.form-actions:after{clear:both}
.help-block,.help-inline{color:#262626}
.help-block{display:block;margin-bottom:10px}
.help-inline{display:inline-block;*display:inline;*zoom:1;vertical-align:middle;padding-left:5px}
.input-append,.input-prepend{display:inline-block;margin-bottom:10px;vertical-align:middle;font-size:0;white-space:nowrap}.input-append input,.input-prepend input,.input-append select,.input-prepend select,.input-append .uneditable-input,.input-prepend .uneditable-input,.input-append .dropdown-menu,.input-prepend .dropdown-menu,.input-append .popover,.input-prepend .popover{font-size:13px}
.input-append input,.input-prepend input,.input-append select,.input-prepend select,.input-append .uneditable-input,.input-prepend .uneditable-input{position:relative;margin-bottom:0;*margin-left:0;vertical-align:top;border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}.input-append input:focus,.input-prepend input:focus,.input-append select:focus,.input-prepend select:focus,.input-append .uneditable-input:focus,.input-prepend .uneditable-input:focus{z-index:2}
.input-append .add-on,.input-prepend .add-on{display:inline-block;width:auto;height:20px;min-width:16px;padding:4px 5px;font-size:13px;font-weight:normal;line-height:20px;text-align:center;text-shadow:0 1px 0 #fff;background-color:#eee;border:1px solid #ccc}
.input-append .add-on,.input-prepend .add-on,.input-append .btn,.input-prepend .btn,.input-append .btn-group>.dropdown-toggle,.input-prepend .btn-group>.dropdown-toggle{vertical-align:top;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.input-append .active,.input-prepend .active{background-color:#a9dba9;border-color:#46a546}
.input-prepend .add-on,.input-prepend .btn{margin-right:-1px}
.input-prepend .add-on:first-child,.input-prepend .btn:first-child{border-radius:4px 0 0 4px;-webkit-border-radius:4px 0 0 4px;-moz-border-radius:4px 0 0 4px;border-radius:4px 0 0 4px}
.input-append input,.input-append select,.input-append .uneditable-input{border-radius:4px 0 0 4px;-webkit-border-radius:4px 0 0 4px;-moz-border-radius:4px 0 0 4px;border-radius:4px 0 0 4px}.input-append input+.btn-group .btn:last-child,.input-append select+.btn-group .btn:last-child,.input-append .uneditable-input+.btn-group .btn:last-child{border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.input-append .add-on,.input-append .btn,.input-append .btn-group{margin-left:-1px}
.input-append .add-on:last-child,.input-append .btn:last-child,.input-append .btn-group:last-child>.dropdown-toggle{border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.input-prepend.input-append input,.input-prepend.input-append select,.input-prepend.input-append .uneditable-input{border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}.input-prepend.input-append input+.btn-group .btn,.input-prepend.input-append select+.btn-group .btn,.input-prepend.input-append .uneditable-input+.btn-group .btn{border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.input-prepend.input-append .add-on:first-child,.input-prepend.input-append .btn:first-child{margin-right:-1px;border-radius:4px 0 0 4px;-webkit-border-radius:4px 0 0 4px;-moz-border-radius:4px 0 0 4px;border-radius:4px 0 0 4px}
.input-prepend.input-append .add-on:last-child,.input-prepend.input-append .btn:last-child{margin-left:-1px;border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.input-prepend.input-append .btn-group:first-child{margin-left:0}
input.search-query{padding-right:14px;padding-right:4px \9;padding-left:14px;padding-left:4px \9;margin-bottom:0;border-radius:15px;-webkit-border-radius:15px;-moz-border-radius:15px;border-radius:15px}
.form-search .input-append .search-query,.form-search .input-prepend .search-query{border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.form-search .input-append .search-query{border-radius:14px 0 0 14px;-webkit-border-radius:14px 0 0 14px;-moz-border-radius:14px 0 0 14px;border-radius:14px 0 0 14px}
.form-search .input-append .btn{border-radius:0 14px 14px 0;-webkit-border-radius:0 14px 14px 0;-moz-border-radius:0 14px 14px 0;border-radius:0 14px 14px 0}
.form-search .input-prepend .search-query{border-radius:0 14px 14px 0;-webkit-border-radius:0 14px 14px 0;-moz-border-radius:0 14px 14px 0;border-radius:0 14px 14px 0}
.form-search .input-prepend .btn{border-radius:14px 0 0 14px;-webkit-border-radius:14px 0 0 14px;-moz-border-radius:14px 0 0 14px;border-radius:14px 0 0 14px}
.form-search input,.form-inline input,.form-horizontal input,.form-search textarea,.form-inline textarea,.form-horizontal textarea,.form-search select,.form-inline select,.form-horizontal select,.form-search .help-inline,.form-inline .help-inline,.form-horizontal .help-inline,.form-search .uneditable-input,.form-inline .uneditable-input,.form-horizontal .uneditable-input,.form-search .input-prepend,.form-inline .input-prepend,.form-horizontal .input-prepend,.form-search .input-append,.form-inline .input-append,.form-horizontal .input-append{display:inline-block;*display:inline;*zoom:1;margin-bottom:0;vertical-align:middle}
.form-search .hide,.form-inline .hide,.form-horizontal .hide{display:none}
.form-search label,.form-inline label,.form-search .btn-group,.form-inline .btn-group{display:inline-block}
.form-search .input-append,.form-inline .input-append,.form-search .input-prepend,.form-inline .input-prepend{margin-bottom:0}
.form-search .radio,.form-search .checkbox,.form-inline .radio,.form-inline .checkbox{padding-left:0;margin-bottom:0;vertical-align:middle}
.form-search .radio input[type="radio"],.form-search .checkbox input[type="checkbox"],.form-inline .radio input[type="radio"],.form-inline .checkbox input[type="checkbox"]{float:left;margin-right:3px;margin-left:0}
.control-group{margin-bottom:10px}
legend+.control-group{margin-top:20px;-webkit-margin-top-collapse:separate}
.form-horizontal .control-group{margin-bottom:20px;*zoom:1}.form-horizontal .control-group:before,.form-horizontal .control-group:after{display:table;content:"";line-height:0}
.form-horizontal .control-group:after{clear:both}
.form-horizontal .control-label{float:left;width:160px;padding-top:5px;text-align:right}
.form-horizontal .controls{*display:inline-block;*padding-left:20px;margin-left:180px;*margin-left:0}.form-horizontal .controls:first-child{*padding-left:180px}
.form-horizontal .help-block{margin-bottom:0}
.form-horizontal input+.help-block,.form-horizontal select+.help-block,.form-horizontal textarea+.help-block,.form-horizontal .uneditable-input+.help-block,.form-horizontal .input-prepend+.help-block,.form-horizontal .input-append+.help-block{margin-top:10px}
.form-horizontal .form-actions{padding-left:180px}
table{max-width:100%;background-color:transparent;border-collapse:collapse;border-spacing:0}
.table{width:100%;margin-bottom:20px}.table th,.table td{padding:8px;line-height:20px;text-align:left;vertical-align:top;border-top:1px solid #ddd}
.table th{font-weight:bold}
.table thead th{vertical-align:bottom}
.table caption+thead tr:first-child th,.table caption+thead tr:first-child td,.table colgroup+thead tr:first-child th,.table colgroup+thead tr:first-child td,.table thead:first-child tr:first-child th,.table thead:first-child tr:first-child td{border-top:0}
.table tbody+tbody{border-top:2px solid #ddd}
.table .table{background-color:#fff}
.table-condensed th,.table-condensed td{padding:4px 5px}
.table-bordered{border:1px solid #ddd;border-collapse:separate;*border-collapse:collapse;border-left:0;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}.table-bordered th,.table-bordered td{border-left:1px solid #ddd}
.table-bordered caption+thead tr:first-child th,.table-bordered caption+tbody tr:first-child th,.table-bordered caption+tbody tr:first-child td,.table-bordered colgroup+thead tr:first-child th,.table-bordered colgroup+tbody tr:first-child th,.table-bordered colgroup+tbody tr:first-child td,.table-bordered thead:first-child tr:first-child th,.table-bordered tbody:first-child tr:first-child th,.table-bordered tbody:first-child tr:first-child td{border-top:0}
.table-bordered thead:first-child tr:first-child>th:first-child,.table-bordered tbody:first-child tr:first-child>td:first-child,.table-bordered tbody:first-child tr:first-child>th:first-child{-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px}
.table-bordered thead:first-child tr:first-child>th:last-child,.table-bordered tbody:first-child tr:first-child>td:last-child,.table-bordered tbody:first-child tr:first-child>th:last-child{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px}
.table-bordered thead:last-child tr:last-child>th:first-child,.table-bordered tbody:last-child tr:last-child>td:first-child,.table-bordered tbody:last-child tr:last-child>th:first-child,.table-bordered tfoot:last-child tr:last-child>td:first-child,.table-bordered tfoot:last-child tr:last-child>th:first-child{-webkit-border-bottom-left-radius:4px;-moz-border-radius-bottomleft:4px;border-bottom-left-radius:4px}
.table-bordered thead:last-child tr:last-child>th:last-child,.table-bordered tbody:last-child tr:last-child>td:last-child,.table-bordered tbody:last-child tr:last-child>th:last-child,.table-bordered tfoot:last-child tr:last-child>td:last-child,.table-bordered tfoot:last-child tr:last-child>th:last-child{-webkit-border-bottom-right-radius:4px;-moz-border-radius-bottomright:4px;border-bottom-right-radius:4px}
.table-bordered tfoot+tbody:last-child tr:last-child td:first-child{-webkit-border-bottom-left-radius:0;-moz-border-radius-bottomleft:0;border-bottom-left-radius:0}
.table-bordered tfoot+tbody:last-child tr:last-child td:last-child{-webkit-border-bottom-right-radius:0;-moz-border-radius-bottomright:0;border-bottom-right-radius:0}
.table-bordered caption+thead tr:first-child th:first-child,.table-bordered caption+tbody tr:first-child td:first-child,.table-bordered colgroup+thead tr:first-child th:first-child,.table-bordered colgroup+tbody tr:first-child td:first-child{-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px}
.table-bordered caption+thead tr:first-child th:last-child,.table-bordered caption+tbody tr:first-child td:last-child,.table-bordered colgroup+thead tr:first-child th:last-child,.table-bordered colgroup+tbody tr:first-child td:last-child{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px}
.table-striped tbody>tr:nth-child(odd)>td,.table-striped tbody>tr:nth-child(odd)>th{background-color:#f9f9f9}
.table-hover tbody tr:hover>td,.table-hover tbody tr:hover>th{background-color:#f5f5f5}
table td[class*="span"],table th[class*="span"],.row-fluid table td[class*="span"],.row-fluid table th[class*="span"]{display:table-cell;float:none;margin-left:0}
.table td.span1,.table th.span1{float:none;width:44px;margin-left:0}
.table td.span2,.table th.span2{float:none;width:124px;margin-left:0}
.table td.span3,.table th.span3{float:none;width:204px;margin-left:0}
.table td.span4,.table th.span4{float:none;width:284px;margin-left:0}
.table td.span5,.table th.span5{float:none;width:364px;margin-left:0}
.table td.span6,.table th.span6{float:none;width:444px;margin-left:0}
.table td.span7,.table th.span7{float:none;width:524px;margin-left:0}
.table td.span8,.table th.span8{float:none;width:604px;margin-left:0}
.table td.span9,.table th.span9{float:none;width:684px;margin-left:0}
.table td.span10,.table th.span10{float:none;width:764px;margin-left:0}
.table td.span11,.table th.span11{float:none;width:844px;margin-left:0}
.table td.span12,.table th.span12{float:none;width:924px;margin-left:0}
.table tbody tr.success>td{background-color:#dff0d8}
.table tbody tr.error>td{background-color:#f2dede}
.table tbody tr.warning>td{background-color:#fcf8e3}
.table tbody tr.info>td{background-color:#d9edf7}
.table-hover tbody tr.success:hover>td{background-color:#d0e9c6}
.table-hover tbody tr.error:hover>td{background-color:#ebcccc}
.table-hover tbody tr.warning:hover>td{background-color:#faf2cc}
.table-hover tbody tr.info:hover>td{background-color:#c4e3f3}
[class^="icon-"],[class*=" icon-"]{display:inline-block;width:14px;height:14px;*margin-right:.3em;line-height:14px;vertical-align:text-top;background-image:url("../img/glyphicons-halflings.png");background-position:14px 14px;background-repeat:no-repeat;margin-top:1px}
.icon-white,.nav-pills>.active>a>[class^="icon-"],.nav-pills>.active>a>[class*=" icon-"],.nav-list>.active>a>[class^="icon-"],.nav-list>.active>a>[class*=" icon-"],.navbar-inverse .nav>.active>a>[class^="icon-"],.navbar-inverse .nav>.active>a>[class*=" icon-"],.dropdown-menu>li>a:hover>[class^="icon-"],.dropdown-menu>li>a:focus>[class^="icon-"],.dropdown-menu>li>a:hover>[class*=" icon-"],.dropdown-menu>li>a:focus>[class*=" icon-"],.dropdown-menu>.active>a>[class^="icon-"],.dropdown-menu>.active>a>[class*=" icon-"],.dropdown-submenu:hover>a>[class^="icon-"],.dropdown-submenu:focus>a>[class^="icon-"],.dropdown-submenu:hover>a>[class*=" icon-"],.dropdown-submenu:focus>a>[class*=" icon-"]{background-image:url("../img/glyphicons-halflings-white.png")}
.icon-glass{background-position:0 0}
.icon-music{background-position:-24px 0}
.icon-search{background-position:-48px 0}
.icon-envelope{background-position:-72px 0}
.icon-heart{background-position:-96px 0}
.icon-star{background-position:-120px 0}
.icon-star-empty{background-position:-144px 0}
.icon-user{background-position:-168px 0}
.icon-film{background-position:-192px 0}
.icon-th-large{background-position:-216px 0}
.icon-th{background-position:-240px 0}
.icon-th-list{background-position:-264px 0}
.icon-ok{background-position:-288px 0}
.icon-remove{background-position:-312px 0}
.icon-zoom-in{background-position:-336px 0}
.icon-zoom-out{background-position:-360px 0}
.icon-off{background-position:-384px 0}
.icon-signal{background-position:-408px 0}
.icon-cog{background-position:-432px 0}
.icon-trash{background-position:-456px 0}
.icon-home{background-position:0 -24px}
.icon-file{background-position:-24px -24px}
.icon-time{background-position:-48px -24px}
.icon-road{background-position:-72px -24px}
.icon-download-alt{background-position:-96px -24px}
.icon-download{background-position:-120px -24px}
.icon-upload{background-position:-144px -24px}
.icon-inbox{background-position:-168px -24px}
.icon-play-circle{background-position:-192px -24px}
.icon-repeat{background-position:-216px -24px}
.icon-refresh{background-position:-240px -24px}
.icon-list-alt{background-position:-264px -24px}
.icon-lock{background-position:-287px -24px}
.icon-flag{background-position:-312px -24px}
.icon-headphones{background-position:-336px -24px}
.icon-volume-off{background-position:-360px -24px}
.icon-volume-down{background-position:-384px -24px}
.icon-volume-up{background-position:-408px -24px}
.icon-qrcode{background-position:-432px -24px}
.icon-barcode{background-position:-456px -24px}
.icon-tag{background-position:0 -48px}
.icon-tags{background-position:-25px -48px}
.icon-book{background-position:-48px -48px}
.icon-bookmark{background-position:-72px -48px}
.icon-print{background-position:-96px -48px}
.icon-camera{background-position:-120px -48px}
.icon-font{background-position:-144px -48px}
.icon-bold{background-position:-167px -48px}
.icon-italic{background-position:-192px -48px}
.icon-text-height{background-position:-216px -48px}
.icon-text-width{background-position:-240px -48px}
.icon-align-left{background-position:-264px -48px}
.icon-align-center{background-position:-288px -48px}
.icon-align-right{background-position:-312px -48px}
.icon-align-justify{background-position:-336px -48px}
.icon-list{background-position:-360px -48px}
.icon-indent-left{background-position:-384px -48px}
.icon-indent-right{background-position:-408px -48px}
.icon-facetime-video{background-position:-432px -48px}
.icon-picture{background-position:-456px -48px}
.icon-pencil{background-position:0 -72px}
.icon-map-marker{background-position:-24px -72px}
.icon-adjust{background-position:-48px -72px}
.icon-tint{background-position:-72px -72px}
.icon-edit{background-position:-96px -72px}
.icon-share{background-position:-120px -72px}
.icon-check{background-position:-144px -72px}
.icon-move{background-position:-168px -72px}
.icon-step-backward{background-position:-192px -72px}
.icon-fast-backward{background-position:-216px -72px}
.icon-backward{background-position:-240px -72px}
.icon-play{background-position:-264px -72px}
.icon-pause{background-position:-288px -72px}
.icon-stop{background-position:-312px -72px}
.icon-forward{background-position:-336px -72px}
.icon-fast-forward{background-position:-360px -72px}
.icon-step-forward{background-position:-384px -72px}
.icon-eject{background-position:-408px -72px}
.icon-chevron-left{background-position:-432px -72px}
.icon-chevron-right{background-position:-456px -72px}
.icon-plus-sign{background-position:0 -96px}
.icon-minus-sign{background-position:-24px -96px}
.icon-remove-sign{background-position:-48px -96px}
.icon-ok-sign{background-position:-72px -96px}
.icon-question-sign{background-position:-96px -96px}
.icon-info-sign{background-position:-120px -96px}
.icon-screenshot{background-position:-144px -96px}
.icon-remove-circle{background-position:-168px -96px}
.icon-ok-circle{background-position:-192px -96px}
.icon-ban-circle{background-position:-216px -96px}
.icon-arrow-left{background-position:-240px -96px}
.icon-arrow-right{background-position:-264px -96px}
.icon-arrow-up{background-position:-289px -96px}
.icon-arrow-down{background-position:-312px -96px}
.icon-share-alt{background-position:-336px -96px}
.icon-resize-full{background-position:-360px -96px}
.icon-resize-small{background-position:-384px -96px}
.icon-plus{background-position:-408px -96px}
.icon-minus{background-position:-433px -96px}
.icon-asterisk{background-position:-456px -96px}
.icon-exclamation-sign{background-position:0 -120px}
.icon-gift{background-position:-24px -120px}
.icon-leaf{background-position:-48px -120px}
.icon-fire{background-position:-72px -120px}
.icon-eye-open{background-position:-96px -120px}
.icon-eye-close{background-position:-120px -120px}
.icon-warning-sign{background-position:-144px -120px}
.icon-plane{background-position:-168px -120px}
.icon-calendar{background-position:-192px -120px}
.icon-random{background-position:-216px -120px;width:16px}
.icon-comment{background-position:-240px -120px}
.icon-magnet{background-position:-264px -120px}
.icon-chevron-up{background-position:-288px -120px}
.icon-chevron-down{background-position:-313px -119px}
.icon-retweet{background-position:-336px -120px}
.icon-shopping-cart{background-position:-360px -120px}
.icon-folder-close{background-position:-384px -120px;width:16px}
.icon-folder-open{background-position:-408px -120px;width:16px}
.icon-resize-vertical{background-position:-432px -119px}
.icon-resize-horizontal{background-position:-456px -118px}
.icon-hdd{background-position:0 -144px}
.icon-bullhorn{background-position:-24px -144px}
.icon-bell{background-position:-48px -144px}
.icon-certificate{background-position:-72px -144px}
.icon-thumbs-up{background-position:-96px -144px}
.icon-thumbs-down{background-position:-120px -144px}
.icon-hand-right{background-position:-144px -144px}
.icon-hand-left{background-position:-168px -144px}
.icon-hand-up{background-position:-192px -144px}
.icon-hand-down{background-position:-216px -144px}
.icon-circle-arrow-right{background-position:-240px -144px}
.icon-circle-arrow-left{background-position:-264px -144px}
.icon-circle-arrow-up{background-position:-288px -144px}
.icon-circle-arrow-down{background-position:-312px -144px}
.icon-globe{background-position:-336px -144px}
.icon-wrench{background-position:-360px -144px}
.icon-tasks{background-position:-384px -144px}
.icon-filter{background-position:-408px -144px}
.icon-briefcase{background-position:-432px -144px}
.icon-fullscreen{background-position:-456px -144px}
.dropup,.dropdown{position:relative}
.dropdown-toggle{*margin-bottom:-3px}
.dropdown-toggle:active,.open .dropdown-toggle{outline:0}
.caret{display:inline-block;width:0;height:0;vertical-align:top;border-top:4px solid #000;border-right:4px solid transparent;border-left:4px solid transparent;content:""}
.dropdown .caret{margin-top:8px;margin-left:2px}
.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:160px;padding:5px 0;margin:2px 0 0;list-style:none;background-color:#fff;border:1px solid #ccc;border:1px solid rgba(0,0,0,0.2);*border-right-width:2px;*border-bottom-width:2px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px;-webkit-box-shadow:0 5px 10px rgba(0,0,0,0.2);-moz-box-shadow:0 5px 10px rgba(0,0,0,0.2);box-shadow:0 5px 10px rgba(0,0,0,0.2);-webkit-background-clip:padding-box;-moz-background-clip:padding;background-clip:padding-box}.dropdown-menu.pull-right{right:0;left:auto}
.dropdown-menu .divider{*width:100%;height:1px;margin:9px 1px;*margin:-5px 0 5px;overflow:hidden;background-color:#e5e5e5;border-bottom:1px solid #fff}
.dropdown-menu>li>a{display:block;padding:3px 20px;clear:both;font-weight:normal;line-height:20px;color:#333;white-space:nowrap}
.dropdown-menu>li>a:hover,.dropdown-menu>li>a:focus,.dropdown-submenu:hover>a,.dropdown-submenu:focus>a{text-decoration:none;color:#fff;background-color:#0081c2;background-image:-moz-linear-gradient(top, #08c, #0077b3);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#08c), to(#0077b3));background-image:-webkit-linear-gradient(top, #08c, #0077b3);background-image:-o-linear-gradient(top, #08c, #0077b3);background-image:linear-gradient(to bottom, #08c, #0077b3);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0077b3', GradientType=0)}
.dropdown-menu>.active>a,.dropdown-menu>.active>a:hover,.dropdown-menu>.active>a:focus{color:#fff;text-decoration:none;outline:0;background-color:#0081c2;background-image:-moz-linear-gradient(top, #08c, #0077b3);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#08c), to(#0077b3));background-image:-webkit-linear-gradient(top, #08c, #0077b3);background-image:-o-linear-gradient(top, #08c, #0077b3);background-image:linear-gradient(to bottom, #08c, #0077b3);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0077b3', GradientType=0)}
.dropdown-menu>.disabled>a,.dropdown-menu>.disabled>a:hover,.dropdown-menu>.disabled>a:focus{color:#999}
.dropdown-menu>.disabled>a:hover,.dropdown-menu>.disabled>a:focus{text-decoration:none;background-color:transparent;background-image:none;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false);cursor:default}
.open{*z-index:1000}.open>.dropdown-menu{display:block}
.dropdown-backdrop{position:fixed;left:0;right:0;bottom:0;top:0;z-index:990}
.pull-right>.dropdown-menu{right:0;left:auto}
.dropup .caret,.navbar-fixed-bottom .dropdown .caret{border-top:0;border-bottom:4px solid #000;content:""}
.dropup .dropdown-menu,.navbar-fixed-bottom .dropdown .dropdown-menu{top:auto;bottom:100%;margin-bottom:1px}
.dropdown-submenu{position:relative}
.dropdown-submenu>.dropdown-menu{top:0;left:100%;margin-top:-6px;margin-left:-1px;border-radius:0 6px 6px 6px;-webkit-border-radius:0 6px 6px 6px;-moz-border-radius:0 6px 6px 6px;border-radius:0 6px 6px 6px}
.dropdown-submenu:hover>.dropdown-menu{display:block}
.dropup .dropdown-submenu>.dropdown-menu{top:auto;bottom:0;margin-top:0;margin-bottom:-2px;border-radius:5px 5px 5px 0;-webkit-border-radius:5px 5px 5px 0;-moz-border-radius:5px 5px 5px 0;border-radius:5px 5px 5px 0}
.dropdown-submenu>a:after{display:block;content:" ";float:right;width:0;height:0;border-color:transparent;border-style:solid;border-width:5px 0 5px 5px;border-left-color:#ccc;margin-top:5px;margin-right:-10px}
.dropdown-submenu:hover>a:after{border-left-color:#fff}
.dropdown-submenu.pull-left{float:none}.dropdown-submenu.pull-left>.dropdown-menu{left:-100%;margin-left:10px;border-radius:6px 0 6px 6px;-webkit-border-radius:6px 0 6px 6px;-moz-border-radius:6px 0 6px 6px;border-radius:6px 0 6px 6px}
.dropdown .dropdown-menu .nav-header{padding-left:20px;padding-right:20px}
.typeahead{z-index:1051;margin-top:2px;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.well{min-height:20px;padding:19px;margin-bottom:20px;background-color:#f5f5f5;border:1px solid #e3e3e3;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.05);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.05);box-shadow:inset 0 1px 1px rgba(0,0,0,0.05)}.well blockquote{border-color:#ddd;border-color:rgba(0,0,0,0.15)}
.well-large{padding:24px;border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.well-small{padding:9px;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.fade{opacity:0;-webkit-transition:opacity .15s linear;-moz-transition:opacity .15s linear;-o-transition:opacity .15s linear;transition:opacity .15s linear}.fade.in{opacity:1}
.collapse{position:relative;height:0;overflow:hidden;-webkit-transition:height .35s ease;-moz-transition:height .35s ease;-o-transition:height .35s ease;transition:height .35s ease}.collapse.in{height:auto}
.close{float:right;font-size:20px;font-weight:bold;line-height:20px;color:#000;text-shadow:0 1px 0 #fff;opacity:.2;filter:alpha(opacity=20)}.close:hover,.close:focus{color:#000;text-decoration:none;cursor:pointer;opacity:.4;filter:alpha(opacity=40)}
button.close{padding:0;cursor:pointer;background:transparent;border:0;-webkit-appearance:none}
.btn{display:inline-block;*display:inline;*zoom:1;padding:4px 12px;margin-bottom:0;font-size:13px;line-height:20px;text-align:center;vertical-align:middle;cursor:pointer;color:#333;text-shadow:0 1px 1px rgba(255,255,255,0.75);background-color:#f5f5f5;background-image:-moz-linear-gradient(top, #fff, #e6e6e6);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#fff), to(#e6e6e6));background-image:-webkit-linear-gradient(top, #fff, #e6e6e6);background-image:-o-linear-gradient(top, #fff, #e6e6e6);background-image:linear-gradient(to bottom, #fff, #e6e6e6);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#ffe6e6e6', GradientType=0);border-color:#e6e6e6 #e6e6e6 #bfbfbf;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#e6e6e6;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false);border:1px solid #ccc;*border:0;border-bottom-color:#b3b3b3;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;*margin-left:.3em;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);-moz-box-shadow:inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);box-shadow:inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05)}.btn:hover,.btn:focus,.btn:active,.btn.active,.btn.disabled,.btn[disabled]{color:#333;background-color:#e6e6e6;*background-color:#d9d9d9}
.btn:active,.btn.active{background-color:#ccc \9}
.btn:first-child{*margin-left:0}
.btn:hover,.btn:focus{color:#333;text-decoration:none;background-position:0 -15px;-webkit-transition:background-position .1s linear;-moz-transition:background-position .1s linear;-o-transition:background-position .1s linear;transition:background-position .1s linear}
.btn:focus{outline:thin dotted #333;outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}
.btn.active,.btn:active{background-image:none;outline:0;-webkit-box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);-moz-box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05)}
.btn.disabled,.btn[disabled]{cursor:default;background-image:none;opacity:.65;filter:alpha(opacity=65);-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none}
.btn-large{padding:11px 19px;font-size:16.25px;border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.btn-large [class^="icon-"],.btn-large [class*=" icon-"]{margin-top:4px}
.btn-small{padding:2px 10px;font-size:11.049999999999999px;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.btn-small [class^="icon-"],.btn-small [class*=" icon-"]{margin-top:0}
.btn-mini [class^="icon-"],.btn-mini [class*=" icon-"]{margin-top:-1px}
.btn-mini{padding:0 6px;font-size:9.75px;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.btn-block{display:block;width:100%;padding-left:0;padding-right:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}
.btn-block+.btn-block{margin-top:5px}
input[type="submit"].btn-block,input[type="reset"].btn-block,input[type="button"].btn-block{width:100%}
.btn-primary.active,.btn-warning.active,.btn-danger.active,.btn-success.active,.btn-info.active,.btn-inverse.active{color:rgba(255,255,255,0.75)}
.btn-primary{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#006dcc;background-image:-moz-linear-gradient(top, #08c, #04c);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#08c), to(#04c));background-image:-webkit-linear-gradient(top, #08c, #04c);background-image:-o-linear-gradient(top, #08c, #04c);background-image:linear-gradient(to bottom, #08c, #04c);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0044cc', GradientType=0);border-color:#04c #04c #002a80;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#04c;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-primary:hover,.btn-primary:focus,.btn-primary:active,.btn-primary.active,.btn-primary.disabled,.btn-primary[disabled]{color:#fff;background-color:#04c;*background-color:#003bb3}
.btn-primary:active,.btn-primary.active{background-color:#039 \9}
.btn-warning{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#faa732;background-image:-moz-linear-gradient(top, #fbb450, #f89406);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#fbb450), to(#f89406));background-image:-webkit-linear-gradient(top, #fbb450, #f89406);background-image:-o-linear-gradient(top, #fbb450, #f89406);background-image:linear-gradient(to bottom, #fbb450, #f89406);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffbb450', endColorstr='#fff89406', GradientType=0);border-color:#f89406 #f89406 #ad6704;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#f89406;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-warning:hover,.btn-warning:focus,.btn-warning:active,.btn-warning.active,.btn-warning.disabled,.btn-warning[disabled]{color:#fff;background-color:#f89406;*background-color:#df8505}
.btn-warning:active,.btn-warning.active{background-color:#c67605 \9}
.btn-danger{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#da4f49;background-image:-moz-linear-gradient(top, #ee5f5b, #bd362f);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#ee5f5b), to(#bd362f));background-image:-webkit-linear-gradient(top, #ee5f5b, #bd362f);background-image:-o-linear-gradient(top, #ee5f5b, #bd362f);background-image:linear-gradient(to bottom, #ee5f5b, #bd362f);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffee5f5b', endColorstr='#ffbd362f', GradientType=0);border-color:#bd362f #bd362f #802420;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#bd362f;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-danger:hover,.btn-danger:focus,.btn-danger:active,.btn-danger.active,.btn-danger.disabled,.btn-danger[disabled]{color:#fff;background-color:#bd362f;*background-color:#a9302a}
.btn-danger:active,.btn-danger.active{background-color:#942a25 \9}
.btn-success{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#5bb75b;background-image:-moz-linear-gradient(top, #62c462, #51a351);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#62c462), to(#51a351));background-image:-webkit-linear-gradient(top, #62c462, #51a351);background-image:-o-linear-gradient(top, #62c462, #51a351);background-image:linear-gradient(to bottom, #62c462, #51a351);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff62c462', endColorstr='#ff51a351', GradientType=0);border-color:#51a351 #51a351 #387038;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#51a351;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-success:hover,.btn-success:focus,.btn-success:active,.btn-success.active,.btn-success.disabled,.btn-success[disabled]{color:#fff;background-color:#51a351;*background-color:#499249}
.btn-success:active,.btn-success.active{background-color:#408140 \9}
.btn-info{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#49afcd;background-image:-moz-linear-gradient(top, #5bc0de, #2f96b4);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#5bc0de), to(#2f96b4));background-image:-webkit-linear-gradient(top, #5bc0de, #2f96b4);background-image:-o-linear-gradient(top, #5bc0de, #2f96b4);background-image:linear-gradient(to bottom, #5bc0de, #2f96b4);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff2f96b4', GradientType=0);border-color:#2f96b4 #2f96b4 #1f6377;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#2f96b4;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-info:hover,.btn-info:focus,.btn-info:active,.btn-info.active,.btn-info.disabled,.btn-info[disabled]{color:#fff;background-color:#2f96b4;*background-color:#2a85a0}
.btn-info:active,.btn-info.active{background-color:#24748c \9}
.btn-inverse{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#363636;background-image:-moz-linear-gradient(top, #444, #222);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#444), to(#222));background-image:-webkit-linear-gradient(top, #444, #222);background-image:-o-linear-gradient(top, #444, #222);background-image:linear-gradient(to bottom, #444, #222);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff444444', endColorstr='#ff222222', GradientType=0);border-color:#222 #222 #000;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#222;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.btn-inverse:hover,.btn-inverse:focus,.btn-inverse:active,.btn-inverse.active,.btn-inverse.disabled,.btn-inverse[disabled]{color:#fff;background-color:#222;*background-color:#151515}
.btn-inverse:active,.btn-inverse.active{background-color:#080808 \9}
button.btn,input[type="submit"].btn{*padding-top:3px;*padding-bottom:3px}button.btn::-moz-focus-inner,input[type="submit"].btn::-moz-focus-inner{padding:0;border:0}
button.btn.btn-large,input[type="submit"].btn.btn-large{*padding-top:7px;*padding-bottom:7px}
button.btn.btn-small,input[type="submit"].btn.btn-small{*padding-top:3px;*padding-bottom:3px}
button.btn.btn-mini,input[type="submit"].btn.btn-mini{*padding-top:1px;*padding-bottom:1px}
.btn-link,.btn-link:active,.btn-link[disabled]{background-color:transparent;background-image:none;-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none}
.btn-link{border-color:transparent;cursor:pointer;color:#08c;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.btn-link:hover,.btn-link:focus{color:#005580;text-decoration:underline;background-color:transparent}
.btn-link[disabled]:hover,.btn-link[disabled]:focus{color:#333;text-decoration:none}
.btn-group{position:relative;display:inline-block;*display:inline;*zoom:1;font-size:0;vertical-align:middle;white-space:nowrap;*margin-left:.3em}.btn-group:first-child{*margin-left:0}
.btn-group+.btn-group{margin-left:5px}
.btn-toolbar{font-size:0;margin-top:10px;margin-bottom:10px}.btn-toolbar>.btn+.btn,.btn-toolbar>.btn-group+.btn,.btn-toolbar>.btn+.btn-group{margin-left:5px}
.btn-group>.btn{position:relative;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.btn-group>.btn+.btn{margin-left:-1px}
.btn-group>.btn,.btn-group>.dropdown-menu,.btn-group>.popover{font-size:13px}
.btn-group>.btn-mini{font-size:9.75px}
.btn-group>.btn-small{font-size:11.049999999999999px}
.btn-group>.btn-large{font-size:16.25px}
.btn-group>.btn:first-child{margin-left:0;-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px;-webkit-border-bottom-left-radius:4px;-moz-border-radius-bottomleft:4px;border-bottom-left-radius:4px}
.btn-group>.btn:last-child,.btn-group>.dropdown-toggle{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px;-webkit-border-bottom-right-radius:4px;-moz-border-radius-bottomright:4px;border-bottom-right-radius:4px}
.btn-group>.btn.large:first-child{margin-left:0;-webkit-border-top-left-radius:6px;-moz-border-radius-topleft:6px;border-top-left-radius:6px;-webkit-border-bottom-left-radius:6px;-moz-border-radius-bottomleft:6px;border-bottom-left-radius:6px}
.btn-group>.btn.large:last-child,.btn-group>.large.dropdown-toggle{-webkit-border-top-right-radius:6px;-moz-border-radius-topright:6px;border-top-right-radius:6px;-webkit-border-bottom-right-radius:6px;-moz-border-radius-bottomright:6px;border-bottom-right-radius:6px}
.btn-group>.btn:hover,.btn-group>.btn:focus,.btn-group>.btn:active,.btn-group>.btn.active{z-index:2}
.btn-group .dropdown-toggle:active,.btn-group.open .dropdown-toggle{outline:0}
.btn-group>.btn+.dropdown-toggle{padding-left:8px;padding-right:8px;-webkit-box-shadow:inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);-moz-box-shadow:inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);box-shadow:inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);*padding-top:5px;*padding-bottom:5px}
.btn-group>.btn-mini+.dropdown-toggle{padding-left:5px;padding-right:5px;*padding-top:2px;*padding-bottom:2px}
.btn-group>.btn-small+.dropdown-toggle{*padding-top:5px;*padding-bottom:4px}
.btn-group>.btn-large+.dropdown-toggle{padding-left:12px;padding-right:12px;*padding-top:7px;*padding-bottom:7px}
.btn-group.open .dropdown-toggle{background-image:none;-webkit-box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);-moz-box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);box-shadow:inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05)}
.btn-group.open .btn.dropdown-toggle{background-color:#e6e6e6}
.btn-group.open .btn-primary.dropdown-toggle{background-color:#04c}
.btn-group.open .btn-warning.dropdown-toggle{background-color:#f89406}
.btn-group.open .btn-danger.dropdown-toggle{background-color:#bd362f}
.btn-group.open .btn-success.dropdown-toggle{background-color:#51a351}
.btn-group.open .btn-info.dropdown-toggle{background-color:#2f96b4}
.btn-group.open .btn-inverse.dropdown-toggle{background-color:#222}
.btn .caret{margin-top:8px;margin-left:0}
.btn-large .caret{margin-top:6px}
.btn-large .caret{border-left-width:5px;border-right-width:5px;border-top-width:5px}
.btn-mini .caret,.btn-small .caret{margin-top:8px}
.dropup .btn-large .caret{border-bottom-width:5px}
.btn-primary .caret,.btn-warning .caret,.btn-danger .caret,.btn-info .caret,.btn-success .caret,.btn-inverse .caret{border-top-color:#fff;border-bottom-color:#fff}
.btn-group-vertical{display:inline-block;*display:inline;*zoom:1}
.btn-group-vertical>.btn{display:block;float:none;max-width:100%;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.btn-group-vertical>.btn+.btn{margin-left:0;margin-top:-1px}
.btn-group-vertical>.btn:first-child{border-radius:4px 4px 0 0;-webkit-border-radius:4px 4px 0 0;-moz-border-radius:4px 4px 0 0;border-radius:4px 4px 0 0}
.btn-group-vertical>.btn:last-child{border-radius:0 0 4px 4px;-webkit-border-radius:0 0 4px 4px;-moz-border-radius:0 0 4px 4px;border-radius:0 0 4px 4px}
.btn-group-vertical>.btn-large:first-child{border-radius:6px 6px 0 0;-webkit-border-radius:6px 6px 0 0;-moz-border-radius:6px 6px 0 0;border-radius:6px 6px 0 0}
.btn-group-vertical>.btn-large:last-child{border-radius:0 0 6px 6px;-webkit-border-radius:0 0 6px 6px;-moz-border-radius:0 0 6px 6px;border-radius:0 0 6px 6px}
.alert{padding:8px 35px 8px 14px;margin-bottom:20px;text-shadow:0 1px 0 rgba(255,255,255,0.5);background-color:#fcf8e3;border:1px solid #fbeed5;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.alert,.alert h4{color:#c09853}
.alert h4{margin:0}
.alert .close{position:relative;top:-2px;right:-21px;line-height:20px}
.alert-success{background-color:#dff0d8;border-color:#d6e9c6;color:#468847}
.alert-success h4{color:#468847}
.alert-danger,.alert-error{background-color:#f2dede;border-color:#eed3d7;color:#b94a48}
.alert-danger h4,.alert-error h4{color:#b94a48}
.alert-info{background-color:#d9edf7;border-color:#bce8f1;color:#3a87ad}
.alert-info h4{color:#3a87ad}
.alert-block{padding-top:14px;padding-bottom:14px}
.alert-block>p,.alert-block>ul{margin-bottom:0}
.alert-block p+p{margin-top:5px}
.nav{margin-left:0;margin-bottom:20px;list-style:none}
.nav>li>a{display:block}
.nav>li>a:hover,.nav>li>a:focus{text-decoration:none;background-color:#eee}
.nav>li>a>img{max-width:none}
.nav>.pull-right{float:right}
.nav-header{display:block;padding:3px 15px;font-size:11px;font-weight:bold;line-height:20px;color:#999;text-shadow:0 1px 0 rgba(255,255,255,0.5);text-transform:uppercase}
.nav li+.nav-header{margin-top:9px}
.nav-list{padding-left:15px;padding-right:15px;margin-bottom:0}
.nav-list>li>a,.nav-list .nav-header{margin-left:-15px;margin-right:-15px;text-shadow:0 1px 0 rgba(255,255,255,0.5)}
.nav-list>li>a{padding:3px 15px}
.nav-list>.active>a,.nav-list>.active>a:hover,.nav-list>.active>a:focus{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.2);background-color:#08c}
.nav-list [class^="icon-"],.nav-list [class*=" icon-"]{margin-right:2px}
.nav-list .divider{*width:100%;height:1px;margin:9px 1px;*margin:-5px 0 5px;overflow:hidden;background-color:#e5e5e5;border-bottom:1px solid #fff}
.nav-tabs,.nav-pills{*zoom:1}.nav-tabs:before,.nav-pills:before,.nav-tabs:after,.nav-pills:after{display:table;content:"";line-height:0}
.nav-tabs:after,.nav-pills:after{clear:both}
.nav-tabs>li,.nav-pills>li{float:left}
.nav-tabs>li>a,.nav-pills>li>a{padding-right:12px;padding-left:12px;margin-right:2px;line-height:14px}
.nav-tabs{border-bottom:1px solid #ddd}
.nav-tabs>li{margin-bottom:-1px}
.nav-tabs>li>a{padding-top:8px;padding-bottom:8px;line-height:20px;border:1px solid transparent;border-radius:4px 4px 0 0;-webkit-border-radius:4px 4px 0 0;-moz-border-radius:4px 4px 0 0;border-radius:4px 4px 0 0}.nav-tabs>li>a:hover,.nav-tabs>li>a:focus{border-color:#eee #eee #ddd}
.nav-tabs>.active>a,.nav-tabs>.active>a:hover,.nav-tabs>.active>a:focus{color:#555;background-color:#fff;border:1px solid #ddd;border-bottom-color:transparent;cursor:default}
.nav-pills>li>a{padding-top:8px;padding-bottom:8px;margin-top:2px;margin-bottom:2px;border-radius:5px;-webkit-border-radius:5px;-moz-border-radius:5px;border-radius:5px}
.nav-pills>.active>a,.nav-pills>.active>a:hover,.nav-pills>.active>a:focus{color:#fff;background-color:#08c}
.nav-stacked>li{float:none}
.nav-stacked>li>a{margin-right:0}
.nav-tabs.nav-stacked{border-bottom:0}
.nav-tabs.nav-stacked>li>a{border:1px solid #ddd;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.nav-tabs.nav-stacked>li:first-child>a{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px;-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px}
.nav-tabs.nav-stacked>li:last-child>a{-webkit-border-bottom-right-radius:4px;-moz-border-radius-bottomright:4px;border-bottom-right-radius:4px;-webkit-border-bottom-left-radius:4px;-moz-border-radius-bottomleft:4px;border-bottom-left-radius:4px}
.nav-tabs.nav-stacked>li>a:hover,.nav-tabs.nav-stacked>li>a:focus{border-color:#ddd;z-index:2}
.nav-pills.nav-stacked>li>a{margin-bottom:3px}
.nav-pills.nav-stacked>li:last-child>a{margin-bottom:1px}
.nav-tabs .dropdown-menu{border-radius:0 0 6px 6px;-webkit-border-radius:0 0 6px 6px;-moz-border-radius:0 0 6px 6px;border-radius:0 0 6px 6px}
.nav-pills .dropdown-menu{border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.nav .dropdown-toggle .caret{border-top-color:#08c;border-bottom-color:#08c;margin-top:6px}
.nav .dropdown-toggle:hover .caret,.nav .dropdown-toggle:focus .caret{border-top-color:#005580;border-bottom-color:#005580}
.nav-tabs .dropdown-toggle .caret{margin-top:8px}
.nav .active .dropdown-toggle .caret{border-top-color:#fff;border-bottom-color:#fff}
.nav-tabs .active .dropdown-toggle .caret{border-top-color:#555;border-bottom-color:#555}
.nav>.dropdown.active>a:hover,.nav>.dropdown.active>a:focus{cursor:pointer}
.nav-tabs .open .dropdown-toggle,.nav-pills .open .dropdown-toggle,.nav>li.dropdown.open.active>a:hover,.nav>li.dropdown.open.active>a:focus{color:#fff;background-color:#999;border-color:#999}
.nav li.dropdown.open .caret,.nav li.dropdown.open.active .caret,.nav li.dropdown.open a:hover .caret,.nav li.dropdown.open a:focus .caret{border-top-color:#fff;border-bottom-color:#fff;opacity:1;filter:alpha(opacity=100)}
.tabs-stacked .open>a:hover,.tabs-stacked .open>a:focus{border-color:#999}
.tabbable{*zoom:1}.tabbable:before,.tabbable:after{display:table;content:"";line-height:0}
.tabbable:after{clear:both}
.tab-content{overflow:auto}
.tabs-below>.nav-tabs,.tabs-right>.nav-tabs,.tabs-left>.nav-tabs{border-bottom:0}
.tab-content>.tab-pane,.pill-content>.pill-pane{display:none}
.tab-content>.active,.pill-content>.active{display:block}
.tabs-below>.nav-tabs{border-top:1px solid #ddd}
.tabs-below>.nav-tabs>li{margin-top:-1px;margin-bottom:0}
.tabs-below>.nav-tabs>li>a{border-radius:0 0 4px 4px;-webkit-border-radius:0 0 4px 4px;-moz-border-radius:0 0 4px 4px;border-radius:0 0 4px 4px}.tabs-below>.nav-tabs>li>a:hover,.tabs-below>.nav-tabs>li>a:focus{border-bottom-color:transparent;border-top-color:#ddd}
.tabs-below>.nav-tabs>.active>a,.tabs-below>.nav-tabs>.active>a:hover,.tabs-below>.nav-tabs>.active>a:focus{border-color:transparent #ddd #ddd #ddd}
.tabs-left>.nav-tabs>li,.tabs-right>.nav-tabs>li{float:none}
.tabs-left>.nav-tabs>li>a,.tabs-right>.nav-tabs>li>a{min-width:74px;margin-right:0;margin-bottom:3px}
.tabs-left>.nav-tabs{float:left;margin-right:19px;border-right:1px solid #ddd}
.tabs-left>.nav-tabs>li>a{margin-right:-1px;border-radius:4px 0 0 4px;-webkit-border-radius:4px 0 0 4px;-moz-border-radius:4px 0 0 4px;border-radius:4px 0 0 4px}
.tabs-left>.nav-tabs>li>a:hover,.tabs-left>.nav-tabs>li>a:focus{border-color:#eee #ddd #eee #eee}
.tabs-left>.nav-tabs .active>a,.tabs-left>.nav-tabs .active>a:hover,.tabs-left>.nav-tabs .active>a:focus{border-color:#ddd transparent #ddd #ddd;*border-right-color:#fff}
.tabs-right>.nav-tabs{float:right;margin-left:19px;border-left:1px solid #ddd}
.tabs-right>.nav-tabs>li>a{margin-left:-1px;border-radius:0 4px 4px 0;-webkit-border-radius:0 4px 4px 0;-moz-border-radius:0 4px 4px 0;border-radius:0 4px 4px 0}
.tabs-right>.nav-tabs>li>a:hover,.tabs-right>.nav-tabs>li>a:focus{border-color:#eee #eee #eee #ddd}
.tabs-right>.nav-tabs .active>a,.tabs-right>.nav-tabs .active>a:hover,.tabs-right>.nav-tabs .active>a:focus{border-color:#ddd #ddd #ddd transparent;*border-left-color:#fff}
.nav>.disabled>a{color:#999}
.nav>.disabled>a:hover,.nav>.disabled>a:focus{text-decoration:none;background-color:transparent;cursor:default}
.navbar{overflow:visible;margin-bottom:20px;*position:relative;*z-index:2}
.navbar-inner{min-height:36px;padding-left:20px;padding-right:20px;background-color:#fafafa;background-image:-moz-linear-gradient(top, #fff, #f2f2f2);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#fff), to(#f2f2f2));background-image:-webkit-linear-gradient(top, #fff, #f2f2f2);background-image:-o-linear-gradient(top, #fff, #f2f2f2);background-image:linear-gradient(to bottom, #fff, #f2f2f2);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#fff2f2f2', GradientType=0);border:1px solid #d4d4d4;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;-webkit-box-shadow:0 1px 4px rgba(0,0,0,0.065);-moz-box-shadow:0 1px 4px rgba(0,0,0,0.065);box-shadow:0 1px 4px rgba(0,0,0,0.065);*zoom:1}.navbar-inner:before,.navbar-inner:after{display:table;content:"";line-height:0}
.navbar-inner:after{clear:both}
.navbar .container{width:auto}
.nav-collapse.collapse{height:auto;overflow:visible}
.navbar .brand{float:left;display:block;padding:8px 20px 8px;margin-left:-20px;font-size:20px;font-weight:200;color:#777;text-shadow:0 1px 0 #fff}.navbar .brand:hover,.navbar .brand:focus{text-decoration:none}
.navbar-text{margin-bottom:0;line-height:36px;color:#777}
.navbar-link{color:#777}.navbar-link:hover,.navbar-link:focus{color:#333}
.navbar .divider-vertical{height:36px;margin:0 9px;border-left:1px solid #f2f2f2;border-right:1px solid #fff}
.navbar .btn,.navbar .btn-group{margin-top:3px}
.navbar .btn-group .btn,.navbar .input-prepend .btn,.navbar .input-append .btn,.navbar .input-prepend .btn-group,.navbar .input-append .btn-group{margin-top:0}
.navbar-form{margin-bottom:0;*zoom:1}.navbar-form:before,.navbar-form:after{display:table;content:"";line-height:0}
.navbar-form:after{clear:both}
.navbar-form input,.navbar-form select,.navbar-form .radio,.navbar-form .checkbox{margin-top:3px}
.navbar-form input,.navbar-form select,.navbar-form .btn{display:inline-block;margin-bottom:0}
.navbar-form input[type="image"],.navbar-form input[type="checkbox"],.navbar-form input[type="radio"]{margin-top:3px}
.navbar-form .input-append,.navbar-form .input-prepend{margin-top:5px;white-space:nowrap}.navbar-form .input-append input,.navbar-form .input-prepend input{margin-top:0}
.navbar-search{position:relative;float:left;margin-top:3px;margin-bottom:0}.navbar-search .search-query{margin-bottom:0;padding:4px 14px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:13px;font-weight:normal;line-height:1;border-radius:15px;-webkit-border-radius:15px;-moz-border-radius:15px;border-radius:15px}
.navbar-static-top{position:static;margin-bottom:0}.navbar-static-top .navbar-inner{border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.navbar-fixed-top,.navbar-fixed-bottom{position:fixed;right:0;left:0;z-index:1030;margin-bottom:0}
.navbar-fixed-top .navbar-inner,.navbar-static-top .navbar-inner{border-width:0 0 1px}
.navbar-fixed-bottom .navbar-inner{border-width:1px 0 0}
.navbar-fixed-top .navbar-inner,.navbar-fixed-bottom .navbar-inner{padding-left:0;padding-right:0;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
.navbar-static-top .container,.navbar-fixed-top .container,.navbar-fixed-bottom .container{width:940px}
.navbar-fixed-top{top:0}
.navbar-fixed-top .navbar-inner,.navbar-static-top .navbar-inner{-webkit-box-shadow:0 1px 10px rgba(0,0,0,.1);-moz-box-shadow:0 1px 10px rgba(0,0,0,.1);box-shadow:0 1px 10px rgba(0,0,0,.1)}
.navbar-fixed-bottom{bottom:0}.navbar-fixed-bottom .navbar-inner{-webkit-box-shadow:0 -1px 10px rgba(0,0,0,.1);-moz-box-shadow:0 -1px 10px rgba(0,0,0,.1);box-shadow:0 -1px 10px rgba(0,0,0,.1)}
.navbar .nav{position:relative;left:0;display:block;float:left;margin:0 10px 0 0}
.navbar .nav.pull-right{float:right;margin-right:0}
.navbar .nav>li{float:left}
.navbar .nav>li>a{float:none;padding:8px 15px 8px;color:#777;text-decoration:none;text-shadow:0 1px 0 #fff}
.navbar .nav .dropdown-toggle .caret{margin-top:8px}
.navbar .nav>li>a:focus,.navbar .nav>li>a:hover{background-color:transparent;color:#333;text-decoration:none}
.navbar .nav>.active>a,.navbar .nav>.active>a:hover,.navbar .nav>.active>a:focus{color:#555;text-decoration:none;background-color:#e5e5e5;-webkit-box-shadow:inset 0 3px 8px rgba(0,0,0,0.125);-moz-box-shadow:inset 0 3px 8px rgba(0,0,0,0.125);box-shadow:inset 0 3px 8px rgba(0,0,0,0.125)}
.navbar .btn-navbar{display:none;float:right;padding:7px 10px;margin-left:5px;margin-right:5px;color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#ededed;background-image:-moz-linear-gradient(top, #f2f2f2, #e5e5e5);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#f2f2f2), to(#e5e5e5));background-image:-webkit-linear-gradient(top, #f2f2f2, #e5e5e5);background-image:-o-linear-gradient(top, #f2f2f2, #e5e5e5);background-image:linear-gradient(to bottom, #f2f2f2, #e5e5e5);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2f2f2', endColorstr='#ffe5e5e5', GradientType=0);border-color:#e5e5e5 #e5e5e5 #bfbfbf;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#e5e5e5;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false);-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075);-moz-box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075);box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075)}.navbar .btn-navbar:hover,.navbar .btn-navbar:focus,.navbar .btn-navbar:active,.navbar .btn-navbar.active,.navbar .btn-navbar.disabled,.navbar .btn-navbar[disabled]{color:#fff;background-color:#e5e5e5;*background-color:#d9d9d9}
.navbar .btn-navbar:active,.navbar .btn-navbar.active{background-color:#ccc \9}
.navbar .btn-navbar .icon-bar{display:block;width:18px;height:2px;background-color:#f5f5f5;-webkit-border-radius:1px;-moz-border-radius:1px;border-radius:1px;-webkit-box-shadow:0 1px 0 rgba(0,0,0,0.25);-moz-box-shadow:0 1px 0 rgba(0,0,0,0.25);box-shadow:0 1px 0 rgba(0,0,0,0.25)}
.btn-navbar .icon-bar+.icon-bar{margin-top:3px}
.navbar .nav>li>.dropdown-menu:before{content:'';display:inline-block;border-left:7px solid transparent;border-right:7px solid transparent;border-bottom:7px solid #ccc;border-bottom-color:rgba(0,0,0,0.2);position:absolute;top:-7px;left:9px}
.navbar .nav>li>.dropdown-menu:after{content:'';display:inline-block;border-left:6px solid transparent;border-right:6px solid transparent;border-bottom:6px solid #fff;position:absolute;top:-6px;left:10px}
.navbar-fixed-bottom .nav>li>.dropdown-menu:before{border-top:7px solid #ccc;border-top-color:rgba(0,0,0,0.2);border-bottom:0;bottom:-7px;top:auto}
.navbar-fixed-bottom .nav>li>.dropdown-menu:after{border-top:6px solid #fff;border-bottom:0;bottom:-6px;top:auto}
.navbar .nav li.dropdown>a:hover .caret,.navbar .nav li.dropdown>a:focus .caret{border-top-color:#333;border-bottom-color:#333}
.navbar .nav li.dropdown.open>.dropdown-toggle,.navbar .nav li.dropdown.active>.dropdown-toggle,.navbar .nav li.dropdown.open.active>.dropdown-toggle{background-color:#e5e5e5;color:#555}
.navbar .nav li.dropdown>.dropdown-toggle .caret{border-top-color:#777;border-bottom-color:#777}
.navbar .nav li.dropdown.open>.dropdown-toggle .caret,.navbar .nav li.dropdown.active>.dropdown-toggle .caret,.navbar .nav li.dropdown.open.active>.dropdown-toggle .caret{border-top-color:#555;border-bottom-color:#555}
.navbar .pull-right>li>.dropdown-menu,.navbar .nav>li>.dropdown-menu.pull-right{left:auto;right:0}.navbar .pull-right>li>.dropdown-menu:before,.navbar .nav>li>.dropdown-menu.pull-right:before{left:auto;right:12px}
.navbar .pull-right>li>.dropdown-menu:after,.navbar .nav>li>.dropdown-menu.pull-right:after{left:auto;right:13px}
.navbar .pull-right>li>.dropdown-menu .dropdown-menu,.navbar .nav>li>.dropdown-menu.pull-right .dropdown-menu{left:auto;right:100%;margin-left:0;margin-right:-1px;border-radius:6px 0 6px 6px;-webkit-border-radius:6px 0 6px 6px;-moz-border-radius:6px 0 6px 6px;border-radius:6px 0 6px 6px}
.navbar-inverse .navbar-inner{background-color:#1b1b1b;background-image:-moz-linear-gradient(top, #222, #111);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#222), to(#111));background-image:-webkit-linear-gradient(top, #222, #111);background-image:-o-linear-gradient(top, #222, #111);background-image:linear-gradient(to bottom, #222, #111);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff222222', endColorstr='#ff111111', GradientType=0);border-color:#252525}
.navbar-inverse .brand,.navbar-inverse .nav>li>a{color:#999;text-shadow:0 -1px 0 rgba(0,0,0,0.25)}.navbar-inverse .brand:hover,.navbar-inverse .nav>li>a:hover,.navbar-inverse .brand:focus,.navbar-inverse .nav>li>a:focus{color:#fff}
.navbar-inverse .brand{color:#999}
.navbar-inverse .navbar-text{color:#999}
.navbar-inverse .nav>li>a:focus,.navbar-inverse .nav>li>a:hover{background-color:transparent;color:#fff}
.navbar-inverse .nav .active>a,.navbar-inverse .nav .active>a:hover,.navbar-inverse .nav .active>a:focus{color:#fff;background-color:#111}
.navbar-inverse .navbar-link{color:#999}.navbar-inverse .navbar-link:hover,.navbar-inverse .navbar-link:focus{color:#fff}
.navbar-inverse .divider-vertical{border-left-color:#111;border-right-color:#222}
.navbar-inverse .nav li.dropdown.open>.dropdown-toggle,.navbar-inverse .nav li.dropdown.active>.dropdown-toggle,.navbar-inverse .nav li.dropdown.open.active>.dropdown-toggle{background-color:#111;color:#fff}
.navbar-inverse .nav li.dropdown>a:hover .caret,.navbar-inverse .nav li.dropdown>a:focus .caret{border-top-color:#fff;border-bottom-color:#fff}
.navbar-inverse .nav li.dropdown>.dropdown-toggle .caret{border-top-color:#999;border-bottom-color:#999}
.navbar-inverse .nav li.dropdown.open>.dropdown-toggle .caret,.navbar-inverse .nav li.dropdown.active>.dropdown-toggle .caret,.navbar-inverse .nav li.dropdown.open.active>.dropdown-toggle .caret{border-top-color:#fff;border-bottom-color:#fff}
.navbar-inverse .navbar-search .search-query{color:#fff;background-color:#515151;border-color:#111;-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);box-shadow:inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);-webkit-transition:none;-moz-transition:none;-o-transition:none;transition:none}.navbar-inverse .navbar-search .search-query:-moz-placeholder{color:#ccc}
.navbar-inverse .navbar-search .search-query:-ms-input-placeholder{color:#ccc}
.navbar-inverse .navbar-search .search-query::-webkit-input-placeholder{color:#ccc}
.navbar-inverse .navbar-search .search-query:focus,.navbar-inverse .navbar-search .search-query.focused{padding:5px 15px;color:#333;text-shadow:0 1px 0 #fff;background-color:#fff;border:0;-webkit-box-shadow:0 0 3px rgba(0,0,0,0.15);-moz-box-shadow:0 0 3px rgba(0,0,0,0.15);box-shadow:0 0 3px rgba(0,0,0,0.15);outline:0}
.navbar-inverse .btn-navbar{color:#fff;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#0e0e0e;background-image:-moz-linear-gradient(top, #151515, #040404);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#151515), to(#040404));background-image:-webkit-linear-gradient(top, #151515, #040404);background-image:-o-linear-gradient(top, #151515, #040404);background-image:linear-gradient(to bottom, #151515, #040404);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff151515', endColorstr='#ff040404', GradientType=0);border-color:#040404 #040404 #000;border-color:rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.25);*background-color:#040404;filter:progid:DXImageTransform.Microsoft.gradient(enabled = false)}.navbar-inverse .btn-navbar:hover,.navbar-inverse .btn-navbar:focus,.navbar-inverse .btn-navbar:active,.navbar-inverse .btn-navbar.active,.navbar-inverse .btn-navbar.disabled,.navbar-inverse .btn-navbar[disabled]{color:#fff;background-color:#040404;*background-color:#000}
.navbar-inverse .btn-navbar:active,.navbar-inverse .btn-navbar.active{background-color:#000 \9}
.breadcrumb{padding:8px 15px;margin:0 0 20px;list-style:none;background-color:#f5f5f5;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}.breadcrumb>li{display:inline-block;*display:inline;*zoom:1;text-shadow:0 1px 0 #fff}.breadcrumb>li>.divider{padding:0 5px;color:#ccc}
.breadcrumb>.active{color:#999}
.pagination{margin:20px 0}
.pagination ul{display:inline-block;*display:inline;*zoom:1;margin-left:0;margin-bottom:0;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;-webkit-box-shadow:0 1px 2px rgba(0,0,0,0.05);-moz-box-shadow:0 1px 2px rgba(0,0,0,0.05);box-shadow:0 1px 2px rgba(0,0,0,0.05)}
.pagination ul>li{display:inline}
.pagination ul>li>a,.pagination ul>li>span{float:left;padding:4px 12px;line-height:20px;text-decoration:none;background-color:#fff;border:1px solid #ddd;border-left-width:0}
.pagination ul>li>a:hover,.pagination ul>li>a:focus,.pagination ul>.active>a,.pagination ul>.active>span{background-color:#f5f5f5}
.pagination ul>.active>a,.pagination ul>.active>span{color:#999;cursor:default}
.pagination ul>.disabled>span,.pagination ul>.disabled>a,.pagination ul>.disabled>a:hover,.pagination ul>.disabled>a:focus{color:#999;background-color:transparent;cursor:default}
.pagination ul>li:first-child>a,.pagination ul>li:first-child>span{border-left-width:1px;-webkit-border-top-left-radius:4px;-moz-border-radius-topleft:4px;border-top-left-radius:4px;-webkit-border-bottom-left-radius:4px;-moz-border-radius-bottomleft:4px;border-bottom-left-radius:4px}
.pagination ul>li:last-child>a,.pagination ul>li:last-child>span{-webkit-border-top-right-radius:4px;-moz-border-radius-topright:4px;border-top-right-radius:4px;-webkit-border-bottom-right-radius:4px;-moz-border-radius-bottomright:4px;border-bottom-right-radius:4px}
.pagination-centered{text-align:center}
.pagination-right{text-align:right}
.pagination-large ul>li>a,.pagination-large ul>li>span{padding:11px 19px;font-size:16.25px}
.pagination-large ul>li:first-child>a,.pagination-large ul>li:first-child>span{-webkit-border-top-left-radius:6px;-moz-border-radius-topleft:6px;border-top-left-radius:6px;-webkit-border-bottom-left-radius:6px;-moz-border-radius-bottomleft:6px;border-bottom-left-radius:6px}
.pagination-large ul>li:last-child>a,.pagination-large ul>li:last-child>span{-webkit-border-top-right-radius:6px;-moz-border-radius-topright:6px;border-top-right-radius:6px;-webkit-border-bottom-right-radius:6px;-moz-border-radius-bottomright:6px;border-bottom-right-radius:6px}
.pagination-mini ul>li:first-child>a,.pagination-small ul>li:first-child>a,.pagination-mini ul>li:first-child>span,.pagination-small ul>li:first-child>span{-webkit-border-top-left-radius:3px;-moz-border-radius-topleft:3px;border-top-left-radius:3px;-webkit-border-bottom-left-radius:3px;-moz-border-radius-bottomleft:3px;border-bottom-left-radius:3px}
.pagination-mini ul>li:last-child>a,.pagination-small ul>li:last-child>a,.pagination-mini ul>li:last-child>span,.pagination-small ul>li:last-child>span{-webkit-border-top-right-radius:3px;-moz-border-radius-topright:3px;border-top-right-radius:3px;-webkit-border-bottom-right-radius:3px;-moz-border-radius-bottomright:3px;border-bottom-right-radius:3px}
.pagination-small ul>li>a,.pagination-small ul>li>span{padding:2px 10px;font-size:11.049999999999999px}
.pagination-mini ul>li>a,.pagination-mini ul>li>span{padding:0 6px;font-size:9.75px}
.pager{margin:20px 0;list-style:none;text-align:center;*zoom:1}.pager:before,.pager:after{display:table;content:"";line-height:0}
.pager:after{clear:both}
.pager li{display:inline}
.pager li>a,.pager li>span{display:inline-block;padding:5px 14px;background-color:#fff;border:1px solid #ddd;border-radius:15px;-webkit-border-radius:15px;-moz-border-radius:15px;border-radius:15px}
.pager li>a:hover,.pager li>a:focus{text-decoration:none;background-color:#f5f5f5}
.pager .next>a,.pager .next>span{float:right}
.pager .previous>a,.pager .previous>span{float:left}
.pager .disabled>a,.pager .disabled>a:hover,.pager .disabled>a:focus,.pager .disabled>span{color:#999;background-color:#fff;cursor:default}
.modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000}.modal-backdrop.fade{opacity:0}
.modal-backdrop,.modal-backdrop.fade.in{opacity:.8;filter:alpha(opacity=80)}
.modal{position:fixed;top:10%;left:50%;z-index:1050;width:560px;margin-left:-280px;background-color:#fff;border:1px solid #999;border:1px solid rgba(0,0,0,0.3);*border:1px solid #999;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px;-webkit-box-shadow:0 3px 7px rgba(0,0,0,0.3);-moz-box-shadow:0 3px 7px rgba(0,0,0,0.3);box-shadow:0 3px 7px rgba(0,0,0,0.3);-webkit-background-clip:padding-box;-moz-background-clip:padding-box;background-clip:padding-box;outline:none}.modal.fade{-webkit-transition:opacity .3s linear, top .3s ease-out;-moz-transition:opacity .3s linear, top .3s ease-out;-o-transition:opacity .3s linear, top .3s ease-out;transition:opacity .3s linear, top .3s ease-out;top:-25%}
.modal.fade.in{top:10%}
.modal-header{padding:9px 15px;border-bottom:1px solid #eee}.modal-header .close{margin-top:2px}
.modal-header h3{margin:0;line-height:30px}
.modal-body{position:relative;overflow-y:auto;max-height:400px;padding:15px}
.modal-form{margin-bottom:0}
.modal-footer{padding:14px 15px 15px;margin-bottom:0;text-align:right;background-color:#f5f5f5;border-top:1px solid #ddd;-webkit-border-radius:0 0 6px 6px;-moz-border-radius:0 0 6px 6px;border-radius:0 0 6px 6px;-webkit-box-shadow:inset 0 1px 0 #fff;-moz-box-shadow:inset 0 1px 0 #fff;box-shadow:inset 0 1px 0 #fff;*zoom:1}.modal-footer:before,.modal-footer:after{display:table;content:"";line-height:0}
.modal-footer:after{clear:both}
.modal-footer .btn+.btn{margin-left:5px;margin-bottom:0}
.modal-footer .btn-group .btn+.btn{margin-left:-1px}
.modal-footer .btn-block+.btn-block{margin-left:0}
.tooltip{position:absolute;z-index:1030;display:block;visibility:visible;font-size:11px;line-height:1.4;opacity:0;filter:alpha(opacity=0)}.tooltip.in{opacity:.8;filter:alpha(opacity=80)}
.tooltip.top{margin-top:-3px;padding:5px 0}
.tooltip.right{margin-left:3px;padding:0 5px}
.tooltip.bottom{margin-top:3px;padding:5px 0}
.tooltip.left{margin-left:-3px;padding:0 5px}
.tooltip-inner{max-width:200px;padding:8px;color:#fff;text-align:center;text-decoration:none;background-color:#000;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.tooltip-arrow{position:absolute;width:0;height:0;border-color:transparent;border-style:solid}
.tooltip.top .tooltip-arrow{bottom:0;left:50%;margin-left:-5px;border-width:5px 5px 0;border-top-color:#000}
.tooltip.right .tooltip-arrow{top:50%;left:0;margin-top:-5px;border-width:5px 5px 5px 0;border-right-color:#000}
.tooltip.left .tooltip-arrow{top:50%;right:0;margin-top:-5px;border-width:5px 0 5px 5px;border-left-color:#000}
.tooltip.bottom .tooltip-arrow{top:0;left:50%;margin-left:-5px;border-width:0 5px 5px;border-bottom-color:#000}
.popover{position:absolute;top:0;left:0;z-index:1010;display:none;max-width:276px;padding:1px;text-align:left;background-color:#fff;-webkit-background-clip:padding-box;-moz-background-clip:padding;background-clip:padding-box;border:1px solid #ccc;border:1px solid rgba(0,0,0,0.2);-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px;-webkit-box-shadow:0 5px 10px rgba(0,0,0,0.2);-moz-box-shadow:0 5px 10px rgba(0,0,0,0.2);box-shadow:0 5px 10px rgba(0,0,0,0.2);white-space:normal}.popover.top{margin-top:-10px}
.popover.right{margin-left:10px}
.popover.bottom{margin-top:10px}
.popover.left{margin-left:-10px}
.popover-title{margin:0;padding:8px 14px;font-size:14px;font-weight:normal;line-height:18px;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;border-radius:5px 5px 0 0;-webkit-border-radius:5px 5px 0 0;-moz-border-radius:5px 5px 0 0;border-radius:5px 5px 0 0}.popover-title:empty{display:none}
.popover-content{padding:9px 14px}
.popover .arrow,.popover .arrow:after{position:absolute;display:block;width:0;height:0;border-color:transparent;border-style:solid}
.popover .arrow{border-width:11px}
.popover .arrow:after{border-width:10px;content:""}
.popover.top .arrow{left:50%;margin-left:-11px;border-bottom-width:0;border-top-color:#999;border-top-color:rgba(0,0,0,0.25);bottom:-11px}.popover.top .arrow:after{bottom:1px;margin-left:-10px;border-bottom-width:0;border-top-color:#fff}
.popover.right .arrow{top:50%;left:-11px;margin-top:-11px;border-left-width:0;border-right-color:#999;border-right-color:rgba(0,0,0,0.25)}.popover.right .arrow:after{left:1px;bottom:-10px;border-left-width:0;border-right-color:#fff}
.popover.bottom .arrow{left:50%;margin-left:-11px;border-top-width:0;border-bottom-color:#999;border-bottom-color:rgba(0,0,0,0.25);top:-11px}.popover.bottom .arrow:after{top:1px;margin-left:-10px;border-top-width:0;border-bottom-color:#fff}
.popover.left .arrow{top:50%;right:-11px;margin-top:-11px;border-right-width:0;border-left-color:#999;border-left-color:rgba(0,0,0,0.25)}.popover.left .arrow:after{right:1px;border-right-width:0;border-left-color:#fff;bottom:-10px}
.thumbnails{margin-left:-20px;list-style:none;*zoom:1}.thumbnails:before,.thumbnails:after{display:table;content:"";line-height:0}
.thumbnails:after{clear:both}
.row-fluid .thumbnails{margin-left:0}
.thumbnails>li{float:left;margin-bottom:20px;margin-left:20px}
.thumbnail{display:block;padding:4px;line-height:20px;border:1px solid #ddd;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px;-webkit-box-shadow:0 1px 3px rgba(0,0,0,0.055);-moz-box-shadow:0 1px 3px rgba(0,0,0,0.055);box-shadow:0 1px 3px rgba(0,0,0,0.055);-webkit-transition:all .2s ease-in-out;-moz-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;transition:all .2s ease-in-out}
a.thumbnail:hover,a.thumbnail:focus{border-color:#08c;-webkit-box-shadow:0 1px 4px rgba(0,105,214,0.25);-moz-box-shadow:0 1px 4px rgba(0,105,214,0.25);box-shadow:0 1px 4px rgba(0,105,214,0.25)}
.thumbnail>img{display:block;max-width:100%;margin-left:auto;margin-right:auto}
.thumbnail .caption{padding:9px;color:#555}
.media,.media-body{overflow:hidden;*overflow:visible;zoom:1}
.media,.media .media{margin-top:15px}
.media:first-child{margin-top:0}
.media-object{display:block}
.media-heading{margin:0 0 5px}
.media>.pull-left{margin-right:10px}
.media>.pull-right{margin-left:10px}
.media-list{margin-left:0;list-style:none}
.label,.badge{display:inline-block;padding:2px 4px;font-size:10.998px;font-weight:bold;line-height:14px;color:#fff;vertical-align:baseline;white-space:nowrap;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#999}
.label{border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.badge{padding-left:9px;padding-right:9px;border-radius:9px;-webkit-border-radius:9px;-moz-border-radius:9px;border-radius:9px}
.label:empty,.badge:empty{display:none}
a.label:hover,a.label:focus,a.badge:hover,a.badge:focus{color:#fff;text-decoration:none;cursor:pointer}
.label-important,.badge-important{background-color:#b94a48}
.label-important[href],.badge-important[href]{background-color:#953b39}
.label-warning,.badge-warning{background-color:#f89406}
.label-warning[href],.badge-warning[href]{background-color:#c67605}
.label-success,.badge-success{background-color:#468847}
.label-success[href],.badge-success[href]{background-color:#356635}
.label-info,.badge-info{background-color:#3a87ad}
.label-info[href],.badge-info[href]{background-color:#2d6987}
.label-inverse,.badge-inverse{background-color:#333}
.label-inverse[href],.badge-inverse[href]{background-color:#1a1a1a}
.btn .label,.btn .badge{position:relative;top:-1px}
.btn-mini .label,.btn-mini .badge{top:0}
@-webkit-keyframes progress-bar-stripes{from{background-position:40px 0} to{background-position:0 0}}@-moz-keyframes progress-bar-stripes{from{background-position:40px 0} to{background-position:0 0}}@-ms-keyframes progress-bar-stripes{from{background-position:40px 0} to{background-position:0 0}}@-o-keyframes progress-bar-stripes{from{background-position:0 0} to{background-position:40px 0}}@keyframes progress-bar-stripes{from{background-position:40px 0} to{background-position:0 0}}.progress{overflow:hidden;height:20px;margin-bottom:20px;background-color:#f7f7f7;background-image:-moz-linear-gradient(top, #f5f5f5, #f9f9f9);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#f5f5f5), to(#f9f9f9));background-image:-webkit-linear-gradient(top, #f5f5f5, #f9f9f9);background-image:-o-linear-gradient(top, #f5f5f5, #f9f9f9);background-image:linear-gradient(to bottom, #f5f5f5, #f9f9f9);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5', endColorstr='#fff9f9f9', GradientType=0);-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);-moz-box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);box-shadow:inset 0 1px 2px rgba(0,0,0,0.1);border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.progress .bar{width:0;height:100%;color:#fff;float:left;font-size:12px;text-align:center;text-shadow:0 -1px 0 rgba(0,0,0,0.25);background-color:#0e90d2;background-image:-moz-linear-gradient(top, #149bdf, #0480be);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#149bdf), to(#0480be));background-image:-webkit-linear-gradient(top, #149bdf, #0480be);background-image:-o-linear-gradient(top, #149bdf, #0480be);background-image:linear-gradient(to bottom, #149bdf, #0480be);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff149bdf', endColorstr='#ff0480be', GradientType=0);-webkit-box-shadow:inset 0 -1px 0 rgba(0,0,0,0.15);-moz-box-shadow:inset 0 -1px 0 rgba(0,0,0,0.15);box-shadow:inset 0 -1px 0 rgba(0,0,0,0.15);-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;-webkit-transition:width .6s ease;-moz-transition:width .6s ease;-o-transition:width .6s ease;transition:width .6s ease}
.progress .bar+.bar{-webkit-box-shadow:inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15);-moz-box-shadow:inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15);box-shadow:inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15)}
.progress-striped .bar{background-color:#149bdf;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);-webkit-background-size:40px 40px;-moz-background-size:40px 40px;-o-background-size:40px 40px;background-size:40px 40px}
.progress.active .bar{-webkit-animation:progress-bar-stripes 2s linear infinite;-moz-animation:progress-bar-stripes 2s linear infinite;-ms-animation:progress-bar-stripes 2s linear infinite;-o-animation:progress-bar-stripes 2s linear infinite;animation:progress-bar-stripes 2s linear infinite}
.progress-danger .bar,.progress .bar-danger{background-color:#dd514c;background-image:-moz-linear-gradient(top, #ee5f5b, #c43c35);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#ee5f5b), to(#c43c35));background-image:-webkit-linear-gradient(top, #ee5f5b, #c43c35);background-image:-o-linear-gradient(top, #ee5f5b, #c43c35);background-image:linear-gradient(to bottom, #ee5f5b, #c43c35);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffee5f5b', endColorstr='#ffc43c35', GradientType=0)}
.progress-danger.progress-striped .bar,.progress-striped .bar-danger{background-color:#ee5f5b;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}
.progress-success .bar,.progress .bar-success{background-color:#5eb95e;background-image:-moz-linear-gradient(top, #62c462, #57a957);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#62c462), to(#57a957));background-image:-webkit-linear-gradient(top, #62c462, #57a957);background-image:-o-linear-gradient(top, #62c462, #57a957);background-image:linear-gradient(to bottom, #62c462, #57a957);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff62c462', endColorstr='#ff57a957', GradientType=0)}
.progress-success.progress-striped .bar,.progress-striped .bar-success{background-color:#62c462;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}
.progress-info .bar,.progress .bar-info{background-color:#4bb1cf;background-image:-moz-linear-gradient(top, #5bc0de, #339bb9);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#5bc0de), to(#339bb9));background-image:-webkit-linear-gradient(top, #5bc0de, #339bb9);background-image:-o-linear-gradient(top, #5bc0de, #339bb9);background-image:linear-gradient(to bottom, #5bc0de, #339bb9);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff339bb9', GradientType=0)}
.progress-info.progress-striped .bar,.progress-striped .bar-info{background-color:#5bc0de;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}
.progress-warning .bar,.progress .bar-warning{background-color:#faa732;background-image:-moz-linear-gradient(top, #fbb450, #f89406);background-image:-webkit-gradient(linear, 0 0, 0 100%, from(#fbb450), to(#f89406));background-image:-webkit-linear-gradient(top, #fbb450, #f89406);background-image:-o-linear-gradient(top, #fbb450, #f89406);background-image:linear-gradient(to bottom, #fbb450, #f89406);background-repeat:repeat-x;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffbb450', endColorstr='#fff89406', GradientType=0)}
.progress-warning.progress-striped .bar,.progress-striped .bar-warning{background-color:#fbb450;background-image:-webkit-gradient(linear, 0 100%, 100% 0, color-stop(.25, rgba(255,255,255,0.15)), color-stop(.25, transparent), color-stop(.5, transparent), color-stop(.5, rgba(255,255,255,0.15)), color-stop(.75, rgba(255,255,255,0.15)), color-stop(.75, transparent), to(transparent));background-image:-webkit-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-moz-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:-o-linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent);background-image:linear-gradient(45deg, rgba(255,255,255,0.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,0.15) 50%, rgba(255,255,255,0.15) 75%, transparent 75%, transparent)}
.accordion{margin-bottom:20px}
.accordion-group{margin-bottom:2px;border:1px solid #e5e5e5;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.accordion-heading{border-bottom:0}
.accordion-heading .accordion-toggle{display:block;padding:8px 15px}
.accordion-toggle{cursor:pointer}
.accordion-inner{padding:9px 15px;border-top:1px solid #e5e5e5}
.carousel{position:relative;margin-bottom:20px;line-height:1}
.carousel-inner{overflow:hidden;width:100%;position:relative}
.carousel-inner>.item{display:none;position:relative;-webkit-transition:.6s ease-in-out left;-moz-transition:.6s ease-in-out left;-o-transition:.6s ease-in-out left;transition:.6s ease-in-out left}.carousel-inner>.item>img,.carousel-inner>.item>a>img{display:block;line-height:1}
.carousel-inner>.active,.carousel-inner>.next,.carousel-inner>.prev{display:block}
.carousel-inner>.active{left:0}
.carousel-inner>.next,.carousel-inner>.prev{position:absolute;top:0;width:100%}
.carousel-inner>.next{left:100%}
.carousel-inner>.prev{left:-100%}
.carousel-inner>.next.left,.carousel-inner>.prev.right{left:0}
.carousel-inner>.active.left{left:-100%}
.carousel-inner>.active.right{left:100%}
.carousel-control{position:absolute;top:40%;left:15px;width:40px;height:40px;margin-top:-20px;font-size:60px;font-weight:100;line-height:30px;color:#fff;text-align:center;background:#222;border:3px solid #fff;-webkit-border-radius:23px;-moz-border-radius:23px;border-radius:23px;opacity:.5;filter:alpha(opacity=50)}.carousel-control.right{left:auto;right:15px}
.carousel-control:hover,.carousel-control:focus{color:#fff;text-decoration:none;opacity:.9;filter:alpha(opacity=90)}
.carousel-indicators{position:absolute;top:15px;right:15px;z-index:5;margin:0;list-style:none}.carousel-indicators li{display:block;float:left;width:10px;height:10px;margin-left:5px;text-indent:-999px;background-color:#ccc;background-color:rgba(255,255,255,0.25);border-radius:5px}
.carousel-indicators .active{background-color:#fff}
.carousel-caption{position:absolute;left:0;right:0;bottom:0;padding:15px;background:#333;background:rgba(0,0,0,0.75)}
.carousel-caption h4,.carousel-caption p{color:#fff;line-height:20px}
.carousel-caption h4{margin:0 0 5px}
.carousel-caption p{margin-bottom:0}
.hero-unit{padding:60px;margin-bottom:30px;font-size:18px;font-weight:200;line-height:30px;color:inherit;background-color:#eee;border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}.hero-unit h1{margin-bottom:0;font-size:60px;line-height:1;color:inherit;letter-spacing:-1px}
.hero-unit li{line-height:30px}
.pull-right{float:right}
.pull-left{float:left}
.hide{display:none}
.show{display:block}
.invisible{visibility:hidden}
.affix{position:fixed}
@-ms-viewport{width:device-width}.hidden{display:none;visibility:hidden}
.visible-phone{display:none !important}
.visible-tablet{display:none !important}
.hidden-desktop{display:none !important}
.visible-desktop{display:inherit !important}
@media (min-width:768px) and (max-width:979px){.hidden-desktop{display:inherit !important} .visible-desktop{display:none !important} .visible-tablet{display:inherit !important} .hidden-tablet{display:none !important}}@media (max-width:767px){.hidden-desktop{display:inherit !important} .visible-desktop{display:none !important} .visible-phone{display:inherit !important} .hidden-phone{display:none !important}}.visible-print{display:none !important}
@media print{.visible-print{display:inherit !important} .hidden-print{display:none !important}}@media (min-width:1200px){.row{margin-left:-30px;*zoom:1}.row:before,.row:after{display:table;content:"";line-height:0} .row:after{clear:both} [class*="span"]{float:left;min-height:1px;margin-left:30px} .container,.navbar-static-top .container,.navbar-fixed-top .container,.navbar-fixed-bottom .container{width:1170px} .span12{width:1170px} .span11{width:1070px} .span10{width:970px} .span9{width:870px} .span8{width:770px} .span7{width:670px} .span6{width:570px} .span5{width:470px} .span4{width:370px} .span3{width:270px} .span2{width:170px} .span1{width:70px} .offset12{margin-left:1230px} .offset11{margin-left:1130px} .offset10{margin-left:1030px} .offset9{margin-left:930px} .offset8{margin-left:830px} .offset7{margin-left:730px} .offset6{margin-left:630px} .offset5{margin-left:530px} .offset4{margin-left:430px} .offset3{margin-left:330px} .offset2{margin-left:230px} .offset1{margin-left:130px} .row-fluid{width:100%;*zoom:1}.row-fluid:before,.row-fluid:after{display:table;content:"";line-height:0} .row-fluid:after{clear:both} .row-fluid [class*="span"]{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;float:left;margin-left:2.564102564102564%;*margin-left:2.5109110747408616%} .row-fluid [class*="span"]:first-child{margin-left:0} .row-fluid .controls-row [class*="span"]+[class*="span"]{margin-left:2.564102564102564%} .row-fluid .span12{width:100%;*width:99.94680851063829%} .row-fluid .span11{width:91.45299145299145%;*width:91.39979996362975%} .row-fluid .span10{width:82.90598290598291%;*width:82.8527914166212%} .row-fluid .span9{width:74.35897435897436%;*width:74.30578286961266%} .row-fluid .span8{width:65.81196581196582%;*width:65.75877432260411%} .row-fluid .span7{width:57.26495726495726%;*width:57.21176577559556%} .row-fluid .span6{width:48.717948717948715%;*width:48.664757228587014%} .row-fluid .span5{width:40.17094017094017%;*width:40.11774868157847%} .row-fluid .span4{width:31.623931623931625%;*width:31.570740134569924%} .row-fluid .span3{width:23.076923076923077%;*width:23.023731587561375%} .row-fluid .span2{width:14.52991452991453%;*width:14.476723040552828%} .row-fluid .span1{width:5.982905982905983%;*width:5.929714493544281%} .row-fluid .offset12{margin-left:105.12820512820512%;*margin-left:105.02182214948171%} .row-fluid .offset12:first-child{margin-left:102.56410256410257%;*margin-left:102.45771958537915%} .row-fluid .offset11{margin-left:96.58119658119658%;*margin-left:96.47481360247316%} .row-fluid .offset11:first-child{margin-left:94.01709401709402%;*margin-left:93.91071103837061%} .row-fluid .offset10{margin-left:88.03418803418803%;*margin-left:87.92780505546462%} .row-fluid .offset10:first-child{margin-left:85.47008547008548%;*margin-left:85.36370249136206%} .row-fluid .offset9{margin-left:79.48717948717949%;*margin-left:79.38079650845607%} .row-fluid .offset9:first-child{margin-left:76.92307692307693%;*margin-left:76.81669394435352%} .row-fluid .offset8{margin-left:70.94017094017094%;*margin-left:70.83378796144753%} .row-fluid .offset8:first-child{margin-left:68.37606837606839%;*margin-left:68.26968539734497%} .row-fluid .offset7{margin-left:62.393162393162385%;*margin-left:62.28677941443899%} .row-fluid .offset7:first-child{margin-left:59.82905982905982%;*margin-left:59.72267685033642%} .row-fluid .offset6{margin-left:53.84615384615384%;*margin-left:53.739770867430444%} .row-fluid .offset6:first-child{margin-left:51.28205128205128%;*margin-left:51.175668303327875%} .row-fluid .offset5{margin-left:45.299145299145295%;*margin-left:45.1927623204219%} .row-fluid .offset5:first-child{margin-left:42.73504273504273%;*margin-left:42.62865975631933%} .row-fluid .offset4{margin-left:36.75213675213675%;*margin-left:36.645753773413354%} .row-fluid .offset4:first-child{margin-left:34.18803418803419%;*margin-left:34.081651209310785%} .row-fluid .offset3{margin-left:28.205128205128204%;*margin-left:28.0987452264048%} .row-fluid .offset3:first-child{margin-left:25.641025641025642%;*margin-left:25.53464266230224%} .row-fluid .offset2{margin-left:19.65811965811966%;*margin-left:19.551736679396257%} .row-fluid .offset2:first-child{margin-left:17.094017094017094%;*margin-left:16.98763411529369%} .row-fluid .offset1{margin-left:11.11111111111111%;*margin-left:11.004728132387708%} .row-fluid .offset1:first-child{margin-left:8.547008547008547%;*margin-left:8.440625568285142%} input,textarea,.uneditable-input{margin-left:0} .controls-row [class*="span"]+[class*="span"]{margin-left:30px} input.span12,textarea.span12,.uneditable-input.span12{width:1156px} input.span11,textarea.span11,.uneditable-input.span11{width:1056px} input.span10,textarea.span10,.uneditable-input.span10{width:956px} input.span9,textarea.span9,.uneditable-input.span9{width:856px} input.span8,textarea.span8,.uneditable-input.span8{width:756px} input.span7,textarea.span7,.uneditable-input.span7{width:656px} input.span6,textarea.span6,.uneditable-input.span6{width:556px} input.span5,textarea.span5,.uneditable-input.span5{width:456px} input.span4,textarea.span4,.uneditable-input.span4{width:356px} input.span3,textarea.span3,.uneditable-input.span3{width:256px} input.span2,textarea.span2,.uneditable-input.span2{width:156px} input.span1,textarea.span1,.uneditable-input.span1{width:56px} .thumbnails{margin-left:-30px} .thumbnails>li{margin-left:30px} .row-fluid .thumbnails{margin-left:0}}@media (min-width:768px) and (max-width:979px){.row{margin-left:-20px;*zoom:1}.row:before,.row:after{display:table;content:"";line-height:0} .row:after{clear:both} [class*="span"]{float:left;min-height:1px;margin-left:20px} .container,.navbar-static-top .container,.navbar-fixed-top .container,.navbar-fixed-bottom .container{width:724px} .span12{width:724px} .span11{width:662px} .span10{width:600px} .span9{width:538px} .span8{width:476px} .span7{width:414px} .span6{width:352px} .span5{width:290px} .span4{width:228px} .span3{width:166px} .span2{width:104px} .span1{width:42px} .offset12{margin-left:764px} .offset11{margin-left:702px} .offset10{margin-left:640px} .offset9{margin-left:578px} .offset8{margin-left:516px} .offset7{margin-left:454px} .offset6{margin-left:392px} .offset5{margin-left:330px} .offset4{margin-left:268px} .offset3{margin-left:206px} .offset2{margin-left:144px} .offset1{margin-left:82px} .row-fluid{width:100%;*zoom:1}.row-fluid:before,.row-fluid:after{display:table;content:"";line-height:0} .row-fluid:after{clear:both} .row-fluid [class*="span"]{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;float:left;margin-left:2.7624309392265194%;*margin-left:2.709239449864817%} .row-fluid [class*="span"]:first-child{margin-left:0} .row-fluid .controls-row [class*="span"]+[class*="span"]{margin-left:2.7624309392265194%} .row-fluid .span12{width:100%;*width:99.94680851063829%} .row-fluid .span11{width:91.43646408839778%;*width:91.38327259903608%} .row-fluid .span10{width:82.87292817679558%;*width:82.81973668743387%} .row-fluid .span9{width:74.30939226519337%;*width:74.25620077583166%} .row-fluid .span8{width:65.74585635359117%;*width:65.69266486422946%} .row-fluid .span7{width:57.18232044198895%;*width:57.12912895262725%} .row-fluid .span6{width:48.61878453038674%;*width:48.56559304102504%} .row-fluid .span5{width:40.05524861878453%;*width:40.00205712942283%} .row-fluid .span4{width:31.491712707182323%;*width:31.43852121782062%} .row-fluid .span3{width:22.92817679558011%;*width:22.87498530621841%} .row-fluid .span2{width:14.3646408839779%;*width:14.311449394616199%} .row-fluid .span1{width:5.801104972375691%;*width:5.747913483013988%} .row-fluid .offset12{margin-left:105.52486187845304%;*margin-left:105.41847889972962%} .row-fluid .offset12:first-child{margin-left:102.76243093922652%;*margin-left:102.6560479605031%} .row-fluid .offset11{margin-left:96.96132596685082%;*margin-left:96.8549429881274%} .row-fluid .offset11:first-child{margin-left:94.1988950276243%;*margin-left:94.09251204890089%} .row-fluid .offset10{margin-left:88.39779005524862%;*margin-left:88.2914070765252%} .row-fluid .offset10:first-child{margin-left:85.6353591160221%;*margin-left:85.52897613729868%} .row-fluid .offset9{margin-left:79.8342541436464%;*margin-left:79.72787116492299%} .row-fluid .offset9:first-child{margin-left:77.07182320441989%;*margin-left:76.96544022569647%} .row-fluid .offset8{margin-left:71.2707182320442%;*margin-left:71.16433525332079%} .row-fluid .offset8:first-child{margin-left:68.50828729281768%;*margin-left:68.40190431409427%} .row-fluid .offset7{margin-left:62.70718232044199%;*margin-left:62.600799341718584%} .row-fluid .offset7:first-child{margin-left:59.94475138121547%;*margin-left:59.838368402492065%} .row-fluid .offset6{margin-left:54.14364640883978%;*margin-left:54.037263430116376%} .row-fluid .offset6:first-child{margin-left:51.38121546961326%;*margin-left:51.27483249088986%} .row-fluid .offset5{margin-left:45.58011049723757%;*margin-left:45.47372751851417%} .row-fluid .offset5:first-child{margin-left:42.81767955801105%;*margin-left:42.71129657928765%} .row-fluid .offset4{margin-left:37.01657458563536%;*margin-left:36.91019160691196%} .row-fluid .offset4:first-child{margin-left:34.25414364640884%;*margin-left:34.14776066768544%} .row-fluid .offset3{margin-left:28.45303867403315%;*margin-left:28.346655695309746%} .row-fluid .offset3:first-child{margin-left:25.69060773480663%;*margin-left:25.584224756083227%} .row-fluid .offset2{margin-left:19.88950276243094%;*margin-left:19.783119783707537%} .row-fluid .offset2:first-child{margin-left:17.12707182320442%;*margin-left:17.02068884448102%} .row-fluid .offset1{margin-left:11.32596685082873%;*margin-left:11.219583872105325%} .row-fluid .offset1:first-child{margin-left:8.56353591160221%;*margin-left:8.457152932878806%} input,textarea,.uneditable-input{margin-left:0} .controls-row [class*="span"]+[class*="span"]{margin-left:20px} input.span12,textarea.span12,.uneditable-input.span12{width:710px} input.span11,textarea.span11,.uneditable-input.span11{width:648px} input.span10,textarea.span10,.uneditable-input.span10{width:586px} input.span9,textarea.span9,.uneditable-input.span9{width:524px} input.span8,textarea.span8,.uneditable-input.span8{width:462px} input.span7,textarea.span7,.uneditable-input.span7{width:400px} input.span6,textarea.span6,.uneditable-input.span6{width:338px} input.span5,textarea.span5,.uneditable-input.span5{width:276px} input.span4,textarea.span4,.uneditable-input.span4{width:214px} input.span3,textarea.span3,.uneditable-input.span3{width:152px} input.span2,textarea.span2,.uneditable-input.span2{width:90px} input.span1,textarea.span1,.uneditable-input.span1{width:28px}}@media (max-width:767px){body{padding-left:20px;padding-right:20px} .navbar-fixed-top,.navbar-fixed-bottom,.navbar-static-top{margin-left:-20px;margin-right:-20px} .container-fluid{padding:0} .dl-horizontal dt{float:none;clear:none;width:auto;text-align:left} .dl-horizontal dd{margin-left:0} .container{width:auto} .row-fluid{width:100%} .row,.thumbnails{margin-left:0} .thumbnails>li{float:none;margin-left:0} [class*="span"],.uneditable-input[class*="span"],.row-fluid [class*="span"]{float:none;display:block;width:100%;margin-left:0;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box} .span12,.row-fluid .span12{width:100%;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box} .row-fluid [class*="offset"]:first-child{margin-left:0} .input-large,.input-xlarge,.input-xxlarge,input[class*="span"],select[class*="span"],textarea[class*="span"],.uneditable-input{display:block;width:100%;min-height:30px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box} .input-prepend input,.input-append input,.input-prepend input[class*="span"],.input-append input[class*="span"]{display:inline-block;width:auto} .controls-row [class*="span"]+[class*="span"]{margin-left:0} .modal{position:fixed;top:20px;left:20px;right:20px;width:auto;margin:0}.modal.fade{top:-100px} .modal.fade.in{top:20px}}@media (max-width:480px){.nav-collapse{-webkit-transform:translate3d(0, 0, 0)} .page-header h1 small{display:block;line-height:20px} input[type="checkbox"],input[type="radio"]{border:1px solid #ccc} .form-horizontal .control-label{float:none;width:auto;padding-top:0;text-align:left} .form-horizontal .controls{margin-left:0} .form-horizontal .control-list{padding-top:0} .form-horizontal .form-actions{padding-left:10px;padding-right:10px} .media .pull-left,.media .pull-right{float:none;display:block;margin-bottom:10px} .media-object{margin-right:0;margin-left:0} .modal{top:10px;left:10px;right:10px} .modal-header .close{padding:10px;margin:-10px} .carousel-caption{position:static}}@media (max-width:979px){body{padding-top:0} .navbar-fixed-top,.navbar-fixed-bottom{position:static} .navbar-fixed-top{margin-bottom:20px} .navbar-fixed-bottom{margin-top:20px} .navbar-fixed-top .navbar-inner,.navbar-fixed-bottom .navbar-inner{padding:5px} .navbar .container{width:auto;padding:0} .navbar .brand{padding-left:10px;padding-right:10px;margin:0 0 0 -5px} .nav-collapse{clear:both} .nav-collapse .nav{float:none;margin:0 0 10px} .nav-collapse .nav>li{float:none} .nav-collapse .nav>li>a{margin-bottom:2px} .nav-collapse .nav>.divider-vertical{display:none} .nav-collapse .nav .nav-header{color:#777;text-shadow:none} .nav-collapse .nav>li>a,.nav-collapse .dropdown-menu a{padding:9px 15px;font-weight:bold;color:#777;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px} .nav-collapse .btn{padding:4px 10px 4px;font-weight:normal;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px} .nav-collapse .dropdown-menu li+li a{margin-bottom:2px} .nav-collapse .nav>li>a:hover,.nav-collapse .nav>li>a:focus,.nav-collapse .dropdown-menu a:hover,.nav-collapse .dropdown-menu a:focus{background-color:#f2f2f2} .navbar-inverse .nav-collapse .nav>li>a,.navbar-inverse .nav-collapse .dropdown-menu a{color:#999} .navbar-inverse .nav-collapse .nav>li>a:hover,.navbar-inverse .nav-collapse .nav>li>a:focus,.navbar-inverse .nav-collapse .dropdown-menu a:hover,.navbar-inverse .nav-collapse .dropdown-menu a:focus{background-color:#111} .nav-collapse.in .btn-group{margin-top:5px;padding:0} .nav-collapse .dropdown-menu{position:static;top:auto;left:auto;float:none;display:none;max-width:none;margin:0 15px;padding:0;background-color:transparent;border:none;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;-webkit-box-shadow:none;-moz-box-shadow:none;box-shadow:none} .nav-collapse .open>.dropdown-menu{display:block} .nav-collapse .dropdown-menu:before,.nav-collapse .dropdown-menu:after{display:none} .nav-collapse .dropdown-menu .divider{display:none} .nav-collapse .nav>li>.dropdown-menu:before,.nav-collapse .nav>li>.dropdown-menu:after{display:none} .nav-collapse .navbar-form,.nav-collapse .navbar-search{float:none;padding:10px 15px;margin:10px 0;border-top:1px solid #f2f2f2;border-bottom:1px solid #f2f2f2;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1);-moz-box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1);box-shadow:inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1)} .navbar-inverse .nav-collapse .navbar-form,.navbar-inverse .nav-collapse .navbar-search{border-top-color:#111;border-bottom-color:#111} .navbar .nav-collapse .nav.pull-right{float:none;margin-left:0} .nav-collapse,.nav-collapse.collapse{overflow:hidden;height:0} .navbar .btn-navbar{display:block} .navbar-static .navbar-inner{padding-left:10px;padding-right:10px}}@media (min-width:979px + 1){.nav-collapse.collapse{height:auto !important;overflow:visible !important}}@font-face{font-family:'FontAwesome';src:url('../components/font-awesome/font/fontawesome-webfont.eot?v=3.2.1');src:url('../components/font-awesome/font/fontawesome-webfont.eot?#iefix&v=3.2.1') format('embedded-opentype'),url('../components/font-awesome/font/fontawesome-webfont.woff?v=3.2.1') format('woff'),url('../components/font-awesome/font/fontawesome-webfont.ttf?v=3.2.1') format('truetype'),url('../components/font-awesome/font/fontawesome-webfont.svg#fontawesomeregular?v=3.2.1') format('svg');font-weight:normal;font-style:normal}[class^="icon-"],[class*=" icon-"]{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em}
[class^="icon-"]:before,[class*=" icon-"]:before{text-decoration:inherit;display:inline-block;speak:none}
.icon-large:before{vertical-align:-10%;font-size:1.3333333333333333em}
a [class^="icon-"],a [class*=" icon-"]{display:inline}
[class^="icon-"].icon-fixed-width,[class*=" icon-"].icon-fixed-width{display:inline-block;width:1.1428571428571428em;text-align:right;padding-right:.2857142857142857em}[class^="icon-"].icon-fixed-width.icon-large,[class*=" icon-"].icon-fixed-width.icon-large{width:1.4285714285714286em}
.icons-ul{margin-left:2.142857142857143em;list-style-type:none}.icons-ul>li{position:relative}
.icons-ul .icon-li{position:absolute;left:-2.142857142857143em;width:2.142857142857143em;text-align:center;line-height:inherit}
[class^="icon-"].hide,[class*=" icon-"].hide{display:none}
.icon-muted{color:#eee}
.icon-light{color:#fff}
.icon-dark{color:#333}
.icon-border{border:solid 1px #eee;padding:.2em .25em .15em;border-radius:3px;-webkit-border-radius:3px;-moz-border-radius:3px;border-radius:3px}
.icon-2x{font-size:2em}.icon-2x.icon-border{border-width:2px;border-radius:4px;-webkit-border-radius:4px;-moz-border-radius:4px;border-radius:4px}
.icon-3x{font-size:3em}.icon-3x.icon-border{border-width:3px;border-radius:5px;-webkit-border-radius:5px;-moz-border-radius:5px;border-radius:5px}
.icon-4x{font-size:4em}.icon-4x.icon-border{border-width:4px;border-radius:6px;-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px}
.icon-5x{font-size:5em}.icon-5x.icon-border{border-width:5px;border-radius:7px;-webkit-border-radius:7px;-moz-border-radius:7px;border-radius:7px}
.pull-right{float:right}
.pull-left{float:left}
[class^="icon-"].pull-left,[class*=" icon-"].pull-left{margin-right:.3em}
[class^="icon-"].pull-right,[class*=" icon-"].pull-right{margin-left:.3em}
[class^="icon-"],[class*=" icon-"]{display:inline;width:auto;height:auto;line-height:normal;vertical-align:baseline;background-image:none;background-position:0 0;background-repeat:repeat;margin-top:0}
.icon-white,.nav-pills>.active>a>[class^="icon-"],.nav-pills>.active>a>[class*=" icon-"],.nav-list>.active>a>[class^="icon-"],.nav-list>.active>a>[class*=" icon-"],.navbar-inverse .nav>.active>a>[class^="icon-"],.navbar-inverse .nav>.active>a>[class*=" icon-"],.dropdown-menu>li>a:hover>[class^="icon-"],.dropdown-menu>li>a:hover>[class*=" icon-"],.dropdown-menu>.active>a>[class^="icon-"],.dropdown-menu>.active>a>[class*=" icon-"],.dropdown-submenu:hover>a>[class^="icon-"],.dropdown-submenu:hover>a>[class*=" icon-"]{background-image:none}
.btn [class^="icon-"].icon-large,.nav [class^="icon-"].icon-large,.btn [class*=" icon-"].icon-large,.nav [class*=" icon-"].icon-large{line-height:.9em}
.btn [class^="icon-"].icon-spin,.nav [class^="icon-"].icon-spin,.btn [class*=" icon-"].icon-spin,.nav [class*=" icon-"].icon-spin{display:inline-block}
.nav-tabs [class^="icon-"],.nav-pills [class^="icon-"],.nav-tabs [class*=" icon-"],.nav-pills [class*=" icon-"],.nav-tabs [class^="icon-"].icon-large,.nav-pills [class^="icon-"].icon-large,.nav-tabs [class*=" icon-"].icon-large,.nav-pills [class*=" icon-"].icon-large{line-height:.9em}
.btn [class^="icon-"].pull-left.icon-2x,.btn [class*=" icon-"].pull-left.icon-2x,.btn [class^="icon-"].pull-right.icon-2x,.btn [class*=" icon-"].pull-right.icon-2x{margin-top:.18em}
.btn [class^="icon-"].icon-spin.icon-large,.btn [class*=" icon-"].icon-spin.icon-large{line-height:.8em}
.btn.btn-small [class^="icon-"].pull-left.icon-2x,.btn.btn-small [class*=" icon-"].pull-left.icon-2x,.btn.btn-small [class^="icon-"].pull-right.icon-2x,.btn.btn-small [class*=" icon-"].pull-right.icon-2x{margin-top:.25em}
.btn.btn-large [class^="icon-"],.btn.btn-large [class*=" icon-"]{margin-top:0}.btn.btn-large [class^="icon-"].pull-left.icon-2x,.btn.btn-large [class*=" icon-"].pull-left.icon-2x,.btn.btn-large [class^="icon-"].pull-right.icon-2x,.btn.btn-large [class*=" icon-"].pull-right.icon-2x{margin-top:.05em}
.btn.btn-large [class^="icon-"].pull-left.icon-2x,.btn.btn-large [class*=" icon-"].pull-left.icon-2x{margin-right:.2em}
.btn.btn-large [class^="icon-"].pull-right.icon-2x,.btn.btn-large [class*=" icon-"].pull-right.icon-2x{margin-left:.2em}
.nav-list [class^="icon-"],.nav-list [class*=" icon-"]{line-height:inherit}
.icon-stack{position:relative;display:inline-block;width:2em;height:2em;line-height:2em;vertical-align:-35%}.icon-stack [class^="icon-"],.icon-stack [class*=" icon-"]{display:block;text-align:center;position:absolute;width:100%;height:100%;font-size:1em;line-height:inherit;*line-height:2em}
.icon-stack .icon-stack-base{font-size:2em;*line-height:1em}
.icon-spin{display:inline-block;-moz-animation:spin 2s infinite linear;-o-animation:spin 2s infinite linear;-webkit-animation:spin 2s infinite linear;animation:spin 2s infinite linear}
a .icon-stack,a .icon-spin{display:inline-block;text-decoration:none}
@-moz-keyframes spin{0%{-moz-transform:rotate(0deg)} 100%{-moz-transform:rotate(359deg)}}@-webkit-keyframes spin{0%{-webkit-transform:rotate(0deg)} 100%{-webkit-transform:rotate(359deg)}}@-o-keyframes spin{0%{-o-transform:rotate(0deg)} 100%{-o-transform:rotate(359deg)}}@-ms-keyframes spin{0%{-ms-transform:rotate(0deg)} 100%{-ms-transform:rotate(359deg)}}@keyframes spin{0%{transform:rotate(0deg)} 100%{transform:rotate(359deg)}}.icon-rotate-90:before{-webkit-transform:rotate(90deg);-moz-transform:rotate(90deg);-ms-transform:rotate(90deg);-o-transform:rotate(90deg);transform:rotate(90deg);filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=1)}
.icon-rotate-180:before{-webkit-transform:rotate(180deg);-moz-transform:rotate(180deg);-ms-transform:rotate(180deg);-o-transform:rotate(180deg);transform:rotate(180deg);filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2)}
.icon-rotate-270:before{-webkit-transform:rotate(270deg);-moz-transform:rotate(270deg);-ms-transform:rotate(270deg);-o-transform:rotate(270deg);transform:rotate(270deg);filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=3)}
.icon-flip-horizontal:before{-webkit-transform:scale(-1, 1);-moz-transform:scale(-1, 1);-ms-transform:scale(-1, 1);-o-transform:scale(-1, 1);transform:scale(-1, 1)}
.icon-flip-vertical:before{-webkit-transform:scale(1, -1);-moz-transform:scale(1, -1);-ms-transform:scale(1, -1);-o-transform:scale(1, -1);transform:scale(1, -1)}
a .icon-rotate-90:before,a .icon-rotate-180:before,a .icon-rotate-270:before,a .icon-flip-horizontal:before,a .icon-flip-vertical:before{display:inline-block}
.icon-glass:before{content:"\f000"}
.icon-music:before{content:"\f001"}
.icon-search:before{content:"\f002"}
.icon-envelope-alt:before{content:"\f003"}
.icon-heart:before{content:"\f004"}
.icon-star:before{content:"\f005"}
.icon-star-empty:before{content:"\f006"}
.icon-user:before{content:"\f007"}
.icon-film:before{content:"\f008"}
.icon-th-large:before{content:"\f009"}
.icon-th:before{content:"\f00a"}
.icon-th-list:before{content:"\f00b"}
.icon-ok:before{content:"\f00c"}
.icon-remove:before{content:"\f00d"}
.icon-zoom-in:before{content:"\f00e"}
.icon-zoom-out:before{content:"\f010"}
.icon-power-off:before,.icon-off:before{content:"\f011"}
.icon-signal:before{content:"\f012"}
.icon-gear:before,.icon-cog:before{content:"\f013"}
.icon-trash:before{content:"\f014"}
.icon-home:before{content:"\f015"}
.icon-file-alt:before{content:"\f016"}
.icon-time:before{content:"\f017"}
.icon-road:before{content:"\f018"}
.icon-download-alt:before{content:"\f019"}
.icon-download:before{content:"\f01a"}
.icon-upload:before{content:"\f01b"}
.icon-inbox:before{content:"\f01c"}
.icon-play-circle:before{content:"\f01d"}
.icon-rotate-right:before,.icon-repeat:before{content:"\f01e"}
.icon-refresh:before{content:"\f021"}
.icon-list-alt:before{content:"\f022"}
.icon-lock:before{content:"\f023"}
.icon-flag:before{content:"\f024"}
.icon-headphones:before{content:"\f025"}
.icon-volume-off:before{content:"\f026"}
.icon-volume-down:before{content:"\f027"}
.icon-volume-up:before{content:"\f028"}
.icon-qrcode:before{content:"\f029"}
.icon-barcode:before{content:"\f02a"}
.icon-tag:before{content:"\f02b"}
.icon-tags:before{content:"\f02c"}
.icon-book:before{content:"\f02d"}
.icon-bookmark:before{content:"\f02e"}
.icon-print:before{content:"\f02f"}
.icon-camera:before{content:"\f030"}
.icon-font:before{content:"\f031"}
.icon-bold:before{content:"\f032"}
.icon-italic:before{content:"\f033"}
.icon-text-height:before{content:"\f034"}
.icon-text-width:before{content:"\f035"}
.icon-align-left:before{content:"\f036"}
.icon-align-center:before{content:"\f037"}
.icon-align-right:before{content:"\f038"}
.icon-align-justify:before{content:"\f039"}
.icon-list:before{content:"\f03a"}
.icon-indent-left:before{content:"\f03b"}
.icon-indent-right:before{content:"\f03c"}
.icon-facetime-video:before{content:"\f03d"}
.icon-picture:before{content:"\f03e"}
.icon-pencil:before{content:"\f040"}
.icon-map-marker:before{content:"\f041"}
.icon-adjust:before{content:"\f042"}
.icon-tint:before{content:"\f043"}
.icon-edit:before{content:"\f044"}
.icon-share:before{content:"\f045"}
.icon-check:before{content:"\f046"}
.icon-move:before{content:"\f047"}
.icon-step-backward:before{content:"\f048"}
.icon-fast-backward:before{content:"\f049"}
.icon-backward:before{content:"\f04a"}
.icon-play:before{content:"\f04b"}
.icon-pause:before{content:"\f04c"}
.icon-stop:before{content:"\f04d"}
.icon-forward:before{content:"\f04e"}
.icon-fast-forward:before{content:"\f050"}
.icon-step-forward:before{content:"\f051"}
.icon-eject:before{content:"\f052"}
.icon-chevron-left:before{content:"\f053"}
.icon-chevron-right:before{content:"\f054"}
.icon-plus-sign:before{content:"\f055"}
.icon-minus-sign:before{content:"\f056"}
.icon-remove-sign:before{content:"\f057"}
.icon-ok-sign:before{content:"\f058"}
.icon-question-sign:before{content:"\f059"}
.icon-info-sign:before{content:"\f05a"}
.icon-screenshot:before{content:"\f05b"}
.icon-remove-circle:before{content:"\f05c"}
.icon-ok-circle:before{content:"\f05d"}
.icon-ban-circle:before{content:"\f05e"}
.icon-arrow-left:before{content:"\f060"}
.icon-arrow-right:before{content:"\f061"}
.icon-arrow-up:before{content:"\f062"}
.icon-arrow-down:before{content:"\f063"}
.icon-mail-forward:before,.icon-share-alt:before{content:"\f064"}
.icon-resize-full:before{content:"\f065"}
.icon-resize-small:before{content:"\f066"}
.icon-plus:before{content:"\f067"}
.icon-minus:before{content:"\f068"}
.icon-asterisk:before{content:"\f069"}
.icon-exclamation-sign:before{content:"\f06a"}
.icon-gift:before{content:"\f06b"}
.icon-leaf:before{content:"\f06c"}
.icon-fire:before{content:"\f06d"}
.icon-eye-open:before{content:"\f06e"}
.icon-eye-close:before{content:"\f070"}
.icon-warning-sign:before{content:"\f071"}
.icon-plane:before{content:"\f072"}
.icon-calendar:before{content:"\f073"}
.icon-random:before{content:"\f074"}
.icon-comment:before{content:"\f075"}
.icon-magnet:before{content:"\f076"}
.icon-chevron-up:before{content:"\f077"}
.icon-chevron-down:before{content:"\f078"}
.icon-retweet:before{content:"\f079"}
.icon-shopping-cart:before{content:"\f07a"}
.icon-folder-close:before{content:"\f07b"}
.icon-folder-open:before{content:"\f07c"}
.icon-resize-vertical:before{content:"\f07d"}
.icon-resize-horizontal:before{content:"\f07e"}
.icon-bar-chart:before{content:"\f080"}
.icon-twitter-sign:before{content:"\f081"}
.icon-facebook-sign:before{content:"\f082"}
.icon-camera-retro:before{content:"\f083"}
.icon-key:before{content:"\f084"}
.icon-gears:before,.icon-cogs:before{content:"\f085"}
.icon-comments:before{content:"\f086"}
.icon-thumbs-up-alt:before{content:"\f087"}
.icon-thumbs-down-alt:before{content:"\f088"}
.icon-star-half:before{content:"\f089"}
.icon-heart-empty:before{content:"\f08a"}
.icon-signout:before{content:"\f08b"}
.icon-linkedin-sign:before{content:"\f08c"}
.icon-pushpin:before{content:"\f08d"}
.icon-external-link:before{content:"\f08e"}
.icon-signin:before{content:"\f090"}
.icon-trophy:before{content:"\f091"}
.icon-github-sign:before{content:"\f092"}
.icon-upload-alt:before{content:"\f093"}
.icon-lemon:before{content:"\f094"}
.icon-phone:before{content:"\f095"}
.icon-unchecked:before,.icon-check-empty:before{content:"\f096"}
.icon-bookmark-empty:before{content:"\f097"}
.icon-phone-sign:before{content:"\f098"}
.icon-twitter:before{content:"\f099"}
.icon-facebook:before{content:"\f09a"}
.icon-github:before{content:"\f09b"}
.icon-unlock:before{content:"\f09c"}
.icon-credit-card:before{content:"\f09d"}
.icon-rss:before{content:"\f09e"}
.icon-hdd:before{content:"\f0a0"}
.icon-bullhorn:before{content:"\f0a1"}
.icon-bell:before{content:"\f0a2"}
.icon-certificate:before{content:"\f0a3"}
.icon-hand-right:before{content:"\f0a4"}
.icon-hand-left:before{content:"\f0a5"}
.icon-hand-up:before{content:"\f0a6"}
.icon-hand-down:before{content:"\f0a7"}
.icon-circle-arrow-left:before{content:"\f0a8"}
.icon-circle-arrow-right:before{content:"\f0a9"}
.icon-circle-arrow-up:before{content:"\f0aa"}
.icon-circle-arrow-down:before{content:"\f0ab"}
.icon-globe:before{content:"\f0ac"}
.icon-wrench:before{content:"\f0ad"}
.icon-tasks:before{content:"\f0ae"}
.icon-filter:before{content:"\f0b0"}
.icon-briefcase:before{content:"\f0b1"}
.icon-fullscreen:before{content:"\f0b2"}
.icon-group:before{content:"\f0c0"}
.icon-link:before{content:"\f0c1"}
.icon-cloud:before{content:"\f0c2"}
.icon-beaker:before{content:"\f0c3"}
.icon-cut:before{content:"\f0c4"}
.icon-copy:before{content:"\f0c5"}
.icon-paperclip:before,.icon-paper-clip:before{content:"\f0c6"}
.icon-save:before{content:"\f0c7"}
.icon-sign-blank:before{content:"\f0c8"}
.icon-reorder:before{content:"\f0c9"}
.icon-list-ul:before{content:"\f0ca"}
.icon-list-ol:before{content:"\f0cb"}
.icon-strikethrough:before{content:"\f0cc"}
.icon-underline:before{content:"\f0cd"}
.icon-table:before{content:"\f0ce"}
.icon-magic:before{content:"\f0d0"}
.icon-truck:before{content:"\f0d1"}
.icon-pinterest:before{content:"\f0d2"}
.icon-pinterest-sign:before{content:"\f0d3"}
.icon-google-plus-sign:before{content:"\f0d4"}
.icon-google-plus:before{content:"\f0d5"}
.icon-money:before{content:"\f0d6"}
.icon-caret-down:before{content:"\f0d7"}
.icon-caret-up:before{content:"\f0d8"}
.icon-caret-left:before{content:"\f0d9"}
.icon-caret-right:before{content:"\f0da"}
.icon-columns:before{content:"\f0db"}
.icon-sort:before{content:"\f0dc"}
.icon-sort-down:before{content:"\f0dd"}
.icon-sort-up:before{content:"\f0de"}
.icon-envelope:before{content:"\f0e0"}
.icon-linkedin:before{content:"\f0e1"}
.icon-rotate-left:before,.icon-undo:before{content:"\f0e2"}
.icon-legal:before{content:"\f0e3"}
.icon-dashboard:before{content:"\f0e4"}
.icon-comment-alt:before{content:"\f0e5"}
.icon-comments-alt:before{content:"\f0e6"}
.icon-bolt:before{content:"\f0e7"}
.icon-sitemap:before{content:"\f0e8"}
.icon-umbrella:before{content:"\f0e9"}
.icon-paste:before{content:"\f0ea"}
.icon-lightbulb:before{content:"\f0eb"}
.icon-exchange:before{content:"\f0ec"}
.icon-cloud-download:before{content:"\f0ed"}
.icon-cloud-upload:before{content:"\f0ee"}
.icon-user-md:before{content:"\f0f0"}
.icon-stethoscope:before{content:"\f0f1"}
.icon-suitcase:before{content:"\f0f2"}
.icon-bell-alt:before{content:"\f0f3"}
.icon-coffee:before{content:"\f0f4"}
.icon-food:before{content:"\f0f5"}
.icon-file-text-alt:before{content:"\f0f6"}
.icon-building:before{content:"\f0f7"}
.icon-hospital:before{content:"\f0f8"}
.icon-ambulance:before{content:"\f0f9"}
.icon-medkit:before{content:"\f0fa"}
.icon-fighter-jet:before{content:"\f0fb"}
.icon-beer:before{content:"\f0fc"}
.icon-h-sign:before{content:"\f0fd"}
.icon-plus-sign-alt:before{content:"\f0fe"}
.icon-double-angle-left:before{content:"\f100"}
.icon-double-angle-right:before{content:"\f101"}
.icon-double-angle-up:before{content:"\f102"}
.icon-double-angle-down:before{content:"\f103"}
.icon-angle-left:before{content:"\f104"}
.icon-angle-right:before{content:"\f105"}
.icon-angle-up:before{content:"\f106"}
.icon-angle-down:before{content:"\f107"}
.icon-desktop:before{content:"\f108"}
.icon-laptop:before{content:"\f109"}
.icon-tablet:before{content:"\f10a"}
.icon-mobile-phone:before{content:"\f10b"}
.icon-circle-blank:before{content:"\f10c"}
.icon-quote-left:before{content:"\f10d"}
.icon-quote-right:before{content:"\f10e"}
.icon-spinner:before{content:"\f110"}
.icon-circle:before{content:"\f111"}
.icon-mail-reply:before,.icon-reply:before{content:"\f112"}
.icon-github-alt:before{content:"\f113"}
.icon-folder-close-alt:before{content:"\f114"}
.icon-folder-open-alt:before{content:"\f115"}
.icon-expand-alt:before{content:"\f116"}
.icon-collapse-alt:before{content:"\f117"}
.icon-smile:before{content:"\f118"}
.icon-frown:before{content:"\f119"}
.icon-meh:before{content:"\f11a"}
.icon-gamepad:before{content:"\f11b"}
.icon-keyboard:before{content:"\f11c"}
.icon-flag-alt:before{content:"\f11d"}
.icon-flag-checkered:before{content:"\f11e"}
.icon-terminal:before{content:"\f120"}
.icon-code:before{content:"\f121"}
.icon-reply-all:before{content:"\f122"}
.icon-mail-reply-all:before{content:"\f122"}
.icon-star-half-full:before,.icon-star-half-empty:before{content:"\f123"}
.icon-location-arrow:before{content:"\f124"}
.icon-crop:before{content:"\f125"}
.icon-code-fork:before{content:"\f126"}
.icon-unlink:before{content:"\f127"}
.icon-question:before{content:"\f128"}
.icon-info:before{content:"\f129"}
.icon-exclamation:before{content:"\f12a"}
.icon-superscript:before{content:"\f12b"}
.icon-subscript:before{content:"\f12c"}
.icon-eraser:before{content:"\f12d"}
.icon-puzzle-piece:before{content:"\f12e"}
.icon-microphone:before{content:"\f130"}
.icon-microphone-off:before{content:"\f131"}
.icon-shield:before{content:"\f132"}
.icon-calendar-empty:before{content:"\f133"}
.icon-fire-extinguisher:before{content:"\f134"}
.icon-rocket:before{content:"\f135"}
.icon-maxcdn:before{content:"\f136"}
.icon-chevron-sign-left:before{content:"\f137"}
.icon-chevron-sign-right:before{content:"\f138"}
.icon-chevron-sign-up:before{content:"\f139"}
.icon-chevron-sign-down:before{content:"\f13a"}
.icon-html5:before{content:"\f13b"}
.icon-css3:before{content:"\f13c"}
.icon-anchor:before{content:"\f13d"}
.icon-unlock-alt:before{content:"\f13e"}
.icon-bullseye:before{content:"\f140"}
.icon-ellipsis-horizontal:before{content:"\f141"}
.icon-ellipsis-vertical:before{content:"\f142"}
.icon-rss-sign:before{content:"\f143"}
.icon-play-sign:before{content:"\f144"}
.icon-ticket:before{content:"\f145"}
.icon-minus-sign-alt:before{content:"\f146"}
.icon-check-minus:before{content:"\f147"}
.icon-level-up:before{content:"\f148"}
.icon-level-down:before{content:"\f149"}
.icon-check-sign:before{content:"\f14a"}
.icon-edit-sign:before{content:"\f14b"}
.icon-external-link-sign:before{content:"\f14c"}
.icon-share-sign:before{content:"\f14d"}
.icon-compass:before{content:"\f14e"}
.icon-collapse:before{content:"\f150"}
.icon-collapse-top:before{content:"\f151"}
.icon-expand:before{content:"\f152"}
.icon-euro:before,.icon-eur:before{content:"\f153"}
.icon-gbp:before{content:"\f154"}
.icon-dollar:before,.icon-usd:before{content:"\f155"}
.icon-rupee:before,.icon-inr:before{content:"\f156"}
.icon-yen:before,.icon-jpy:before{content:"\f157"}
.icon-renminbi:before,.icon-cny:before{content:"\f158"}
.icon-won:before,.icon-krw:before{content:"\f159"}
.icon-bitcoin:before,.icon-btc:before{content:"\f15a"}
.icon-file:before{content:"\f15b"}
.icon-file-text:before{content:"\f15c"}
.icon-sort-by-alphabet:before{content:"\f15d"}
.icon-sort-by-alphabet-alt:before{content:"\f15e"}
.icon-sort-by-attributes:before{content:"\f160"}
.icon-sort-by-attributes-alt:before{content:"\f161"}
.icon-sort-by-order:before{content:"\f162"}
.icon-sort-by-order-alt:before{content:"\f163"}
.icon-thumbs-up:before{content:"\f164"}
.icon-thumbs-down:before{content:"\f165"}
.icon-youtube-sign:before{content:"\f166"}
.icon-youtube:before{content:"\f167"}
.icon-xing:before{content:"\f168"}
.icon-xing-sign:before{content:"\f169"}
.icon-youtube-play:before{content:"\f16a"}
.icon-dropbox:before{content:"\f16b"}
.icon-stackexchange:before{content:"\f16c"}
.icon-instagram:before{content:"\f16d"}
.icon-flickr:before{content:"\f16e"}
.icon-adn:before{content:"\f170"}
.icon-bitbucket:before{content:"\f171"}
.icon-bitbucket-sign:before{content:"\f172"}
.icon-tumblr:before{content:"\f173"}
.icon-tumblr-sign:before{content:"\f174"}
.icon-long-arrow-down:before{content:"\f175"}
.icon-long-arrow-up:before{content:"\f176"}
.icon-long-arrow-left:before{content:"\f177"}
.icon-long-arrow-right:before{content:"\f178"}
.icon-apple:before{content:"\f179"}
.icon-windows:before{content:"\f17a"}
.icon-android:before{content:"\f17b"}
.icon-linux:before{content:"\f17c"}
.icon-dribbble:before{content:"\f17d"}
.icon-skype:before{content:"\f17e"}
.icon-foursquare:before{content:"\f180"}
.icon-trello:before{content:"\f181"}
.icon-female:before{content:"\f182"}
.icon-male:before{content:"\f183"}
.icon-gittip:before{content:"\f184"}
.icon-sun:before{content:"\f185"}
.icon-moon:before{content:"\f186"}
.icon-archive:before{content:"\f187"}
.icon-bug:before{content:"\f188"}
.icon-vk:before{content:"\f189"}
.icon-weibo:before{content:"\f18a"}
.icon-renren:before{content:"\f18b"}
code{color:#000}
pre{font-size:inherit;line-height:inherit}
.border-box-sizing{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}
.corner-all{border-radius:4px}
.hbox{display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
.hbox>*{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none}
.vbox{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
.vbox>*{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none}
.hbox.reverse,.vbox.reverse,.reverse{-webkit-box-direction:reverse;-moz-box-direction:reverse;box-direction:reverse;flex-direction:row-reverse}
.hbox.box-flex0,.vbox.box-flex0,.box-flex0{-webkit-box-flex:0;-moz-box-flex:0;box-flex:0;flex:none;width:auto}
.hbox.box-flex1,.vbox.box-flex1,.box-flex1{-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
.hbox.box-flex,.vbox.box-flex,.box-flex{-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
.hbox.box-flex2,.vbox.box-flex2,.box-flex2{-webkit-box-flex:2;-moz-box-flex:2;box-flex:2;flex:2}
.box-group1{-webkit-box-flex-group:1;-moz-box-flex-group:1;box-flex-group:1}
.box-group2{-webkit-box-flex-group:2;-moz-box-flex-group:2;box-flex-group:2}
.hbox.start,.vbox.start,.start{-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start}
.hbox.end,.vbox.end,.end{-webkit-box-pack:end;-moz-box-pack:end;box-pack:end;justify-content:flex-end}
.hbox.center,.vbox.center,.center{-webkit-box-pack:center;-moz-box-pack:center;box-pack:center;justify-content:center}
.hbox.align-start,.vbox.align-start,.align-start{-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}
.hbox.align-end,.vbox.align-end,.align-end{-webkit-box-align:end;-moz-box-align:end;box-align:end;align-items:flex-end}
.hbox.align-center,.vbox.align-center,.align-center{-webkit-box-align:center;-moz-box-align:center;box-align:center;align-items:center}
div.error{margin:2em;text-align:center}
div.error>h1{font-size:500%;line-height:normal}
div.error>p{font-size:200%;line-height:normal}
div.traceback-wrapper{text-align:left;max-width:800px;margin:auto}
body{background-color:#fff;position:absolute;left:0;right:0;top:0;bottom:0;overflow:visible}
div#header{display:none}
#ipython_notebook{padding-left:16px}
#noscript{width:auto;padding-top:16px;padding-bottom:16px;text-align:center;font-size:22px;color:#f00;font-weight:bold}
#ipython_notebook img{font-family:Verdana,"Helvetica Neue",Arial,Helvetica,Geneva,sans-serif;height:24px;text-decoration:none;color:#000}
#site{width:100%;display:none}
.ui-button .ui-button-text{padding:.2em .8em;font-size:77%}
input.ui-button{padding:.3em .9em}
.navbar span{margin-top:3px}
span#login_widget{float:right}
.nav-header{text-transform:none}
.navbar-nobg{background-color:transparent;background-image:none}
#header>span{margin-top:10px}
.modal_stretch{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;height:80%}.modal_stretch .modal-body{max-height:none;flex:1}
@media (min-width:768px){.modal{width:700px;margin-left:-350px}}.center-nav{display:inline-block;margin-bottom:-4px}
.alternate_upload{background-color:none;display:inline}
.alternate_upload.form{padding:0;margin:0}
.alternate_upload input.fileinput{background-color:#f00;position:relative;opacity:0;z-index:2;width:295px;margin-left:163px;cursor:pointer;height:26px}
ul#tabs{margin-bottom:4px}
ul#tabs a{padding-top:4px;padding-bottom:4px}
ul.breadcrumb a:focus,ul.breadcrumb a:hover{text-decoration:none}
ul.breadcrumb i.icon-home{font-size:16px;margin-right:4px}
ul.breadcrumb span{color:#5e5e5e}
.list_toolbar{padding:4px 0 4px 0}
.list_toolbar [class*="span"]{min-height:26px}
.list_header{font-weight:bold}
.list_container{margin-top:4px;margin-bottom:20px;border:1px solid #ababab;border-radius:4px}
.list_container>div{border-bottom:1px solid #ababab}.list_container>div:hover .list-item{background-color:#f00}
.list_container>div:last-child{border:none}
.list_item:hover .list_item{background-color:#ddd}
.list_item a{text-decoration:none}
.list_header>div,.list_item>div{padding-top:4px;padding-bottom:4px;padding-left:7px;padding-right:7px;height:22px;line-height:22px}
.item_name{line-height:22px;height:26px}
.item_icon{font-size:14px;color:#5e5e5e;margin-right:7px}
.item_buttons{line-height:1em}
.toolbar_info{height:26px;line-height:26px}
input.nbname_input,input.engine_num_input{padding-top:3px;padding-bottom:3px;height:14px;line-height:14px;margin:0}
input.engine_num_input{width:60px}
.highlight_text{color:#00f}
#project_name>.breadcrumb{padding:0;margin-bottom:0;background-color:transparent;font-weight:bold}
.folder_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f114"}
.notebook_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f02d"}
.ansibold{font-weight:bold}
.ansiblack{color:#000}
.ansired{color:#8b0000}
.ansigreen{color:#006400}
.ansiyellow{color:#a52a2a}
.ansiblue{color:#00008b}
.ansipurple{color:#9400d3}
.ansicyan{color:#4682b4}
.ansigray{color:#808080}
.ansibgblack{background-color:#000}
.ansibgred{background-color:#f00}
.ansibggreen{background-color:#008000}
.ansibgyellow{background-color:#ff0}
.ansibgblue{background-color:#00f}
.ansibgpurple{background-color:#f0f}
.ansibgcyan{background-color:#0ff}
.ansibggray{background-color:#808080}
div.cell{border:1px solid transparent;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}div.cell.selected{border-radius:4px;border:thin #ababab solid}
div.cell.edit_mode{border-radius:4px;border:thin #008000 solid}
div.cell{width:100%;padding:5px 5px 5px 0;margin:0;outline:none}
div.prompt{min-width:11ex;padding:.4em;margin:0;font-family:monospace;text-align:right;line-height:1.21429em}
@media (max-width:480px){div.prompt{text-align:left}}div.inner_cell{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
div.input_area{border:1px solid #cfcfcf;border-radius:4px;background:#f7f7f7;line-height:1.21429em}
div.prompt:empty{padding-top:0;padding-bottom:0}
div.input{page-break-inside:avoid;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
@media (max-width:480px){div.input{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}}div.input_prompt{color:#000080;border-top:1px solid transparent}
div.input_area>div.highlight{margin:.4em;border:none;padding:0;background-color:transparent}
div.input_area>div.highlight>pre{margin:0;border:none;padding:0;background-color:transparent}
.CodeMirror{line-height:1.21429em;height:auto;background:none;}
.CodeMirror-scroll{overflow-y:hidden;overflow-x:auto}
.CodeMirror-lines{padding:.4em}
.CodeMirror-linenumber{padding:0 8px 0 4px}
.CodeMirror-gutters{border-bottom-left-radius:4px;border-top-left-radius:4px}
.CodeMirror pre{padding:0;border:0;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
pre code{display:block;padding:.5em}
.highlight-base,pre code,pre .subst,pre .tag .title,pre .lisp .title,pre .clojure .built_in,pre .nginx .title{color:#000}
.highlight-string,pre .string,pre .constant,pre .parent,pre .tag .value,pre .rules .value,pre .rules .value .number,pre .preprocessor,pre .ruby .symbol,pre .ruby .symbol .string,pre .aggregate,pre .template_tag,pre .django .variable,pre .smalltalk .class,pre .addition,pre .flow,pre .stream,pre .bash .variable,pre .apache .tag,pre .apache .cbracket,pre .tex .command,pre .tex .special,pre .erlang_repl .function_or_atom,pre .markdown .header{color:#ba2121}
.highlight-comment,pre .comment,pre .annotation,pre .template_comment,pre .diff .header,pre .chunk,pre .markdown .blockquote{color:#408080;font-style:italic}
.highlight-number,pre .number,pre .date,pre .regexp,pre .literal,pre .smalltalk .symbol,pre .smalltalk .char,pre .go .constant,pre .change,pre .markdown .bullet,pre .markdown .link_url{color:#080}
pre .label,pre .javadoc,pre .ruby .string,pre .decorator,pre .filter .argument,pre .localvars,pre .array,pre .attr_selector,pre .important,pre .pseudo,pre .pi,pre .doctype,pre .deletion,pre .envvar,pre .shebang,pre .apache .sqbracket,pre .nginx .built_in,pre .tex .formula,pre .erlang_repl .reserved,pre .prompt,pre .markdown .link_label,pre .vhdl .attribute,pre .clojure .attribute,pre .coffeescript .property{color:#88f}
.highlight-keyword,pre .keyword,pre .id,pre .phpdoc,pre .aggregate,pre .css .tag,pre .javadoctag,pre .phpdoc,pre .yardoctag,pre .smalltalk .class,pre .winutils,pre .bash .variable,pre .apache .tag,pre .go .typename,pre .tex .command,pre .markdown .strong,pre .request,pre .status{color:#008000;font-weight:bold}
.highlight-builtin,pre .built_in{color:#008000}
pre .markdown .emphasis{font-style:italic}
pre .nginx .built_in{font-weight:normal}
pre .coffeescript .javascript,pre .javascript .xml,pre .tex .formula,pre .xml .javascript,pre .xml .vbscript,pre .xml .css,pre .xml .cdata{opacity:.5}
.cm-s-ipython span.cm-variable{color:#000}
.cm-s-ipython span.cm-keyword{color:#008000;font-weight:bold}
.cm-s-ipython span.cm-number{color:#080}
.cm-s-ipython span.cm-comment{color:#408080;font-style:italic}
.cm-s-ipython span.cm-string{color:#ba2121}
.cm-s-ipython span.cm-builtin{color:#008000}
.cm-s-ipython span.cm-error{color:#f00}
.cm-s-ipython span.cm-operator{color:#a2f;font-weight:bold}
.cm-s-ipython span.cm-meta{color:#a2f}
.cm-s-ipython span.cm-tab{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);background-position:right;background-repeat:no-repeat}
div.output_wrapper{position:relative;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
div.output_scroll{height:24em;width:100%;overflow:auto;border-radius:4px;-webkit-box-shadow:inset 0 2px 8px rgba(0,0,0,0.8);-moz-box-shadow:inset 0 2px 8px rgba(0,0,0,0.8);box-shadow:inset 0 2px 8px rgba(0,0,0,0.8);display:block}
div.output_collapsed{margin:0;padding:0;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
div.out_prompt_overlay{height:100%;padding:0 .4em;position:absolute;border-radius:4px}
div.out_prompt_overlay:hover{-webkit-box-shadow:inset 0 0 1px #000;-moz-box-shadow:inset 0 0 1px #000;box-shadow:inset 0 0 1px #000;background:rgba(240,240,240,0.5)}
div.output_prompt{color:#8b0000}
div.output_area{padding:0;page-break-inside:avoid;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}div.output_area .MathJax_Display{text-align:left !important}
div.output_area .rendered_html table{margin-left:0;margin-right:0}
div.output_area .rendered_html img{margin-left:0;margin-right:0}
.output{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
@media (max-width:480px){div.output_area{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}}div.output_area pre{margin:0;padding:0;border:0;vertical-align:baseline;color:#000;background-color:transparent;border-radius:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}
div.output_subarea{padding:.4em .4em 0 .4em;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
div.output_text{text-align:left;color:#000;line-height:1.21429em}
div.output_stderr{background:#fdd;}
div.output_latex{text-align:left}
div.output_javascript:empty{padding:0}
.js-error{color:#8b0000}
div.raw_input_container{font-family:monospace;padding-top:5px}
span.raw_input_prompt{}
input.raw_input{font-family:inherit;font-size:inherit;color:inherit;width:auto;vertical-align:baseline;padding:0 .25em;margin:0 .25em}
input.raw_input:focus{box-shadow:none}
p.p-space{margin-bottom:10px}
.rendered_html{color:#000;}.rendered_html em{font-style:italic}
.rendered_html strong{font-weight:bold}
.rendered_html u{text-decoration:underline}
.rendered_html :link{text-decoration:underline}
.rendered_html :visited{text-decoration:underline}
.rendered_html h1{font-size:185.7%;margin:1.08em 0 0 0;font-weight:bold;line-height:1}
.rendered_html h2{font-size:157.1%;margin:1.27em 0 0 0;font-weight:bold;line-height:1}
.rendered_html h3{font-size:128.6%;margin:1.55em 0 0 0;font-weight:bold;line-height:1}
.rendered_html h4{font-size:100%;margin:2em 0 0 0;font-weight:bold;line-height:1}
.rendered_html h5{font-size:100%;margin:2em 0 0 0;font-weight:bold;line-height:1;font-style:italic}
.rendered_html h6{font-size:100%;margin:2em 0 0 0;font-weight:bold;line-height:1;font-style:italic}
.rendered_html h1:first-child{margin-top:.538em}
.rendered_html h2:first-child{margin-top:.636em}
.rendered_html h3:first-child{margin-top:.777em}
.rendered_html h4:first-child{margin-top:1em}
.rendered_html h5:first-child{margin-top:1em}
.rendered_html h6:first-child{margin-top:1em}
.rendered_html ul{list-style:disc;margin:0 2em}
.rendered_html ul ul{list-style:square;margin:0 2em}
.rendered_html ul ul ul{list-style:circle;margin:0 2em}
.rendered_html ol{list-style:decimal;margin:0 2em}
.rendered_html ol ol{list-style:upper-alpha;margin:0 2em}
.rendered_html ol ol ol{list-style:lower-alpha;margin:0 2em}
.rendered_html ol ol ol ol{list-style:lower-roman;margin:0 2em}
.rendered_html ol ol ol ol ol{list-style:decimal;margin:0 2em}
.rendered_html *+ul{margin-top:1em}
.rendered_html *+ol{margin-top:1em}
.rendered_html hr{color:#000;background-color:#000}
.rendered_html pre{margin:1em 2em}
.rendered_html pre,.rendered_html code{border:0;background-color:#fff;color:#000;font-size:100%;padding:0}
.rendered_html blockquote{margin:1em 2em}
.rendered_html table{margin-left:auto;margin-right:auto;border:1px solid #000;border-collapse:collapse}
.rendered_html tr,.rendered_html th,.rendered_html td{border:1px solid #000;border-collapse:collapse;margin:1em 2em}
.rendered_html td,.rendered_html th{text-align:left;vertical-align:middle;padding:4px}
.rendered_html th{font-weight:bold}
.rendered_html *+table{margin-top:1em}
.rendered_html p{text-align:justify}
.rendered_html *+p{margin-top:1em}
.rendered_html img{display:block;margin-left:auto;margin-right:auto}
.rendered_html *+img{margin-top:1em}
div.text_cell{padding:5px 5px 5px 0;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
@media (max-width:480px){div.text_cell>div.prompt{display:none}}div.text_cell_render{outline:none;resize:none;width:inherit;border-style:none;padding:.5em .5em .5em .4em;color:#000}
a.anchor-link:link{text-decoration:none;padding:0 20px;visibility:hidden}
h1:hover .anchor-link,h2:hover .anchor-link,h3:hover .anchor-link,h4:hover .anchor-link,h5:hover .anchor-link,h6:hover .anchor-link{visibility:visible}
div.cell.text_cell.rendered{padding:0}
.widget-area{page-break-inside:avoid;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}.widget-area .widget-subarea{padding:.44em .4em .4em 1px;margin-left:6px;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;-webkit-box-flex:2;-moz-box-flex:2;box-flex:2;flex:2;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}
.widget-hlabel{min-width:10ex;padding-right:8px;padding-top:3px;text-align:right;vertical-align:text-top}
.widget-vlabel{padding-bottom:5px;text-align:center;vertical-align:text-bottom}
.widget-hreadout{padding-left:8px;padding-top:3px;text-align:left;vertical-align:text-top}
.widget-vreadout{padding-top:5px;text-align:center;vertical-align:text-top}
.slide-track{border:1px solid #ccc;background:#fff;border-radius:4px;}
.widget-hslider{padding-left:8px;padding-right:5px;overflow:visible;width:348px;height:5px;max-height:5px;margin-top:11px;margin-bottom:10px;border:1px solid #ccc;background:#fff;border-radius:4px;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}.widget-hslider .ui-slider{border:0 !important;background:none !important;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}.widget-hslider .ui-slider .ui-slider-handle{width:14px !important;height:28px !important;margin-top:-8px !important}
.widget-vslider{padding-bottom:8px;overflow:visible;width:5px;max-width:5px;height:250px;margin-left:12px;border:1px solid #ccc;background:#fff;border-radius:4px;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}.widget-vslider .ui-slider{border:0 !important;background:none !important;margin-left:-4px;margin-top:5px;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}.widget-vslider .ui-slider .ui-slider-handle{width:28px !important;height:14px !important;margin-left:-9px}
.widget-text{width:350px;margin:0 !important}
.widget-listbox{width:364px;margin-bottom:0}
.widget-numeric-text{width:150px;margin:0 !important}
.widget-progress{width:363px}.widget-progress .bar{-webkit-transition:none;-moz-transition:none;-ms-transition:none;-o-transition:none;transition:none}
.widget-combo-btn{min-width:138px;}
.widget-box{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}
.widget-hbox{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
.widget-hbox-single{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch;height:30px}
.widget-vbox{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch}
.widget-vbox-single{margin:5px;-webkit-box-pack:start;-moz-box-pack:start;box-pack:start;justify-content:flex-start;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start;display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;width:30px}
.widget-modal{overflow:hidden;position:absolute !important;top:0;left:0;margin-left:0 !important}
.widget-modal-body{max-height:none !important}
.widget-container{box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;-webkit-box-align:start;-moz-box-align:start;box-align:start;align-items:flex-start}
.widget-radio-box{display:-webkit-box;-webkit-box-orient:vertical;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:vertical;-moz-box-align:stretch;display:box;box-orient:vertical;box-align:stretch;display:flex;flex-direction:column;align-items:stretch;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;padding-top:4px}
.docked-widget-modal{overflow:hidden;position:relative !important;top:0 !important;left:0 !important;margin-left:0 !important}
body{background-color:#fff}
body.notebook_app{overflow:hidden}
@media (max-width:767px){body.notebook_app{padding-left:0;padding-right:0}}span#notebook_name{height:1em;line-height:1em;padding:3px;border:none;font-size:146.5%}
div#notebook_panel{margin:0 0 0 0;padding:0;-webkit-box-shadow:0 -1px 10px rgba(0,0,0,0.1);-moz-box-shadow:0 -1px 10px rgba(0,0,0,0.1);box-shadow:0 -1px 10px rgba(0,0,0,0.1)}
div#notebook{font-size:14px;line-height:20px;overflow-y:scroll;overflow-x:auto;width:100%;padding:1em 0 1em 0;margin:0;border-top:1px solid #ababab;outline:none;box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box}
div.ui-widget-content{border:1px solid #ababab;outline:none}
pre.dialog{background-color:#f7f7f7;border:1px solid #ddd;border-radius:4px;padding:.4em;padding-left:2em}
p.dialog{padding:.2em}
pre,code,kbd,samp{white-space:pre-wrap}
#fonttest{font-family:monospace}
p{margin-bottom:0}
.end_space{height:200px}
.celltoolbar{border:thin solid #cfcfcf;border-bottom:none;background:#eee;border-radius:3px 3px 0 0;width:100%;-webkit-box-pack:end;height:22px;display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch;-webkit-box-direction:reverse;-moz-box-direction:reverse;box-direction:reverse;flex-direction:row-reverse}
.ctb_hideshow{display:none;vertical-align:bottom;padding-right:2px}
.celltoolbar>div{padding-top:0}
.ctb_global_show .ctb_show.ctb_hideshow{display:block}
.ctb_global_show .ctb_show+.input_area,.ctb_global_show .ctb_show+div.text_cell_input{border-top-right-radius:0;border-top-left-radius:0}
.celltoolbar .button_container select{margin:10px;margin-top:1px;margin-bottom:0;padding:0;font-size:87%;width:auto;display:inline-block;height:18px;line-height:18px;vertical-align:top}
.celltoolbar label{display:inline-block;height:15px;line-height:15px;vertical-align:top}
.celltoolbar label span{font-size:85%}
.celltoolbar input[type=checkbox]{margin:0;margin-left:4px;margin-right:4px}
.celltoolbar .ui-button{border:none;vertical-align:top;height:20px;min-width:30px}
.completions{position:absolute;z-index:10;overflow:hidden;border:1px solid #ababab;border-radius:4px;-webkit-box-shadow:0 6px 10px -1px #adadad;-moz-box-shadow:0 6px 10px -1px #adadad;box-shadow:0 6px 10px -1px #adadad}
.completions select{background:#fff;outline:none;border:none;padding:0;margin:0;overflow:auto;font-family:monospace;font-size:110%;color:#000;width:auto}
.completions select option.context{color:#0064cd}
#menubar .navbar-inner{min-height:28px;border-top:1px;border-radius:0 0 4px 4px}
#menubar .navbar{margin-bottom:8px}
.nav-wrapper{border-bottom:1px solid #d4d4d4}
#menubar li.dropdown{line-height:12px}
i.menu-icon{padding-top:4px}
ul#help_menu li a{overflow:hidden;padding-right:2.2em}ul#help_menu li a i{margin-right:-1.2em}
#notification_area{z-index:10}
.indicator_area{color:#777;padding:4px 3px;margin:0;width:11px;z-index:10;text-align:center}
#kernel_indicator{margin-right:-16px}
.edit_mode_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f040"}
.command_mode_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:' '}
.kernel_idle_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f10c"}
.kernel_busy_icon:before{font-family:FontAwesome;font-weight:normal;font-style:normal;text-decoration:inherit;-webkit-font-smoothing:antialiased;*margin-right:.3em;content:"\f111"}
.notification_widget{color:#777;padding:1px 12px;margin:2px 4px;z-index:10;border:1px solid #ccc;border-radius:4px;background:rgba(240,240,240,0.5)}.notification_widget.span{padding-right:2px}
div#pager_splitter{height:8px}
#pager-container{position:relative;padding:15px 0}
div#pager{font-size:14px;line-height:20px;overflow:auto;display:none}div#pager pre{line-height:1.21429em;color:#000;background-color:#f7f7f7;padding:.4em}
.quickhelp{display:-webkit-box;-webkit-box-orient:horizontal;-webkit-box-align:stretch;display:-moz-box;-moz-box-orient:horizontal;-moz-box-align:stretch;display:box;box-orient:horizontal;box-align:stretch;display:flex;flex-direction:row;align-items:stretch}
.shortcut_key{display:inline-block;width:20ex;text-align:right;font-family:monospace}
.shortcut_descr{display:inline-block;-webkit-box-flex:1;-moz-box-flex:1;box-flex:1;flex:1}
span#save_widget{padding:0 5px;margin-top:12px}
span#checkpoint_status,span#autosave_status{font-size:small}
@media (max-width:767px){span#save_widget{font-size:small} span#checkpoint_status,span#autosave_status{font-size:x-small}}@media (max-width:767px){span#checkpoint_status,span#autosave_status{display:none}}@media (min-width:768px) and (max-width:979px){span#checkpoint_status{display:none} span#autosave_status{font-size:x-small}}.toolbar{padding:0 10px;margin-top:-5px}.toolbar select,.toolbar label{width:auto;height:26px;vertical-align:middle;margin-right:2px;margin-bottom:0;display:inline;font-size:92%;margin-left:.3em;margin-right:.3em;padding:0;padding-top:3px}
.toolbar .btn{padding:2px 8px}
.toolbar .btn-group{margin-top:0}
.toolbar-inner{border:none !important;-webkit-box-shadow:none !important;-moz-box-shadow:none !important;box-shadow:none !important}
#maintoolbar{margin-bottom:0}
@-moz-keyframes fadeOut{from{opacity:1} to{opacity:0}}@-webkit-keyframes fadeOut{from{opacity:1} to{opacity:0}}@-moz-keyframes fadeIn{from{opacity:0} to{opacity:1}}@-webkit-keyframes fadeIn{from{opacity:0} to{opacity:1}}.bigtooltip{overflow:auto;height:200px;-webkit-transition-property:height;-webkit-transition-duration:500ms;-moz-transition-property:height;-moz-transition-duration:500ms;transition-property:height;transition-duration:500ms}
.smalltooltip{-webkit-transition-property:height;-webkit-transition-duration:500ms;-moz-transition-property:height;-moz-transition-duration:500ms;transition-property:height;transition-duration:500ms;text-overflow:ellipsis;overflow:hidden;height:80px}
.tooltipbuttons{position:absolute;padding-right:15px;top:0;right:0}
.tooltiptext{padding-right:30px}
.ipython_tooltip{max-width:700px;-webkit-animation:fadeOut 400ms;-moz-animation:fadeOut 400ms;animation:fadeOut 400ms;-webkit-animation:fadeIn 400ms;-moz-animation:fadeIn 400ms;animation:fadeIn 400ms;vertical-align:middle;background-color:#f7f7f7;overflow:visible;border:#ababab 1px solid;outline:none;padding:3px;margin:0;padding-left:7px;font-family:monospace;min-height:50px;-moz-box-shadow:0 6px 10px -1px #adadad;-webkit-box-shadow:0 6px 10px -1px #adadad;box-shadow:0 6px 10px -1px #adadad;border-radius:4px;position:absolute;z-index:2}.ipython_tooltip a{float:right}
.ipython_tooltip .tooltiptext pre{border:0;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0;font-size:100%;background-color:#f7f7f7}
.pretooltiparrow{left:0;margin:0;top:-16px;width:40px;height:16px;overflow:hidden;position:absolute}
.pretooltiparrow:before{background-color:#f7f7f7;border:1px #ababab solid;z-index:11;content:"";position:absolute;left:15px;top:10px;width:25px;height:25px;-webkit-transform:rotate(45deg);-moz-transform:rotate(45deg);-ms-transform:rotate(45deg);-o-transform:rotate(45deg)}

    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}

@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration -->

</head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[242]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="o">%</span><span class="k">matplotlib</span> <span class="n">inline</span> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[243]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">pylab</span> <span class="kn">as</span> <span class="nn">py</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[244]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[245]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="kn">from</span> <span class="nn">graph_tool.all</span> <span class="kn">import</span> <span class="o">*</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Creating-a-random-Undirected-Graph-for-evaluation">Creating a random Undirected Graph for evaluation<a class="anchor-link" href="#Creating-a-random-Undirected-Graph-for-evaluation">&#182;</a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[246]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">=</span><span class="n">Graph</span><span class="p">(</span><span class="n">directed</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[247]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">5</span><span class="p">):</span>
    <span class="n">g</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">()</span> <span class="p">;</span>
    <span class="k">print</span> <span class="s">&quot;added no&quot;</span><span class="p">,</span><span class="n">i</span><span class="p">;</span>
<span class="s">&quot;End&quot;</span> 
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>
added no 0
added no 1
added no 2
added no 3
added no 4

</pre>
</div>
</div>

<div class="output_area"><div class="prompt output_prompt">
    Out[247]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&apos;End&apos;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[248]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">0</span><span class="p">),</span> <span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>
<span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>
<span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">2</span><span class="p">),</span> <span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">3</span><span class="p">))</span>
<span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">4</span><span class="p">),</span> <span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">3</span><span class="p">))</span>
<span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">4</span><span class="p">))</span>
<span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">2</span><span class="p">),</span> <span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">4</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">
    Out[248]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&lt;Edge object with source &apos;2&apos; and target &apos;4&apos; at 0x7f96f6f37f28&gt;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[249]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">graph_draw</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">vertex_text</span><span class="o">=</span><span class="n">g</span><span class="o">.</span><span class="n">vertex_index</span><span class="p">,</span> <span class="n">vertex_font_size</span><span class="o">=</span><span class="mi">18</span><span class="p">,</span><span class="n">output_size</span><span class="o">=</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span> <span class="mi">200</span><span class="p">),</span> <span class="n">output</span><span class="o">=</span><span class="s">&quot;two-nodes.png&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
8zyj59+QAgCOnBzLxHvvGRHY9mG07sWXOw0QmT/SIceM8bDb08DMa4bjUHHls61XSRs0TXvCtFpn
s80aTlzxxRzHs7+rPXGC1IE/rQ6Zifj+s2+9Nf2cbyzM+GSw4mO/bOx0HJbTqcUvm5sjrZYwrJYw
AY/3yxUpSj/q9XyQY7POREvraH1vbdL60h8P0NFJ+33Fuk7x+dePNEfm6dKfWguipxYvXjxkckYp
yjG9XkDH7/c/CqIN0uurN0bl2+M3zc/nblYa6op0u/XYTV8ZJfNyrezzHhCa9s7hw4cr+nocRRkM
fZ2T7gOwFKY5UQQCuRQI2iwbNjbq729p6yl3K+s6GedNTzGKpqdLryfOPl89NO3DeDy+5J577ul7
7ilFGQR9zmqyYsUKezwe/yEBlyMS8YtoexpCYant2RPSd+8JUUtLksJRgwyD2e3WZZrfap41zm2e
Pc7Lbrdgp6OJXa5WBv5ss9l+dLS3XlGGpFPNi0VLly69RtO0JTDNLGpv9yGR8FDScDBzx7ouzMxE
REQMix5lqzXMDkcAmlZPRE8sWrTodXSeqEFRhozTyqz48MMPO5xO53wiuhTABJZSI9PUwUczKxIZ
rGkGdaTA305Ef05JSXm+N2l+FGUo6Lc1+crLyzOJqEgIkcrMKUBHShwhRGMsFtui+jgURVEURVEU
RVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEU
RVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEURVEU
RemN/w+odgxiQv5a6QAAAABJRU5ErkJggg==
"
>
</div>

</div>

<div class="output_area"><div class="prompt output_prompt">
    Out[249]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&lt;PropertyMap object with key type &apos;Vertex&apos; and value type &apos;vector&lt;double&gt;&apos;, for Graph 0x7f96f6e6a390, at 0x7f96f6f9fd10&gt;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[250]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">3</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">
    Out[250]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&lt;Edge object with source &apos;1&apos; and target &apos;3&apos; at 0x7f96f6e5a3e0&gt;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[251]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">graph_draw</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">vertex_text</span><span class="o">=</span><span class="n">g</span><span class="o">.</span><span class="n">vertex_index</span><span class="p">,</span> <span class="n">vertex_font_size</span><span class="o">=</span><span class="mi">18</span><span class="p">,</span><span class="n">output_size</span><span class="o">=</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span> <span class="mi">200</span><span class="p">),</span> <span class="n">output</span><span class="o">=</span><span class="s">&quot;two-nodes.png&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
TkSuQmCC
"
>
</div>

</div>

<div class="output_area"><div class="prompt output_prompt">
    Out[251]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&lt;PropertyMap object with key type &apos;Vertex&apos; and value type &apos;vector&lt;double&gt;&apos;, for Graph 0x7f96f6e6a390, at 0x7f96f6f9f290&gt;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[252]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">(</span><span class="mi">5</span><span class="p">);</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[253]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">graph_draw</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">vertex_text</span><span class="o">=</span><span class="n">g</span><span class="o">.</span><span class="n">vertex_index</span><span class="p">,</span> <span class="n">vertex_font_size</span><span class="o">=</span><span class="mi">18</span><span class="p">,</span><span class="n">output_size</span><span class="o">=</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span> <span class="mi">200</span><span class="p">),</span> <span class="n">output</span><span class="o">=</span><span class="s">&quot;two-nodes.png&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
rkJggg==
"
>
</div>

</div>

<div class="output_area"><div class="prompt output_prompt">
    Out[253]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&lt;PropertyMap object with key type &apos;Vertex&apos; and value type &apos;vector&lt;double&gt;&apos;, for Graph 0x7f96f6e6a390, at 0x7f96f6f9f250&gt;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[254]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">7</span><span class="p">),</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">4</span><span class="p">));</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[255]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">8</span><span class="p">),</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">3</span><span class="p">));</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[256]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">2</span><span class="p">),</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">5</span><span class="p">));</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[257]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">6</span><span class="p">),</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">9</span><span class="p">));</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[258]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">g</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">5</span><span class="p">),</span><span class="n">g</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="mi">6</span><span class="p">));</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[259]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">graph_draw</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">vertex_text</span><span class="o">=</span><span class="n">g</span><span class="o">.</span><span class="n">vertex_index</span><span class="p">,</span> <span class="n">vertex_font_size</span><span class="o">=</span><span class="mi">18</span><span class="p">,</span><span class="n">output_size</span><span class="o">=</span><span class="p">(</span><span class="mi">200</span><span class="p">,</span> <span class="mi">200</span><span class="p">),</span> <span class="n">output</span><span class="o">=</span><span class="s">&quot;two-nodes.png&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area"><div class="prompt output_prompt">
    Out[259]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&lt;PropertyMap object with key type &apos;Vertex&apos; and value type &apos;vector&lt;double&gt;&apos;, for Graph 0x7f96f6e6a390, at 0x7f96f6f9f490&gt;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Subroutine-used-by-maxdsubgraph-for-modification-of-flow-capacities">Subroutine used by maxdsubgraph for modification of flow capacities<a class="anchor-link" href="#Subroutine-used-by-maxdsubgraph-for-modification-of-flow-capacities">&#182;</a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[260]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="k">def</span> <span class="nf">modifycap</span><span class="p">(</span><span class="n">g</span><span class="p">,</span><span class="n">s</span><span class="p">,</span><span class="n">t</span><span class="p">,</span><span class="n">go</span><span class="p">,</span><span class="n">gn</span><span class="p">,</span><span class="n">cap</span><span class="p">):</span>
    
    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">g</span><span class="o">.</span><span class="n">edges</span><span class="p">():</span>
        <span class="k">if</span>  <span class="n">e</span><span class="o">.</span><span class="n">target</span><span class="p">()</span><span class="o">==</span><span class="n">t</span><span class="p">:</span>    
            <span class="n">cap</span><span class="p">[</span><span class="n">e</span><span class="p">]</span><span class="o">=</span><span class="n">cap</span><span class="p">[</span><span class="n">e</span><span class="p">]</span><span class="o">-</span><span class="mi">2</span><span class="o">*</span><span class="n">go</span><span class="o">+</span><span class="mi">2</span><span class="o">*</span><span class="n">gn</span>
        <span class="s">&quot;end&quot;</span>
    <span class="s">&quot;end for&quot;</span>
    
    
<span class="s">&quot;end func&quot;</span>
        
        
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">
    Out[260]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&apos;end func&apos;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Subroutine-which-filters-off-unwanted-nodes-using-the-Maxflow-min-cut-theoram">Subroutine which filters off unwanted nodes using the Maxflow min cut theoram<a class="anchor-link" href="#Subroutine-which-filters-off-unwanted-nodes-using-the-Maxflow-min-cut-theoram">&#182;</a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[266]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="k">def</span> <span class="nf">maxdsubgraph</span><span class="p">(</span><span class="n">g</span><span class="p">,</span><span class="n">s</span><span class="p">,</span><span class="n">t</span><span class="p">,</span><span class="n">m</span><span class="p">,</span><span class="n">n</span><span class="p">,</span><span class="n">cap</span><span class="p">):</span>
    <span class="n">go</span><span class="o">=</span><span class="mf">0.0</span><span class="p">;</span>
    <span class="n">l</span><span class="o">=</span><span class="mf">0.0</span><span class="p">;</span>
    <span class="n">u</span><span class="o">=</span><span class="n">m</span><span class="p">;</span>
    <span class="n">b</span><span class="o">=</span><span class="mf">1.0</span><span class="o">/</span><span class="p">(</span><span class="n">n</span><span class="o">*</span><span class="p">(</span><span class="n">n</span><span class="o">-</span><span class="mi">1</span><span class="p">));</span>
    <span class="n">res</span><span class="o">=-</span><span class="mi">123</span><span class="p">;</span>

    <span class="k">print</span> <span class="s">&quot;Inside MaxdSubgraph&quot;</span><span class="p">;</span>
    
    
    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">g</span><span class="o">.</span><span class="n">edges</span><span class="p">():</span>
        <span class="k">print</span> <span class="n">cap</span><span class="p">[</span><span class="n">e</span><span class="p">],</span><span class="n">e</span><span class="o">.</span><span class="n">source</span><span class="p">(),</span><span class="n">e</span><span class="o">.</span><span class="n">target</span><span class="p">();</span>
    <span class="s">&quot;end for&quot;</span>
    
    
    
    
    
    <span class="k">while</span> <span class="p">(</span><span class="n">u</span><span class="o">-</span><span class="n">l</span><span class="p">)</span><span class="o">&gt;</span><span class="n">b</span> <span class="p">:</span>
        
        <span class="k">print</span> <span class="s">&quot;value of l&quot;</span><span class="p">,</span><span class="n">l</span><span class="p">,</span><span class="s">&quot;value of u&quot;</span><span class="p">,</span><span class="n">u</span><span class="p">,</span><span class="s">&quot;value of b&quot;</span><span class="p">,</span><span class="n">b</span><span class="p">;</span>
        
        <span class="n">gn</span><span class="o">=</span><span class="p">(</span><span class="n">u</span><span class="o">+</span><span class="n">l</span><span class="p">)</span><span class="o">/</span><span class="mi">2</span><span class="p">;</span>
        
        <span class="n">modifycap</span><span class="p">(</span><span class="n">g</span><span class="p">,</span><span class="n">s</span><span class="p">,</span><span class="n">t</span><span class="p">,</span><span class="n">go</span><span class="p">,</span><span class="n">gn</span><span class="p">,</span><span class="n">cap</span><span class="p">);</span>
        
        <span class="k">print</span> <span class="s">&quot;yeah done with while&quot;</span><span class="p">;</span>
        
        <span class="c">#&quot;&quot;&quot;</span>
        
        
        <span class="c">#get cut</span>
        <span class="c">#s=g.vertex(m);</span>
        <span class="c">#t=g.vertex(m+1);</span>
        
        
        <span class="n">res23</span> <span class="o">=</span> <span class="n">push_relabel_max_flow</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">s</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">cap</span><span class="p">);</span>
        
        <span class="c">#&quot;&quot;&quot;</span>
        <span class="n">part</span> <span class="o">=</span> <span class="n">min_st_cut</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">s</span><span class="p">,</span> <span class="n">cap</span><span class="p">,</span> <span class="n">res23</span><span class="p">);</span>
        <span class="c">#</span>
        
        <span class="n">g</span><span class="o">.</span><span class="n">set_vertex_filter</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="n">inverted</span><span class="o">=</span><span class="bp">False</span><span class="p">);</span>
        
        
        
        
        <span class="k">if</span> <span class="n">g</span><span class="o">.</span><span class="n">num_vertices</span><span class="p">()</span><span class="o">==</span><span class="mi">1</span><span class="p">:</span>
            <span class="k">print</span> <span class="s">&quot;u reduced&quot;</span><span class="p">;</span>
            <span class="n">u</span><span class="o">=</span><span class="n">gn</span><span class="p">;</span>
            
        <span class="k">else</span> <span class="p">:</span>
            <span class="k">print</span> <span class="s">&quot;l increased&quot;</span><span class="p">;</span>
            <span class="n">l</span><span class="o">=</span><span class="n">gn</span><span class="p">;</span>
            <span class="n">res</span><span class="o">=</span><span class="n">part</span><span class="p">;</span>
        <span class="s">&quot;end if&quot;</span>
        <span class="n">go</span><span class="o">=</span><span class="n">gn</span><span class="p">;</span>
        <span class="n">g</span><span class="o">.</span><span class="n">clear_filters</span><span class="p">();</span>
        <span class="c">#&quot;&quot;&quot;</span>
    <span class="s">&quot;end while&quot;</span>
    <span class="k">if</span><span class="p">(</span><span class="n">res</span><span class="o">!=-</span><span class="mi">123</span><span class="p">):</span>
        <span class="n">g</span><span class="o">.</span><span class="n">set_vertex_filter</span><span class="p">(</span><span class="n">res</span><span class="p">,</span><span class="n">inverted</span><span class="o">=</span><span class="bp">False</span><span class="p">);</span>
    <span class="s">&quot;end if&quot;</span>
    

<span class="s">&quot;end func&quot;</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">
    Out[266]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&apos;end func&apos;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Worker-Function-:-Sets-up-thr-priliminary-G-graph-with-dual-edges-and-capacity-1">Worker Function : Sets up thr priliminary G graph with dual edges and capacity 1<a class="anchor-link" href="#Worker-Function-:-Sets-up-thr-priliminary-G-graph-with-dual-edges-and-capacity-1">&#182;</a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[262]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="k">def</span> <span class="nf">dsg</span><span class="p">(</span><span class="n">g</span><span class="p">,</span><span class="n">m</span><span class="p">,</span><span class="n">n</span><span class="p">):</span>
    
    <span class="k">print</span> <span class="s">&quot;m &quot;</span><span class="p">,</span><span class="n">m</span><span class="p">,</span><span class="s">&quot;n&quot;</span><span class="p">,</span><span class="n">n</span><span class="p">,</span><span class="s">&quot;</span><span class="se">\n\n\n</span><span class="s">&quot;</span><span class="p">;</span>
    
    <span class="n">G</span><span class="o">=</span><span class="n">Graph</span><span class="p">();</span>
    
    <span class="n">G</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">(</span><span class="n">n</span><span class="p">);</span>
    
    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">g</span><span class="o">.</span><span class="n">edges</span><span class="p">():</span>
        <span class="n">G</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">source</span><span class="p">(),</span><span class="n">e</span><span class="o">.</span><span class="n">target</span><span class="p">());</span>
        <span class="n">G</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">target</span><span class="p">(),</span><span class="n">e</span><span class="o">.</span><span class="n">source</span><span class="p">());</span>
    <span class="s">&quot;End for&quot;</span>
    
    <span class="n">s</span><span class="o">=</span><span class="n">G</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">();</span>
    <span class="n">t</span><span class="o">=</span><span class="n">G</span><span class="o">.</span><span class="n">add_vertex</span><span class="p">();</span>
    
    
  
    
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">n</span><span class="p">):</span>
        <span class="n">G</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">s</span><span class="p">,</span><span class="n">G</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="n">i</span><span class="p">));</span>
        <span class="n">G</span><span class="o">.</span><span class="n">add_edge</span><span class="p">(</span><span class="n">G</span><span class="o">.</span><span class="n">vertex</span><span class="p">(</span><span class="n">i</span><span class="p">),</span><span class="n">t</span><span class="p">);</span>
    <span class="s">&quot;End For&quot;</span>
    
    
    <span class="n">cap</span> <span class="o">=</span> <span class="n">G</span><span class="o">.</span><span class="n">new_edge_property</span><span class="p">(</span><span class="s">&quot;float&quot;</span><span class="p">)</span>                

    
    
    
    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">G</span><span class="o">.</span><span class="n">edges</span><span class="p">():</span>
        <span class="k">print</span> <span class="s">&quot;Source&quot;</span><span class="p">,</span><span class="n">e</span><span class="o">.</span><span class="n">source</span><span class="p">(),</span><span class="s">&quot;target&quot;</span><span class="p">,</span><span class="n">e</span><span class="o">.</span><span class="n">target</span><span class="p">();</span>
        
        <span class="k">if</span> <span class="n">e</span><span class="o">.</span><span class="n">source</span><span class="p">()</span><span class="o">==</span><span class="n">s</span><span class="p">:</span>
 <span class="c">#           print &quot;found source&quot;;</span>
            <span class="n">cap</span><span class="p">[</span><span class="n">e</span><span class="p">]</span><span class="o">=</span><span class="n">m</span><span class="p">;</span>
        <span class="k">elif</span> <span class="n">e</span><span class="o">.</span><span class="n">target</span><span class="p">()</span><span class="o">==</span><span class="n">t</span><span class="p">:</span>
 <span class="c">#           print &quot;found target&quot;;</span>
            <span class="n">cap</span><span class="p">[</span><span class="n">e</span><span class="p">]</span><span class="o">=</span><span class="n">m</span><span class="o">-</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">source</span><span class="p">()</span><span class="o">.</span><span class="n">in_degree</span><span class="p">()</span><span class="o">-</span><span class="mi">1</span><span class="p">);</span>
        <span class="k">else</span> <span class="p">:</span>
<span class="c">#            print &quot;else mei&quot;;</span>
            <span class="n">cap</span><span class="p">[</span><span class="n">e</span><span class="p">]</span><span class="o">=</span><span class="mi">1</span><span class="p">;</span>
        <span class="s">&quot;end if&quot;</span>
    <span class="s">&quot;end for&quot;</span>
    
    
    
    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">G</span><span class="o">.</span><span class="n">edges</span><span class="p">():</span>
        <span class="k">print</span> <span class="n">cap</span><span class="p">[</span><span class="n">e</span><span class="p">],</span><span class="n">e</span><span class="o">.</span><span class="n">source</span><span class="p">(),</span><span class="n">e</span><span class="o">.</span><span class="n">target</span><span class="p">();</span>
    <span class="s">&quot;end for&quot;</span>    
    
    <span class="n">maxdsubgraph</span><span class="p">(</span><span class="n">G</span><span class="p">,</span><span class="n">s</span><span class="p">,</span><span class="n">t</span><span class="p">,</span><span class="n">m</span><span class="p">,</span><span class="n">n</span><span class="p">,</span><span class="n">cap</span><span class="p">);</span>
    
    
    <span class="n">cap2</span><span class="o">=</span><span class="n">g</span><span class="o">.</span><span class="n">new_vertex_property</span><span class="p">(</span><span class="s">&quot;bool&quot;</span><span class="p">);</span>
    
    
    <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">g</span><span class="o">.</span><span class="n">vertices</span><span class="p">():</span>
        <span class="n">cap2</span><span class="p">[</span><span class="n">v</span><span class="p">]</span><span class="o">=</span><span class="bp">False</span><span class="p">;</span>
    <span class="s">&quot;end&quot;</span>
    
    <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">G</span><span class="o">.</span><span class="n">vertices</span><span class="p">():</span>
        
        <span class="k">if</span> <span class="n">v</span><span class="o">==</span><span class="n">s</span><span class="p">:</span>
            <span class="s">&quot;blah&quot;</span><span class="p">;</span>
                       
        <span class="k">else</span> <span class="p">:</span>
            
            <span class="n">cap2</span><span class="p">[</span><span class="n">v</span><span class="p">]</span><span class="o">=</span><span class="bp">True</span><span class="p">;</span>
        <span class="s">&quot;end if&quot;</span>
        
    <span class="s">&quot;end for&quot;</span>
    
    <span class="c">#res = boykov_kolmogorov_max_flow(G, s, t, cap);</span>
    <span class="c">#part = min_st_cut(G, s, cap, res);</span>
    <span class="c">#G.set_vertex_filter(part,inverted=False);</span>
    
    <span class="n">g</span><span class="o">.</span><span class="n">set_vertex_filter</span><span class="p">(</span><span class="n">cap2</span><span class="p">,</span><span class="n">inverted</span><span class="o">=</span><span class="bp">False</span><span class="p">);</span>
    
    <span class="k">print</span> <span class="s">&quot;</span><span class="se">\n\n\n\n</span><span class="s">Densest Subgraph is ::&quot;</span><span class="p">;</span>
    
    <span class="n">graph_draw</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">vertex_text</span><span class="o">=</span><span class="n">g</span><span class="o">.</span><span class="n">vertex_index</span><span class="p">,</span> <span class="n">vertex_font_size</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span><span class="n">output_size</span><span class="o">=</span><span class="p">(</span><span class="mi">500</span><span class="p">,</span> <span class="mi">500</span><span class="p">),</span> <span class="n">output</span><span class="o">=</span><span class="s">&quot;two-nodes.png&quot;</span><span class="p">);</span>
    
    
    <span class="k">print</span> <span class="s">&quot;Density is equal to&quot;</span><span class="p">,(</span><span class="n">g</span><span class="o">.</span><span class="n">num_edges</span><span class="p">()</span><span class="o">*</span><span class="mf">1.0</span><span class="p">)</span><span class="o">/</span><span class="n">g</span><span class="o">.</span><span class="n">num_vertices</span><span class="p">();</span>
    

<span class="s">&quot;end def&quot;</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">
    Out[262]:</div>


<div class="output_text output_subarea output_pyout">
<pre>
&apos;end def&apos;
</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Densest-Subgraph-Function-used-on-the-graph-created">Densest Subgraph Function used on the graph created<a class="anchor-link" href="#Densest-Subgraph-Function-used-on-the-graph-created">&#182;</a></h2>
</div>
</div>
</div>

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[263]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre><span class="n">dsg</span><span class="p">(</span><span class="n">g</span><span class="p">,</span><span class="n">g</span><span class="o">.</span><span class="n">num_edges</span><span class="p">(),</span><span class="n">g</span><span class="o">.</span><span class="n">num_vertices</span><span class="p">());</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>
m  12 n 10 



Source 0 target 1
Source 0 target 11
Source 1 target 0
Source 1 target 2
Source 1 target 4
Source 1 target 3
Source 1 target 11
Source 2 target 1
Source 2 target 3
Source 2 target 4
Source 2 target 5
Source 2 target 11
Source 3 target 1
Source 3 target 2
Source 3 target 4
Source 3 target 8
Source 3 target 11
Source 4 target 1
Source 4 target 2
Source 4 target 3
Source 4 target 7
Source 4 target 11
Source 5 target 2
Source 5 target 6
Source 5 target 11
Source 6 target 5
Source 6 target 9
Source 6 target 11
Source 7 target 4
Source 7 target 11
Source 8 target 3
Source 8 target 11
Source 9 target 6
Source 9 target 11
Source 10 target 0
Source 10 target 1
Source 10 target 2
Source 10 target 3
Source 10 target 4
Source 10 target 5
Source 10 target 6
Source 10 target 7
Source 10 target 8
Source 10 target 9
1.0 0 1
11.0 0 11
1.0 1 0
1.0 1 2
1.0 1 4
1.0 1 3
8.0 1 11
1.0 2 1
1.0 2 3
1.0 2 4
1.0 2 5
8.0 2 11
1.0 3 1
1.0 3 2
1.0 3 4
1.0 3 8
8.0 3 11
1.0 4 1
1.0 4 2
1.0 4 3
1.0 4 7
8.0 4 11
1.0 5 2
1.0 5 6
10.0 5 11
1.0 6 5
1.0 6 9
10.0 6 11
1.0 7 4
11.0 7 11
1.0 8 3
11.0 8 11
1.0 9 6
11.0 9 11
12.0 10 0
12.0 10 1
12.0 10 2
12.0 10 3
12.0 10 4
12.0 10 5
12.0 10 6
12.0 10 7
12.0 10 8
12.0 10 9
Inside MaxdSubgraph
1.0 0 1
11.0 0 11
1.0 1 0
1.0 1 2
1.0 1 4
1.0 1 3
8.0 1 11
1.0 2 1
1.0 2 3
1.0 2 4
1.0 2 5
8.0 2 11
1.0 3 1
1.0 3 2
1.0 3 4
1.0 3 8
8.0 3 11
1.0 4 1
1.0 4 2
1.0 4 3
1.0 4 7
8.0 4 11
1.0 5 2
1.0 5 6
10.0 5 11
1.0 6 5
1.0 6 9
10.0 6 11
1.0 7 4
11.0 7 11
1.0 8 3
11.0 8 11
1.0 9 6
11.0 9 11
12.0 10 0
12.0 10 1
12.0 10 2
12.0 10 3
12.0 10 4
12.0 10 5
12.0 10 6
12.0 10 7
12.0 10 8
12.0 10 9
value of l 0.0 value of u 12 value of b 0.0111111111111
yeah done with while
u reduced
value of l 0.0 value of u 6.0 value of b 0.0111111111111
yeah done with while
u reduced
value of l 0.0 value of u 3.0 value of b 0.0111111111111
yeah done with while
u reduced
value of l 0.0 value of u 1.5 value of b 0.0111111111111
yeah done with while
l increased
value of l 0.75 value of u 1.5 value of b 0.0111111111111
yeah done with while
l increased
value of l 1.125 value of u 1.5 value of b 0.0111111111111
yeah done with while
l increased
value of l 1.3125 value of u 1.5 value of b 0.0111111111111
yeah done with while
l increased
value of l 1.40625 value of u 1.5 value of b 0.0111111111111
yeah done with while
l increased
value of l 1.453125 value of u 1.5 value of b 0.0111111111111
yeah done with while
l increased
value of l 1.4765625 value of u 1.5 value of b 0.0111111111111
yeah done with while
l increased
value of l 1.48828125 value of u 1.5 value of b 0.0111111111111
yeah done with while
l increased




Densest Subgraph is ::

</pre>
</div>
</div>

<div class="output_area"><div class="prompt"></div>


<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfQAAAH0CAYAAADL1t+KAAAABmJLR0QA/wD/AP+gvaeTAAAgAElE
QVR4nOzdeXhcxZUo8HPqLt3q1i7bWr1hsDGyZENrwWwhEEIAEyBgCIQlEIJtSJhsL0Mm8xJN3oRk
3mScNwyLxTrJECCESSBgliyEYTPabFnygjHgVbutXa1e7q3z/rDV6pa6JUtu3V50ft/H96lvVd8+
3Vg6XfeeqgJgjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHG
GGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhj
jDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wx
xhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMMcYY
Y4wxxhhjjDHGGGOMMcYYY4wxxhhjjDHGGGOMxRGMdQCMsfjy1FNP2X0+3yIAWCClXIiIi4koUwiR
RkRORLQDgB8A+onIjYg+AGhDxANEdEAIsf/rX//64Zi+CcZmIU7ojDHctGnTciI6GxErAaAUEbWT
PGcXEdUjYoPX633v3nvv7YpGoIyxyDihMzZLPfbYY0VSysuJ6HJELJrBl5IAUIOIr2qa9rfbb7/d
M4OvxdisxQmdsVmkqqpKFBQUnE9ENwPAKjiRvwFECKapggQBIAUQCQAAQGECgiQhJCqKcYIhDAPA
XwHgyXXr1h2c5ttgjIXBCZ2xWaCqqkrk5uZeLoS4FQBOidSPpBTo8znA53egadjQMHWQUiOiCf9W
oBAmKIqPFOEjVfWAbnODrk00EpdE9Iau60/dcccdn073fTHGRnFCZyzJbdq06QxEvA8AzgjbwTRV
GB7OEF5fGhiGfbLkfcKEMEnXhsBu7wObbQgQKUwvSUTPOxyOR2699dahqLwuY7MUJ3TGktRDDz2U
qijKPYh4LQCIcR08njQcHs5En98ZtSQeiRAG2Gz94HR0k6r6w/ToIqJfrF+//q8zGgdjSYwTOmNJ
6KGHHlququrPAaAwpIEIcXg4HdzDOWAYtonOgUNuv9Lb64WePp/o7fWBz0vo95vo8UkAALLbFNA1
IVPTVMjO1GVGhi4zM2ykquO/PIycE5GkTR8Ah/NohEvyf/B6vb+49957vdN424zNapzQGUsyjz76
6PVE9C0A0EMaPJ5UMTCYS6aph3ue8PlMPHBwUD10eEgcOOAWPX3hRtITQwRZWJBiLlzgMBbOT6W8
PEe46+wAAGDTByk9vQ3GF9TtVRTlvjvvvPPAlF+fsVmMEzpjSaK6ulojoh8h4mXBx8k0VTEwMA88
3oyxz0EAEgcPDao7d/cpez8eRMOImH+nQ2ZlaEbxigxz+dIMmZY2/ouEECalOjvB4egNiZnIDQB/
v379+i3RjIexZMYJnbEksHHjxpTU1NR/IaJzQho8nlTsHygAKZXgw0hE6t5P+tQPao+KI0d8Mx4g
IhglZ6T7y8vmyIyM8Zf6j43WW0FRzKCjhpTynzds2PDKjMfHWBLghM5YgquurnYAwIMAUBp8HAcG
56DbPWdswZvS3j6k/+nNdksS+Vgjif3cc3Nlil0NaVIUn8zIaBlzb52IaOP69euftThSxhIOJ3TG
Etjzzz+vd3d3/zsilgcOEiH29haC15cW3Fd4PIb23vudyvYdfTH/xbfZhPczF8w1VyzPDr7Gj4hE
GektZLcPBB0mIvrx+vXrX7U6TMYSScx/rxlj01NVVaXn5ub+PyFExcgxklIovb1F5PM7g/uqn+7r
t732pzbweqX1kUZmnLLY6b/0cwUyJSUwWkdEkmmp7WPuq0shxH1f//rX34xBmIwlhIjTSxhj8S0/
P/87wckciFCMSeYIAHpNfaf+4sst8ZbMAQDUT/cN2X/z231KV9fwyDEiQjEwmAfDw+lBXYWU8p8e
fPDBpTEIk7GEwCN0xhLQpk2bLkfEn4w8puPJHLy+1JFjKKXUX/9zq/rhnoHwZ4kfpKro++LlBcai
RYEkjogkM9JbIPTye7vT6bzp5ptv7o9BmIzFNR6hM5ZgHnroofmI+P3gY9g/kBuczAUR6a+8djgR
kjkAABoG6S++0qp+ui+QqIkIsa+/AHx+e1DXvMHBwftiECJjcY8TOmMJ5Pnnn1dUVb0fAALJG9zu
TBwezhp5iACk/ekvLerHnyTU2ugoJel/3NyqHm4ZDBwkEqKvrwhMMzDtDhE/X11dfXVMgmQsjnFC
ZyyB9Pb2fhkAlgcO+Px2MTCYF9xHe/vdDnXn7oQYmY+FUpLtxT+2KB0d7pFjZJqa6OsrHNP13scf
fzzb4vAYi2uc0BlLEI888sg8KeW6wAEixP7+guB55uqu3T1a/daemAQYLT6/tP3x1Rbh8QSWhCWf
3wmDg8EJPN00zXtjEB1jcYsTOmMJAhG/hYiOwOPBoZANVpTuHo/tr291xCa66MKBAUN/46+tCBCY
po5D7rlgGFpQtyseeeSRM2MQHmNxiRM6YwngySefPAURLwkc8Pt1dLvnjDxE05S2lze3gN8f1bXY
Y0n55JMhtXF7d+AAkcCBgdygLoiI662PjLH4xAmdsQTg8/nuhKBppmJoaG7Ipfa6+iN4tNv6pVxn
mPb2e13Y1zf6vry+NPT5Rq9SILqqq6vPiklwjMUZTuiMxbnHHnusCAAuDhzwGTbyeAPztUV/v0+r
begO99xEh4ZB+jvvh95GGBycO6bbbdZFxFj84oTOWJyTUl6HiKO7pbkH5wS361tqOqO97Wk8UT/a
Oyja2gJV7+DzOyBolA4A51RXVy+wPjLG4gsndMbiWFVVlUpElwcOGIYmgjZdwe4er0jQKWpTodfU
dQU/xqGh4Ip3JKI1FofEWNzhhM5YHCsoKKhAxEDywmFPRvC9c31b49HZsH6z8ul+t9J1JLDeO/r8
qWCawduvfgF4KWs2y3FCZyyOmaZ5RfBj9HgyAj97vaayc/esWdNcbWoOzK8nIsSgzVsQseDRRx9d
GZvIGIsPnNAZi1NVVVUCEVcHDvh8KWSa+shD5eNP+5P53vlY6od7BtA0R3eM83gzgtuJaPW4JzE2
i3BCZyxOFRQUnIqIo6NQz+jmKwAA6s5dfdZHFUNen1T37R+tFzAM+5jL7mXWB8VY/OCEzlicIqKQ
BEV+b2Cfc+H1GuJwy/D4ZyU3/GTfYMhj7+hnAgDFGzduTLE4JMbiBid0xuJXYMEUklIIwwxsIypa
W92zsQJM3X9gKOR9+/zB09dUp9NZanFIjMUNTuiMxSkiOmXkZ2EY9uDqdnGoxR3+WTPLPneOWvHL
fy26fMs7y+dfuSZ98mdEFw4NmaKn1xM4YBghI/Lgz4yx2UadvAtjzGrV1dUaEY1uGWoYenC7aO/w
jHvSDFv4pasylm1Yn4situMA7DrigaxMOwAAmqYuiRARCQAAERfGNDjGYohH6IzFISFEUfDqcGSY
IQld6TritTKeZRvWzTn19tvnNv2f+1u6amoHJ3/GzBE9PYG13YkIMXQHtkXWR8RYfOCEzlgcMgyj
IPgxmqMjdOHxGOD1yvHPmjnd2xrdb9/4lU/b335nyMrXDQe7e0I3oZEyOKEXAGOzFF9yZywOCSGC
q7eBpFRHbqDjkNuwOp6uD2pics8+HOzv94c8Nk11ZDI+EaWGeQpjswKP0BmLT8HV24A0+rtKPmtH
5/FG+Hwh75+Igv+OOYGxWYoTOmPxKSShQ1DSQr9hWh5NHCHPmC80wZ8NovLAAw/YLA+KsTjACZ2x
OEREtjEHAlPWUJqzZrnXcIQZ+v6Rxm3KwgmdzUqc0BmLTyHT0hAxMColVZvVv7dSV0PePyGEJHib
zTbrVtBjDIATOmNxSQgRUk1OQQkdNHV2/97q9pD3j0IE34LwrVu3zg+MzUKz+w8DY3FKShk6yhRB
CV23zerfW7LpY0boQVcviOKmGp8xq83qPwyMxStEDNnnHIUITFWjVKc2/hmzB2VlhLx/VJTgaXyz
Zn94xsbihM5YHDIM40DwYynUwGIqUtMUSkubtWtIUHZOSNGbVJTAZ4OIh6yPiLH4wAmdsTjU1dXV
CQCjy7tqSshSr3JOtj72OTMJFQW0jHRFy0hXUNUQAECx24SWka5oqamW/h2RmRmB945CmMEjdCI6
EP5ZjCU/TuiMxaGqqioJAAcDBxQ1ZLlTWVBg6b7faYsX65e8vnnpJa9vXpp7/rnpAABnfOdb+Ze8
vnnphc8/a+kOZzJ33uh7DxqdAwAIITihs1lr1l62YywB7AWA0wAAQNc8KIRJUioAALKo0AEAR60K
pP/jj32vrj5/t1WvF4nMztKkc7SGQGpaSBEcIu61PirG4gOP0BmLU0TUEPJYUwPJy8yd5yAhxi6o
kvTkooWha9zrowmdiNwtLS27rI+KsfjACZ2xOEVE9SEHgkajpKrCXLJ41q1bbiw5JW3kZ0Qk0PXg
EXpjVVWV5RvXMBYvOKEzFqc2bNjQQkRtI4/JZgvZh9wsPiPD+qhih1JTVTm/MPAlhjTVjUIEz0Gv
i01kjMUHTuiMxTFEfCfwQNN8EHSJ2Vy0MJXsdiUmgcWAseKMdAIM3GaglJTe4HYies/6qBiLH5zQ
GYtTVVVV4t333+/1ev2je3zb7X0jP5IQwnCdmRmT4KyGCEZJcVbgoRAm2O0DQT123X333Z/GIDLG
4gZXuTMWZ5YtW5amp2fe+IdXXr2WEHIWLVzkLCosGAQAIJttAHEwd2TLUP+q0hytvqEHvL6k3iPd
KF2RIdPSAvPPyWbrB8TApixSyldiExlj8YMTOmNxovScc+aB37wVJH0RgBwjG6buP3jQmDtvbqpN
0wZBUUxIcXSDe2gOAADZbIp/5coMrbauJ5axzyhE8LnOzBl9iCSdjuApez4i+nMMImMsrvAld8Zi
rLS0YnGJq/wn4DdeAqAvgwBHcPuej/f2uoeGAgVw5EzphqANSYzys+aAw5G099L9Fa5syswMLPdK
Nr0fVDV4R7VX7r777uT9QsPYCeKEzliMrKisLC0tK/8l2uC3KPByAAi76YrH6zM/3LvX5/f7j62Q
pigm2O2BgjBps6m+iy6cZ03U1pJZGZr/7Mq5I48RkaQjNTA6JyK/EOKJ2ETHWHzhS+6MWQtLysvP
BxK3oaSVgAg0+XNg9569PWcsXTYnI0MbBgCQaaldis+XRqapAQAYS0/NUE9Z1Cc+3Z9U24f6L7xg
HilKYOBBKY6jqKuBde0R8c9f//rXO2ITHWPxhUfojFmgqqpKrCoru2RlefmvEXAjIq2cyvOHPcPG
7r17/VJKFQAAhZAy1dk50k4A6L30kkJKTU2aL+mG66xMY/Hi9MABRfFTmvPIyEMi8vh8vk0xCY6x
OJS0990YiwfLli1LKzjl1K/u+WjvTwnxSgCcO/mzxiDwAeLvAOGHZyxbdjYAHFstTdO86PengGnq
AACkacLMy7Nru3b3TXS6RGDm59t9l11aBCJo3nlGeitoWvBmLNX33HPPO2GeztislDTf5hmLJyMV
60R0JQI5aTqrrhP0E+JzUhMv7NyypbsJAK65/PJfIOLGQJf09Fbs7lkMxy+9y8J8p/eyz+frr77R
lqgLvcusDM131ZoiUoLWqnc4j4DdHrxS3n5EfNr66BiLX4n6O89YXCotrVhMGt2OAi+BCEVukyLq
BMD/0sh8qaGhYdw98U2bNv0cET8XOODz20VPzyKi0a8N2tbGI/pbb3dN6/VjyelU3F++bhFljO55
Dro2RNnZB4N6SSK6e/369fXjT8DY7MUjdMaiYEVlZakw5e2IcC4ATqs2hSR8qgD8SgH5p4aGBn+k
fpqm/dQwjOUAUAgAALrmobTUdugfyB/p4z9r1RwwTNLffe9IpPPEG5maqvrWfml+SDJXFD9lZLSO
6fo4J3PGxuMROmPTN1qxPsUit2BEuB1Q/qq5ru4dgBMqeodNmzadgYiPA8Bo8hsczMHBoZDpa9qu
3T36G39pBzqh08aMzM7SvNdevSB4NTgQwoDsrP0UNOeciOra29vvqaqqSuqV8RibDk7ojE1R8dq1
Ou4/tAalvAEFLJnOOYhIAsHrRMqzO7Z+sHs653jkkUeuEUL8MPgY9vXnwvBwdvAx5XDLoH3z660w
NGRO53VmmnnaklTfJRfnS7s9cMUQhTBlZsYh0PXhkWNE1GYYxle/8Y1vHA1/JsZmN07ojJ2gkTXW
BdG1hJAz+TPGIwIvIv4BBDzXVFNz+GRjqq6uvgsA7go5GGakLtzDfturr7eIg4eGIU6QEOi/8Py5
xqqVOcHXD1BR/GZG5qHg+eZE1Kuq6tfuvPPOAzEIlbGEwAmdsUmEVKwjOCd/RhgjFevqsYr1aMZX
XV19HwBcF3wMBwezYXAoN/iYICJle1O3/t6WI7HezMUsLLD7P3dRvpmTbQ9pUBQ/ZWYcDJ6eRkRu
IcSGu+66a6flgTKWQLgojrEIVq1atchUtDvAb1wCABpOb+pZBwA8rZH5UkP9+Ir1aGhra/u/+fn5
dgBYE3jZ1NRu1HUP9PYVwvHFaCQiylUrc8ylS9O197d0qs07+62+ty7T0lT/OWfPMYuXZ9KYAQXa
bf1menobChH4skFEQwDwXU7mjE2OR+iMjTFasY7n0jRXUxytWDcnrFiPIty0adM3EPG2kDhMUxV9
fQXg84+7siD6+rxaXf0RtXnXjCd2mZmh+SvKc8zlp2eGzC+HY+uzU1pqOzkcvcHHiajbNM2/u+ee
e6ZVY8DYbMMJnbFjolKxDhJqSdBzU6lYj6ZNmzbdAADfQcTAKpBEhDg0lCXcw3NIynGrQwr3sF/5
6KN+dcfuPtHZ6R3bPl0kBMrTTnUaxadnmAsXphGGucaha25KTesAXfOEPJfoICJ+a926dQfHPYcx
FhYndDarFRcX6+hIWyPIvB4QT53OOaJRsR5N1dXVZwHAPwNA6A5spqngwOA89HozghehCab09Hrw
8GG3evDwkGhp9eDgoHHCL4wIMjfXZi4scsqiIoeZl+sgmy3s8tKoKH5yOrrI4QhZptbr9ab29fU3
LVy44PZbb7116IRfmzHGCZ3NTvFYsR5NDz/8cJaiKD8BgNXjGg1DwyF3Nng8mUA04S0F4fOZ2Nfv
w+5uL/h8UvgMCYZfklAQdE2ArguZYlcpK1OH9HRdhhuFB1MUH6U6uyAlpT/4sGma2sDQ0Nyt2xqH
d320tx0VvCHePlPG4h0ndDarnHnm+XNN1XdbVCrW3eKFnTujW7EeZbhp06ZrAOAbiJg+rtUwNHR7
MsHryRhZC35GgkAk0lQ32O19lJLSD4iBWxFEhMPDwzmHW1ttdVu3dfX29/uOHYctzfW135ypmBhL
RpzQ2awwUrF+cmusB1Wsh1ljPV7df//9OR1dXW8umD8/x26zdauq6hvbB30+Bw170tHvd4Bh2E76
RRElaOow6foQpKT0gaKMu3Tv9/tTevv6sxq2bRv85MCB/vHngO831da+edKxMDZLcEJnSS2aFeuZ
aY433nrrrRO/pxwnVlZWfpYk/WtWRoatePnp2YsXLBApKSndmqaFXWSGTFNFn8+BhqmTadjQMHWQ
UkMiMe7eO6JEIUxQhI8U1QeK8JGue0DThoNH4mF07vn444/ffve983yGEXZOPBJ1D/WK6z7+uGZ8
smeMjcMJnSWj6FSsE72DQM9ur6+vgxhUrEdLaVnF44CwauRxmsOpnb5safaSxYswLTV1QNf1Ey8+
I0KQ8tgXI0WZzlKyTYj4IhG9tm7dOnNlWeXjhFQauTv+d1Ndzc+m8TqMzTqc0FnSuPDCC9XeAfel
EumWk61YB1CfaW7Y8mG0Y7TayrKyMwnFY+HaFCFw+bJlWz9z7jk9AHAeBG/0EkVE1IqImwHgtbHT
0IrPWn2qIsynAcMvcoUAUiB8fVtt7faZiI2xZMIJnSW84uLiVOFIvSlZK9ZPRmlZ+S8B8fxwbUQk
haZes33LlpZf//rXzsHBwbMQsQwRXQBwWvBc9qkgoj4i+gARGxCxfrK55KWu8r8DgbdEPJ+ET3PS
HDcl4u0OxqzECZ0lrKhUrEvoJ5EQFetTtsLlWiKE8hxE+j0neLOpvvb74ZqqqqrUoqKiQinlIiIq
BIAsKaVTCOEgIjsiDgGASUQDQggTAA5LKQ/YbLYDt99+e2+4c0Zy4YUX2rsHh38LSIWR+iDgQ9vr
ap6aynkZm204obOEE1Sx/jmY7mXiBK1Yn4rSsoofA8KVkdoVgbduq6nZZWVMkawoLz9HAD4QqZ0I
vDw3nbGJcUJnCaPEtboE0bjjJCvWP1EAfp2oFesnqri8PE8hfDHSvWmQuLWpoeausG0xsrK84ucE
8LlI7UT0QXN93TesjImxRMK7rbF4F1Sxbq4EwOmVmx+vWG9qSOyK9ROlSLgBROTfbwT4tZXxnAgv
wr9qEisRKS1cOyKevfKsiku3b619w+rYGEsEPEJncYkr1qdv2bJlabbUjM0gwBGunSR80txQ+2WI
wy82K8rLrxeAYe/rA/DcdMYmwiN0FleKi4tTFbvz2u4h93UgIH863zlHKtaFpjy7fcuWlhkIM66l
ONOvlRGSOQCAcmx0HnfJHABgR13dCyvLKr8QaW46IWY7MukbAHC/xaExFvc4obO4EFyxDidbsT6c
fBXrJ6p47Vqd9u2/KVI7ErRnpjni+ZK1NKS4f6K56YBwzary8lcb6+oaLY6NsbjGl9xZTEWjYh0J
2gngN8lcsX6iSlwVV6OAf4zULkz6ZePWut9YGdN0lLrK7wWBt0ZqJwmf6mB+paGhwW9lXIzFMx6h
s5gYqVgnxHORK9ajRSDiLRGvpkvoS7Gpv7c2pOnJTnM+2j04fHGkueko4BSD1FsA4EmLQ2MsbvEI
nVkpamusC4Rf8SXXUCvKzr5QoPxF5B70ZFNd3cPWRXRyeG46Y1PDI3Q244Iq1m8GwNNgwk24whup
WEek3zTV1++ZgTATngB5e6Q2IvDKYfU5K+M5WTvq6t4vcVX+GQVdEq4dEWxkyvsAgOemMwac0NkM
4op166wqL18lAYojtSPA5kQsFPQr9AtN4tkTzU0vPav8C01b6163OjbG4g0ndBZ1XLFuPSK8NdL3
JQSQKplPWxtRdHxYW3u0pKLiYSD4+4idBH5v1apVHzQ2Nk5pDXnGkg3fQ2dRc+aZZy40hPo1rli3
Vkl5+SkI+FuIuAkLvtlUXxNxsZYEICbdN53gD031tT+1MCbG4g6P0NlJG6lYlydRsY4EuyTSr7NT
nW9xxfqU3QwTfDlXFPhP60KZEScyN/3qM8+seGPbttp6i2NjLG7wCJ1NF1esx4EVlZW5wqSXEmkT
lumabG46EB4whwdv3Llzp8/CsBiLGzxCZ1MSjYp1IDKJ4A2uWD95wpA3gMDIv8dE/2VhODNqsrnp
gLRQTUm9GXhuOpuleITOTsjq1atThvzm1YBwEwDkT+skhB5AeBFVwRXrUbBs2bI0PS3jFYxQeBjP
m7BM12Rz0wHApxj+G7dt23bAsqAYixPTut+ZqKqrq7VYx5BoXC7XnNLyyu8N+s3XAeG7MJ1kLqGf
AB8lr/vKprqaX3Ayjw5bWsY1kZI5AAAKehqSKJkDHJubThL/PEEX3VDUfwAerLBZKKn+0T/yyCPz
iGiZEGIhIi4gooWImEdETkR0wPHKayJyI+IgAPiJqAMADh7/b7+qqjvuvPPOWT9NiivW45vL5dL8
QvwRAOeGa0eC9qxUx9XJWGB4ekVFji7hd4CQHqmPIPmjxvr6V62Mi7FYS+iEvnHjxhSn03k+AJQR
URkiLojCaYmI9hFRPSI2uN3u97/zne8MR+G8CaG07JwVAP6vIeK5dJIV6zlOrlifKaVlZ38RUP4o
UjsS/vv2+pqkuX8+VmlZ5XWAdF/EDgS9wvBdx3PT2WyScAm9qqpK5ObmlgkhLieii46PvGcMEbkB
4G+qqm4+fPhwfVVVlZzJ14sRrlhPLKK0rPJ3gLQwXCMRDuhkXJHkV0UmnZtOQC8219X9s5VBMRZL
CZPQq6urNSK6EhFvA4DwVa7BiBD8pg7S0FFKQUQCiI6NOBElIkoSQoJQfaApPsDJy7WJ6AAiPpmV
lfX69ddfb570m4qxtWvXKns/PfAFiXQzIJ42rZNwxbrlSsrPuQDB2BipnQj+s7m+9kErY4qFFS7X
EoHKbyJO2QMgxYANPDedzRZxn9CrqqpEXl7elwDgdkTMjdjR57ejz+sAv98BhmlHKVUiOqH3h4hE
QhigKh7SNDfo9iHQVW+k/kR0GACeam9vfzkRR+zRrFhXdPWZbe+91xrdCNlESssqHgeEVWEbCXym
pqzZuWV2LJe70lXxTRJwW8QOPDedzSJxndAff/zxCsMw7ot4b9znS4FhTwZ6vekgpRLVFxfCIJtt
AFLsfaDrYe+hE9FBRPyXdevW1UT1tWeIy+Wa4xfqV4loDSKkTuskEvpI4G/B4/5dc3NzT5RDZJNY
UVlZKiRFnGc92y4zX3bZZbaWru7nI85NBwAgeKSpvvYJC8NiLCbiMqFXV1dnAMA9AHA1jC3MIkJw
uzPRPZwNpjmt6uspU1UvOFK6KSWlL8yleQkALwPAA+vWreuzJJ4pikbFOgC0AcEzTk15ccuWLbOm
SDDerCyv/AUBXRiuDQGkMPxrZ9sc7JIzK1ajCv8xQRef8Ptuamxs3G9VTIzFQtwl9EceeeRMIcRP
AWBeSMPxRC7cwzlkmhHnk6MpCbs6h0Vfv0/09vmwu8eH/f1+9BsEhl8CAEhNV9BuE6BrQubk6DI7
y0Y5OTY5N8dOgJE/E0XxkyPlKDgcvWESe7tpmv9w9913N03/3UdXNCrWgWAXIT3eXFf3Lhz78sJi
ZLJNWBDwre11Nd+zOKy4UOqqvB8EfT5ih2NL4K6DJJuXz1iweErouGnTplCn7eQAACAASURBVK8C
wHpEDL18PjycLgaH5kVK5MI97Fc+/qRf7Ns3pBw87Ea/f3q/tDZdGPOLHHLRIod52pIMmZISttgG
FcUn01I7wG4fHNNkSCkf2rBhQywX9OCK9SRVUl7+jwh4daR2BLpte13dTitjihcnNjcdf9RYX8Nz
01nSiouE/vzzzyu9vb0/JKIvhjSYpgIDA3no8Y77JUVTkvLxx33K7j396r79Q0BRzp+IYCw5xWkU
L8+USxanhR252219lJbWAYoytuL95aysrH+2shI+mhXrQsGnt9fWfhTlENlJOLbHvPcliHTLhKCx
qb72Tmujii+Tzk2X0CdM37U8N50lq5gn9I0bN6Y4HI6fIeJ5IQ1erxP7+gtAypBRMpqmVHbt7tU+
qDsqBgYsWbREZqZr/oqKbHP5skxSlNBL10IYlJHeCjbb0Jinve31en9w7733RqyWj4ZAxTrAjYBQ
MK2TcMV63JusmptA/U5z3ftvWxlTHBIlZZWPTXRlioBeaq6r+z9WBsWYVWKa0I+v9PYQAIQuDjE4
mCOG3HPHTjtT9+3r1//6Px3Y3x+T1cdkVobmu/iiXHPB/LTg44hI5HR0Umrq2KlC2wDg79atWxf1
BT5cLtccA5QbCeEqQMic1km4Yj0hFBcXp4oU5+YJNmH5tLmh9gbg+8MnNDdd+Onuxsa6OksDY8wC
0Z3qNQVVVVVqTk7OLwCgLHCQCLGvrwDdwzkQ9GUDh9x+2+t/atHf/+Aoer0xK8xCj1equz7sV7p7
PLKo0EGaNvL5Ifj8qWgYOthsg0FX5/MB4PSysrI/v/XWW1GJ2+VyLZhTUPRdKcQPAcEFCPapnoMk
HCQUD6Vq4icNNR/UdHZ2eqIRG5sZ+QsXfxkRzo/UjiD+o6P1MC/qAwCdbW098woK7Rhpnj4ASsTS
ueed84euXbsSfnEoxoLFZD/044vF/JiIzhk5RlIK0ddXAF5fyOhXOXR40Lb59VZ0u+Pml0/Z89Fg
yuGWfZ4rvlBgFhWOzuf2eDOQegVlZrYEVcGvzsvL+zEA/AhOYgQ1UrFuIJ6LJ1ux3sAV64nC5XJp
fqAvR7yYRtCRnWrnQq8gRXNzHmvp6v4cIBWFa0cBC8T+Q7cBwGMWh8bYjIrJJfdNmzbdjYh3BA4Q
Ifb0LACfP7AuOwKA+kFdp/b+lqMxv9EfAQGA8ZkL5vpcq+YEH0ddG5JZWYfGTG17bN26ddVTfIlo
VKwTEL3LFeuJabJNWIDggab62l9bGFJC4LnpbDayPFdu2rTpAkT8t5HXJiIUvb2FwSNzNCXpf/pL
i7r7wwGr45sOY+WKDN/Fn80PqYS36QOUlXU4qBsh4vfuuuuu/5nsfKMV6/AVQFg6raC4Yj0ZiNKy
yucBaVG4RiIcQN/wmqamprEFmQwASl3l94NAnpvOZg1LE/rjjz+ebZrmswCQEzjYPzAP3e7AYyQi
26tvHFb2fDR2jndcM0qK032XXFQQnNTJ4TgK6WmdgcdE3T6f7yv33ntvV7hzcMU6C1ZSXn4BAkbc
hAUk/bqpoe4BC0NKKMWrV2crfvOFCeemS/hxY0PtZivjYmymTO9e7DQZhvEjCErm6HZnhCRzANL/
8mZroiVzAAC1eWe//te32oK/IaHbnYMez+iVB8RsXdfHzZN1uVxzVroqvjnkN18GhO9OK5lL6CPA
R4XhXdNUV/MLTuaJDwFvidhI4PMp+BsLw0k4xzaowYcm6iMBvlNSUpJlVUyMzSTLqtw3bdp0MSJ+
LXDAb+jY1zcfgq4S6O+936lt3Z6wiz6Ijk4vIZAsKhqdXuT1pYJNHxhZfAYRF61Zs+bDV1555cBM
VKy3t7dzxXoSWFFZWYoE6yO1E9Iru+rqXrcypkTU0dqyZ15BUQUi5IXtgGAHVc3sbG2d9FYYY/HO
koT+xBNPpEkpH0DElMDB3p75aMrAqlfqno969b+9HfZSdCJRDrUMw9w5uszOHknOiKZhh5SUwMYt
fsM4+0h//2k+SX+PiKfDdP4/EO4nwP+QnqGf72zctuPw4cMxmZvPZkZeXtH3AGFxuDYEkIph/GN7
e3tcbgYUZ2heft5OBHENYPgrkgi4NH9eQWN7eytf1WIJzZJL7n6//6uImD3yGN3uTPQbgeQu+vu9
tr+82WFFLFbQ/vTXDjE05A8c8Pkd4HYHFn8RiHNXnH76LQAQcZOZCAiI3hFAdzbV11zXXF/zEu/z
nHxKSysWgwi/oxoAABC8M9t2VDsZOxoaPiGApyfogqaCPyheu9aa3RsZmyEzntCPb4W6NnDANBUc
HArspIYApL/6Rit4fUkzLxo9HlN/9Y0WDKqexcGhuWCaCgCAqqq+Zaedpth0/cRG5kQmSXrVh/CV
pvq6b/P0sySnw00wQcGqEMDT1KaoaG7OY0B4OFL7sbnpB79qYUiMRd2MJ3RE/AoiBuaXw5A7h6QM
JDKleUeP0tqWdPd9lUOHh5Udu0brAaRUcWg4cJUi1ensP+P0ZdlhnzyC0AOAzyk2/ZrmhroffcjT
z5Key+WaAwhXRGonwu3bamu3WxlTMnjttde8IOHnE/VBoK+WllaEvc3BWCKY0YReXV3tIKLrAgdM
U8Hh4UBFqfB4DNvb7yX8ffNI9Hff70Kvd3SFu2F39sgoXdO04aVLlmi6qo7/f0DQyxXrs5MP8QaI
tKMaAAAKHp1PU9PWmg+A4I0Juuig4Q8gDjatYmw6ZjShE9EXAEbngOLQcDYQBV5Tbdh6FGK4NvtM
Q7fb1LY2HgkcIBLoHv1Ck5ae3r940aLA50MSDgoJPzaHhy5vrqt5lLd5nF2Ki4tTAcT1kdpJwqfN
dVtm+45qJ8XUlH8Dgv6IHQSdtfKsiohXSBiLZzN9yf3KwE9ECJ6g0fmwx1AbGpN+hy+tYWuv8HhG
K9CHh7Ph+C5yNk0bXLJ4sQIEOwnoO80Ntdc1NtRu5kK32Um1Oa6OtKMaAAAg/gZ4VbOTsnPLlm5E
8eBEfQjh2zw3nSWiGUvoDz300HxEXBE44PGkQdC9c7VpRzcaRvL/cfL5pdK8a/SLi5QKBC02s2jB
/N7bbrzhH5vr6t4G3jBl1nK5XBoJuClyD+qSw4OvWRdR8tpe98GLRBi5DkFABtpS7rUwJMaiYsYS
uhDiCxC8BarHkxH4GYDUpuZZM4dW297UG1Lx7vGM3oZANNPS0i6JTWQsXhikXAqI8yJ2kPgcX7mJ
GgkofwoEkdduQFizsqyswsKYGDtpM5bQETGwNSqYpoI+f+BSojjcMoQDA7NmIRTs7zdES5s78Njn
Tx0pjgMAkFKeE/6ZbJYQJOC2SI1EMAh+zwtWBpTsmuvqPiWQ/zVBF5Qk7uO56SyRzEhCr66udiDi
8sABn89Jx+8bAwCoe/ZELkpJUupHHwXeMxEh+HzB90qLn3rqqSkv+8qSw0pX5TmRVoUDAECi3/OO
atFXNHfu4zw3nSWTGUnoUsozAUAdeYze0eSFAKB8vC/hNl85WeLjT0PeMwbv/Y6oDQ8Pr7I+KhYP
CODWCZr9YNOesyyYWeQE56bfznPTWaKYkYSuKMrK4MfoH01e0N3jxaEhc9yTkpwYGDCwr8878hhD
R+igKMqZ1kfFYm1FZWUpCDorUjsBvdb0/vudkdrZyTk+N32iTW40npvOEsVMjdAXBR6YpkKmGbgP
pbS2xfTSYeEXPp92+ZZ3ln/hzT8vtfq1lcOtgfvoZJo6SBn8+S+yOh4We8KkmyO1IYBU/H5eSGaG
mZqycbK56aXl5WssDImxaZmporiFgZ+CkjkAgOjq8o7rbREtNVUsv/eb4bdRtIBy5GjoEreGYRv5
kYgWjnsCS2oul2sBIlwYsQPBu42NjfstC2iW2rllS7ecZG46SPx2cfHqiZdqZizGop7Qq6qqBADM
DxwISloAAKK7J2ZTb4q/+615vu4e/+Q9Z4bo6Q5572gYgS87iDj/+GfHZgk/KjfThL+DE1Zhsyja
UffBH4Ag8qZHAtKVFJPnprO4FvUEkp2dnYOIo4nKkCFbhIqj3TFJ6HPLy1LyP3dx5vaf/Ut7LF4f
AAC7joa8dzJk8NULW1FRUSawWeH4JiwRL+MiYdP2+vptVsY0yxEh3Q8Akb/w89x0FueintAdDocj
+DHR6OpwCEQ4OGj5/HOh61h83//KP/D7Pxzt27MnZpf8YWDACF5gBoI+GwAAr9cbedlPllT8QlwP
E23CogCPzi3WXFf3KQBN+Lnz3HQWz6Ke0A3DCElKSEGFXz5/TJY2XbburhwUAvc8XH1k8t4zBwGA
/P7RFeMopCgOQraZZUnL5XI5gPC6iB0I9m2vqXnLuojYiMI5c57gueksUUU9oSuKkhJyIGh3NTRM
yxN6+mmn2RZdf+2cnb/Y2GZ6vTFfO174jdEpe0GfDQCAoig8Qp8FfKBcDTi6C+FYUsAzwJuwxATP
TWeJLOoJ3e/3a2MOBeZvkrR4+jkilP7w7/M63n6nr/O9Le7Jn2ABivydRlEUNWIjSwoul0tDjDxV
DQCO0NDQZssCYuPw3HSWqKKe0DVNC0mchDiawVTV0iruxTfekOUoKNB3/OvGuFmYg4I/g+DPBgD8
fn98fOlgM8ZE9ZKJNmFBwN/yJiyxd0Jz08vOvjJiO2MxEPUEi4ghSQlhNGmhzWZZQk/Jy1OX3fm1
ubsf3tTp6+2Nn5XpdD0ooYuQhE5EnNCTG5pEE27CQt7h560MiIW3c8uWbingPybsRPJbPDedxZOo
X+Idm9CDR6ESEUlV0Yp90HMvOC9VpNiV4nu/mVt87zdzx7aLFLsyslpc9/ZGd+23/1fEQpio0TVB
iKO3IMaM0DmhJ7fisrPPQZRLIrUj4Iu8CUv82FFb+2JJWcWliFAWtoOAdGE3/g4AfmxtZIyFF/WE
bhhGb8gBRYTM65RZWbpiwWpxLa++1n/kg5rxfxyFwAuefXqJ9Hrlu1+9Yx8AgDE8bEkBkszOCa0v
CP1syOFwhH52LKkIMG+d4LarH3TlGSvjYZMi1fT/zFS1ZyHCFEMUeMXKsrLN2+vray2OjbFxon4J
fN26dW4iCkwPI1UNXUxlTo4lczj9g0Ny8OAh/7j/DrccS6KSaOSYp+uIJXPjZU52yKp5EPrZdNx+
++2hS8OypFHiWl2CiK6IHQje4E1Y4s+2bdsOANDTE/XhueksXszUPe2DIz+gqoaMxik7Oyb/8IWm
oZaRruhpaQIAgBBQy0hXtIx0BVTVkmpVmZUV+t4VJZDQpZQHxz2BJQ2B5oSbsIAPfmVlPOzEmW73
40B4IFI7CliABw7cYWVMjIUzIwkdEfeP/Eyq6g++j24W5MVk8ZT5V16efsnrm5d+7tU/LgUAUOx2
ccnrm5de8vrmpXnnnWvJ/G8qzB+do48oQVX9ow8j/8Fgic3lci0AhM9Gaieg95uaavdZGRM7cTt3
7vSpEu6HCdYGEAS3lZSXn2JhWIyNMyPznhFxD1HQv31dc4PXlwoAIPPzHCQEopSWLpxx4Pcv9R34
/Ut9Vr5mMBICzdx5o19mdG1sAdxeayNiVvEL9SsAFPnLs5S8RWqc27q1pmGlq/J1EnRZhC4aAv4A
AO4CXhSIxciMjNCJqC7kcdDcdFJVIQsL7DPxuvGMigrtIXPQNS2kYM80zbpxT2IJ7/SKihwAijhf
GQmbmhoatloZE5seNL3/BgQTFa6eWVJW+UXLAmJsjBlJ6OvWrTsIAKMFProtJHkZpy+NuOxlsvKf
vizkPZNuCx6ht99zzz2HLA6JWUAnmnATFhITF1yx+NHY2NgrBTw0UR8k+juem85iZcYWegkZpeua
B4MLwE5dkg44e1ZNJCFQnnrKaEJXFB/oWqCiHRF5yksSOr4Jy9qIHQj2NdXWvmVdROxk7aitfZEI
6iN2ODY3/VsWhsRYwIwldCHEm8GPpc0eWEZRpqSoxpLFqTP12vFGnrrEKe320XoFuz3kXj4RvTnu
SSzhTboJC4pnASAmOxCyaSPV9P8MACIuz4sCL+d901kszFhCb21tfY+IRu83pdhCkpjhcs2ay1J+
15kh75XstsCXm77+fsej//n0HJfLNXZTG5bALrzwQnXSTVjcA69YFhCLmuNz0yfZr1784LLLLrNN
3Iex6JqxhF5VVWUAwKuBA5rmC67sNgvznXLB/JRwz00m8pRFDjM/b3RanK4Ngab5AAAMw9D37P3Y
6Te8/+hH5bWS8sq7TnG5MmIWLIua3sHBz0+4CQvh87wJS+Iy3e4nJpqbTgjzW44c4bnpzFIzulmK
lDJ0G8jU1K7gh/6zK+bM5OvHA195ech7pKDPwOvzZe07cGAAAAAQMhHorlShvFbiKv+Jy+VaYHGo
LHpQAt4asVWCe6gXXrAwHhZlJzI3HQBv5bnpzEozmtDvvvvuPYj4/shj0nV38CjdKCpMNYrPSNqK
d6N4eZpZmB8YnaOuDYGuDwMAEJFy6HCLcqS7e+xyrzoKvNwQygulZeW/XFleXmxp0OykrSgvXw2I
p0ZqJ4Q/fPxxTeStOVlC2Lq1poEkvjZBFw0J/wF433RmkRnfzlSOXTRjzCjdd97qeVLXLN0n3RK6
JnznnROyy5tMTQ2scT88PJy188MPI85pJQABiOcT4K9KyiqfKCkvvwD4D0NCEIS3TNDsR139jWXB
sBmlmN6NE85NR1hV4qq4ysKQ2Cw244l0/fr19QDQNPKYdN0N9tECOXI6NeP885Lu0rv3sxfOI6dz
tNDNbu8FXXcDAEgpRWtbu9be2XlC26Ui0koE3FhaVvGbVa6KK9auXavMUNjsJJWWnbMCEMojtZOk
P/EmLMmjsbGxlwgenKgPAtzLc9OZFawaGf8SgqbnyLS0ThTCHHlsrCzJMZeeljTT2Mzi5WlG8fKs
kccohCnTRq9MGIZh29bcfCT8syeAsFQK+Kc9+w7+tqSs8qri4mLe4SnOEJlfmbAZeJnXZNPcUPvS
ZHPTVbv8toUhsVnKkoS+bt26ZgB4eeQxKoohnY5AgiMA8F5yUYHMykj4qVsyO0vzfvYz+cHHKNXZ
iYoS2KJV1/XfHGlr/QwBPgoSpr6+PNIiRPrfSorz1ZLyyrtWrVqVGYXQ2UlaUV4+H1BeHLkHvb+j
oeET6yJiFpl0bjoJuqzUdXalhTGxWciye9emaT4IAKOFQE5nT8ild5tN8Xzp6gXgdCbs5WRyOhXv
l65aQLo++h7s9l5yOILvsfU4nc4HGxsbe5vrah516soaCeJ+kjD17VOPV8ZLTX+VK+NjT5HKTYgY
8XdKNQWPzpPUicxNR5T38dx0NpMsS56bN2/2rFmzphsRLwwc1PUh4fGmA9GxOOx2RS5a6BC7P+xH
09rd2E6aTRfetdcukFlZoxvPKIpPZmUeRsTAeyGin95xxx07Rx4fPnzY6Gw9vLuzreV38woLdiNh
ESBEnL8cgYKIpxGKtbkFBWfkFixq6Wg9xPdpLXR6RUWOAvRPgOF/pxCwubGh5hGr42LWmZOV1SRU
28WAEP6KGULGgNuNHa2tvBETmxGWjoZfeeWVj6688soCAFgKAACIRLo2hF5vOtCx7SXJ4dBo4QKH
sveTQTSMhEjq5HQq3uu+tMCcO2d0oRwhDMrOOoCKEqgVIKIX169f/2Sk03S2th7oaG15Mb+woJYI
sgBxAUytsh0BcSGgvHpeQVFlbmFBb2dr69RH/mzK8vMLb0WECZb7pI0dra2853kS6+rqMnPz8z4G
FGsg4u8trphXWPC3ztbWHkuDY7OC5Ze3L7roohpd1y8EgGNFY4pigmYbEsFJPTVVM05bkqrs2z+I
Hm9cr3Uts7M07/VfWiizR0fmKIRJmVkHQVOD76nt9fl833/ttdfMMKcJ0d7a2t7R2vpGVlHh/whJ
KQhwCkxwKTccRMhDwEtzCwovzM8v9Jx/3jmf7tq1KyG+ICUal8vlkCDuB4Swl1NJwsHm+rr/C7xP
dtLraGtrm5dfMB8RT4vQRUHC0zpaW16O0M7YtFme0N944w3jiiuuqAOASxHxWBJUhEmq6kGvNw1G
vtna7apcfnq66O72ip5ev9VxnghzyRKn7+o182Xw9DRESZkZLWA7toDMcT0A8M177rmneyrnP9LS
crSzrfVvBYsXv0omIRCeCgjq5M8MgpBDCJ892tN3RW5BIZyycMEnhw8fNiZ/IjtRcwsLrwWBn43U
joAPd7S27LIyJhY7qQX5W3UQVwGCPWwHhLy5RYVdnS0tH1ocGktyMVuo5OGHHy4VQjwcSOoAAD7D
Jvp655NpBhIkApBav+2I9u57R1HGyX11RPBdcO5cw3VWDgV9hqgofpmReQh01TtyjIjcALB+/fr1
J/0HfdWqVZmmZrseia6PeJ9uMgS9SPCSCuazDQ0NU586x0KsXbtW2bPvwB8AoSBcOxIcNYaHruR1
22eXkrLKqxDpf0dqJ4JB1bSt3bbtna5IfRibqphVlG/evLnjiiuu2IOIl8BItb0iTNK1QeHzpQYK
5QBQFuQ75bKlqXj0qFf098d0dGkWFaZ4r/nifHPJKekQmsx9MjPjEOha4A83EfkR8bvr169vjMZr
t7e3ezpbWxrmZGU+pyr6QUmwBBGmtpkLgh0QVkkU18/LL1hYmJf7aXt7+9SnzjEAAFDtzktB4EQr
gf1qx/bGyHOUWVLqbG35KLeg8ExAKAzXjgg6oTmno7WFt05mURPzpUQfffTRc4joXwAgUFBGUgrs
789HjzdknXcEIOXDPX3a+1uOiN5+Sy/Dy6wMzb/67Dnm6csyaOznZrf1yfT0dhQi+H7/sJTyvg0b
Nrw3g2GJkvLy85Dwa4AwrTXfEUAS0XsA2hNN9e/viHaASQ5Ly8qfgcj3S93uHlzD67bPTi6Xa4Ff
KM8BQMQFoFDit7Y31LxrYVgsicU8oQMELr//P0QMTeCDg9k45J5HRCFxIhCpez/pV7fUHBFHjs7o
pUw5J0f3V5bnmMtOyyDA0DgQSaY6O8DpDKlYJaJuAPhWNC6zn6hV5eWrJMFtgHgeTPP/KxFuB5S/
aq6rewe4gGtSpWdVng0KRVz2EyU8s72hdqOVMbH4sqKiYr0guDNiB4JWp6bcsGXLluGIfRg7QXGR
0AEAqqurl8CxJWJD70WapioGBnJpzGgd4NiIXbS1u9Vdu/uUPXsH0eOZtIL8RJDTqRgrlmeYy5al
m3Nywu/Zbrf1UVpaJwStAHdcCwB8c926dTGZLnZ6RcVSzaSbEeFSQJzeLRWivYLw6cw0xxtvvfUW
F9BFUOqqeBhEhKlqBAbo6hd53fbZrbi4WFdSUp8BpEWRe9GTTXV1D1sWFEtacZPQAQAeeOCBdJvN
VgUAF4xrHB5Ox8GheRBUMBcMAUh093ixpcWtfnpgUHR2enFgYPJkhAgyK1OT2Vk2KipKMYsKHXLe
nJSxo/EARfFTqrMTUlLCXUZ90zCMn9xzzz2Dk77uDDvz3HMLTJ9xExBcBUjhv5RMrg0InnFqyos8
ggi14qyzlwtFRlwZjCS+2txQ8yMrY2LxqdTlOguEUg2R/t4SmT6Bt3xYW/uRtZGxZBNXCf04fPTR
R2+SUt6DiOPvPXk8qTg4NBcMI/yUkGB+v1QGh3zg90v0+yX4vBJ8fgm6Jki3K2DThczKtJGiTD7H
W1U9lOrsArt9XLImIh8A/Pv69et/e2Jv0TqrVq3KlIp+FQi4EQCmtasdEQwh4suKof+Kq3KPKXVV
3g+CPh+hmUxTuXHn1i0fWxoUi1slrvJ/QoFXTNBlR1Nd7R0QtIkVY1MVjwkdAACqq6vnAMC9AHD5
2DYiQvR6U3F4OAN9/tSx99ijBY+tZDdIKSl9YLcPROj2qpTywQ0bNsT1pdXi4mJdszsvMQG+hgKm
u+a7jyT9RZXGE8fWrp6dVpSXz0eC/460bjsRvN9cX3uv1XGx+HWKy5WRiuoLgJQVqY8Ecf+Oug9+
b2VcLLnEbUIfsWnTpgsA4Ft4bBnU8UxTAa83DXw+J/r8DpByaguvjCWEAbo2RLruBpttAIKWbg1G
RIeFEA/eddddfzmp17Pescp4wDsAYMV0TjBSGU+kPtncsKU5yvHFvVVlFd+XCNdHahd+2tDYWMfr
dbMQpWVnfxFQRrwNw3PT2cmK+4QOAFBVVSXy8vI+j4h3AMApE/Uln2FD029Dw9TBNHQyTR0JBBAJ
HFlaFlECoiQEiYriA0X1kar4QNU8Y5ZrHX9+ogOI+GRWVtbr119/fVSK8GKFK+OnrqSkJAttjpcB
KdItnx1NdbVftTImljCwtKziYUAoj9iD4I2m+tofWhgTSyIJkdBHHE/snwWA6xDRBRZs/+r3+1P8
fsPhcKS8QkR/bG9v/2tVVVVS3edavqryNFWRt3Bl/ORKyivvQqC7IrULkj9orK//s5UxscThcrkW
+FF5DpDnprPoS6iEHuyxxx7LNQzjMiHExQCwDKKU3KWUqtfnS/f7/M6jPT146PDhwU8OHOgf9Azf
uqOmpikarxGvXK7z8/3C95WTroyX8ILpGfrvnTt3xrzaP5pcLpfDD8orIGDcFEoAACQ4dM2ay69N
ti98LLpKyirWIcLXJ+jS5lSV63lmCZuqhE3owR566KFURVHOIiIXIpYAwKKxi9RMhogGWtrb57a1
tad3dXUNt3V2uT3e0XntBKK6ue6Dx6IefBwqLi5OVVKcVwLCbcCV8QEry8tvIMD/FbED4c+b6mte
sDAkloBOZG46kXyqub7+IQvDYkkgKRJ6ONXV1RlCiIWmaS4EAI2InEKIkVG8n4iGhBBDiNhjGMah
DRs2dJaWVfwUEC6NcMpZd290pDJeIt4BSAuneRofSfqLYvqfbGxs3B/N+Kx0QpuwLF545c7f/Y43
YWGTOpG56Sjwlu08N51NQdIm9OlYeVbFGlKgKlwbAkjpGb60ubm5J1x7khMl5eXnCRC3E1DJdE6Q
6JXxK8+quJQU+GnEDhI2NTXUPm5hSCzBTTo3nWBnU33t7cBz09kJCMFT1wAAIABJREFUmvGiskTi
VWELRKjUJgAhtJTwy3wmP9lcV/f29rqa2wXQnUA05Yp2AhCAeD4K86mSssonSsrLL4DE+UKJJOC2
CdrdbhWftywalhSGQG4EwsgDBITi0rLKaywMiSW4mG2fGo+OtLQM5xYWXgiR7hsjDHe0trxlZUzx
pr21tb2jtfWN7HlFbwkkBwIuBpzaF0NEyEPAS3MLCi7Kzy8aPn3Zafv2798ft6OQUtfZlSDo1kjt
KOmF3XW1b1kYEksCPW1t3tyC+X2A9JlIfQjgrMLcUza3tx90WxkbS0w8Qh+DSL4fqQ0BVkPijCpn
1O7Gmr3NDXU/0sh2DUr4FRFMvaId8VQp4J96Bt2bS8or7youLk6dgVCjwIyYzIHAMFXxtIXBsCTS
VP/By0AQcREiRHCawvNtK2NiiYtH6GPk5eebgOLKsI0IjtyC/P/paG09anFYcaut7eBgR1tLbd6c
nN+BonYD0mkA6JzSSRAcCOBCVV+bV1g0J3fRwo87Dh0amqGQp6TEtfp0FBRxGVckfKO5ruZlK2Ni
yaUoP69ZgrgGMMLfY8QluXmFuzvaWmKygyNLHDxCH2PZKadsn2i0iaicY2U8iaKpqWmoqb72WdPt
vkpI+DEQ7p/qORDBCUBfBr/xUomr/CerVq1aFP1IpxqTecsEzeQz4deWBcOSUkNDw0FC/M8JOynw
/dWrV093bQg2S/AIfYxdu3ZRXn5RMSAsDttBotrR1sIjsgi6urrM9raWvR2tLS/MKyzYLUAUAEDu
FE+jIOJpoCjX5RYUnDF3/vy2zpaWjpmIdyKllZVFRPQPiOG30iWCD3ZureXL7eykzc3KbBaqfhEg
RNq8Jc0wSOloa6m1NDCWUHiEHoYUuCViI8qV8XuvN65ErTJeSHoyJpXxJt0YaUc1AAABkfdDZ2wq
du7c6QMyfwYT/I4Q0s0rKyqWWhgWSzA8Qg8jb9GCoyDlV8I2Igqh67s6Wlr2WRxWwhqpjJ+Tt+Bv
CPKkKuPn5RdePK9ovpx77upPunbtmrHNcVatWpVJQv0JIITdvQ+Bdm+vr39wpl6fzT4dbW1tuQWF
hYAQPmkjCiA4vaO15Y8wCzZCYlPHCT2MjkOHhublF34OI13+IhjoaG15x+KwEl5X2+HuzrbWv2UV
Ff5BAA4DwTKcYJOKcBAhG4HOV3r6rp5XWOTISkv96OjRo1FfnW3u/IW3IlJlxDik/GVHW9sn0X5d
Nrs58/O26aB8ERDC3y9HmJdbUHS0o7Vll8WhsQTAl9wjQYh82R3oPOsCST4f1tYeba6reRR9niuA
4N8AaMprvRNCDgLdpadlvFJaXvm90nPOmRet+FavXp2Ckm6I1I4Eh6658sq/ROv1GBvxaUNDHwD+
x0R9COib0fz3zpIHj9AjyMsrAhBwedhGROe8woK/dLa2zsZlYKOmo6PD39HasmNOVtbvVEU/SMcu
xWdO5RzHR/grQMrr5+UXLMybW7S/o6Ol92TiyszP/xIiXhypXSJVP//MMztO5jUYi6Sj9fBHufmF
qwChMFw7Iuhg0NyOtpa/Wh0bi288Qo/AXLJgKxB6IrUrJqy2Mp5ktnPnTl9jQ+3mpvqa6wnoO0g4
nW1qNRR4Odrgt6Vl5b9cUVlZOp1Y1q5dqwjCmyN2IOyZ43T+cTrnZuwEkQbmz4Eg8q0kQZ8/XiTK
WACP0CPo2rXLzC0sWAmAC8K1SwTsbG191eq4khx1trYe6GhteSm/sKCWCLIAcQFMrbIdAXEhElw1
r6CoMrewoLeztfWEF+TQUlIuASGujhgg4n/Vvv/e/2fvzMOjus77/33PnUU7EkiaVWIzYCwQ4EEo
4I04iR2vsRPjbI6z1AaStGnrpP0laZsQp0376y9L6zYxeIljO85iJ/GGndhxYhLHYCRkQGzG7KCZ
0UhIQttIs9zz/v4QEiOYO1rQXI2k83kenod73zP3fmcezbz3nPMu20egR6EYMcFgsL3U49UI8BmN
EUxLvC7nc8FgMGamNkXmomboKSAgRRlYunz16tVZZuqZSuyqrd1Vv6P273Vd+zgYvwFSzFYMIOIl
BPr+Yt+KX1cuX/HxijVrhgrAIybtMyns4R6BX4xUh0IxGmwy/hgYhtk0THDGIO4xU5Mis1Ez9BR4
Xa5OSSJ5cBRB64rqu5sDDadMljWlaA42tIYC/jeKvJ7n+iLjaT4R7CO5BhGmgbBqqMj4JcuXrwBR
qrrtvzlQW/P6KN6GQjFigsGgdLicR0DiZhivUi1yuN1vqHLUCkDN0FNSV1d3EkwNRnaNWO2jm8S5
yPiem8H4HpibRnqN/sh4e960l5JFxksI4zKvzLpmtz41CukKxaipr6t7G4zNhgOINED804YNG9Rv
uULN0IfC5faUM6EimY0lCpqC/l+arWkq0x8Z73W5ngaLUwzMSlEuMzkEK86LjHeUuRxE9LcpXvT7
3dvfev7i1CsUIyfX5dw1RG56yf7Dh1qb/Co3faqjHPoQlHjcGoGuT2YjwjRHmfflkN/fYbauqU4w
GJRna8b/utTjPiBYuECjqxlPFtxBjNuZKJeAeJJxHBX4xmm/Xy1rKkynLRiMODzuMwCtNhzEWOac
NfPlTOlSqBgf1DLNEORZLLVIEZAlpVTd18aXvprxO7Z/btQ14xl2JlQQYxaYZgIoEIn9WCTXvFNT
8+7YylYohk99be1mSBg2ZiFCLsXi95mpSZF5KIc+BNu2beuBxC4ju8b0HjP1KIzpj4y3Sv0jAP0i
ZR5vIoTpQL8H5xwwPCzlXHD/eU21SFWMN0PmpjPwfpWbPrVRS+7DwOHxzADBoK43lRYXFT7V3Nyc
tkYhipERDAbbQwH/1uFExhOggeHGBVHEpAHII7CVBb1TkOM91Nrqj6RfvUKRHJWbrhgK5dCHQYnL
2UUk1iQ1EqyaxVIXCgT8JstSDMFpv7+nKeCvK3M5n5EQrQBfAqLcxDHEmAHAsB0uEbUAWGS1Y43D
653hmDXzsNqnVIwXZS5nvYR4n2EgKCFPMmmhYEAVP5qCKIc+DJqCwTan23MryOCHn9GivkCZSzAY
TB4Zz0xE5IHx1lMUhEYAF0TGO7yeE6qWv8JsVG66IhXKoQ+TUo97DoEuNTDnhgKBX5kqSDFiLoiM
h1jJQNLSvgAAQjOA8+v590XGg+5wuN2Xub3exka/P5RW4QpFAqFgMFjqcbsItCDpACIB0MLPr733
+S1btqi+6VMIFRQ3TAgp2qkSXbKounqkKVOK8UNeOmvWmwzuAnACjC46f65D0MHcnuIaBKKrdMaj
S6qqnlzqW3GTKu6hMIseIf6LmFsNBxAu+9VLL91hoiRFBqBm6MOkMD//tMVm/1Tf028SJB1tCvgP
mixLMUpsOTnvZ6LbQYiB0AHmDhABjCwQiIAWEA1zr5xKmPDed9499EGH2yOKr1j1bvP+/SpIUpE2
Wv3+iNPpbYPAasNBTEtVbvrUQjn0YdLS0hJ1uL3vAcGZzC4IsVDA/5rZuhSjw+H2bgChZOAEkQ6g
mwlnAIoAFDi7bz58BmrGn7m91FOWrSLjFekkFPQP2TeddOlUv0tTB7VEODIMl90lU/WaNWvUA9IE
YOnSqiomXJbMRkBcAz9s5fj1o68ZT9MJvDZnGm9OVjNeoRgrhsxNJ7xvcdUqlZs+RVAOaAQUl3kj
gnF7MhsR7Gfa299SAVKZT4nX+1UilCU1MuvCbvunt7dvb02MjJeMmXSRNeNVZLxirBlebrpUuelT
BOXQR0Cz39/idLs/AqKkTRIYfDoUCOwwW5di+FQuX76AiP7OcADjtd3b33qu/7A/Mr4p2BcZDxZO
Mth2ScGgyHin292m6hYoxoph5qZbVGrt5EctuY8MKRlvGRmJSbVTzXCYtU+mMkc1+omBTe6prf3z
nh3b/0qA7yHgNWaWI7w9gegqJvEjFRmvGCvq6upiYP3fkaqHAeETlcuXJ09zU0wa1Ax9hDg87iwi
ujaZjQgziovKf93c3NBjti7F0Ph8V7kkxf7ZOFMBtft21AxZt70xEGgMBfyvlXo8vyMIgDEfNNLv
Ul9k/IF3D9/gcHvo8iWVhw4fPqwi4xWjQuWmKwDl0EeMu7T0NDTtLiSv0kQWi36oMRA4ZLYuxdCU
up1rIWiJ4QBJ/x4K+huGe72mQKAjFPBvLZ5Z/ixJ9BBjHgxqxhtCKABhVVd3WEXGKy6KgrKynTbJ
txhtCYJQ8s6hd8+EAoF9JktTmIRy6COksbGx1+H2XDUo5SkByaKnKeh/3WxditTM8fmm2Uj7tlEq
GoHfqa+reWA0125uaOhpCvjrvClqxg8JUTYBvv6a8SVl3iNNfr/KH1YMm1a/P+JyeVuZ8F7DQZKW
OWbPfEnlpk9O1P7dKJACW41sRLwK6nPNOPJIuwPEyWcuAFjHTy/2HnV1deH6HTU/t7L8kJD4Jksc
HfFFBHIA/piQ/NxiX9X9i6uq5lysLsXUYVddzUup+qZDIAfR+FdMlKQwEeV4RoE1ZRlYFFZUVxvV
fFeMAzfccIOdwB81HMDU8OFbb3p1rO5XV1cX21VX89KeupqPMvg+Zto9istYSdCNBPplpW/Fj1Sf
a8VwGSo3HYRrVW765EQtuY+C9ffe23zg4KGPGu2XConGUMC/02xdiuTkFM64DYTrjEfIh375s5/t
Sce9mwKBE00B/wslzrI3AJkFYC7RBZXjU0EgeAh0vdPjvtrl8kbWr7v3iApsUhjRl5teJgi83GiM
yk2fnCiHPgq2bNnCTq9nIQCj5VBrKOB/wUxNiuRs2LBBHHj38L+DUJB0AOPM9Lzcbxw/fjyeTh1N
wYbTTcHA686yst+CCcyYRwTLyK5CxSoyXjEcylyOPTqLaw2LIRHyJDRrKOA3TMNVTDyUQx8lDndZ
DoivSW7lksL8/F+2tLQYL3spTKG1u/taED5sZGfgyZqtb5pWcCPk93eEAv6tJTPLnxuzyPgy76FW
v4qMV5wjGAxKl8d1GES3wKBvOoMXOVwz32gKNpw2WZ4iTag99FFi5dhWGBVyINLsBQUrzFWkSArT
pw1NjAgiPU+bKaeffdu2te6p3f6QlfWb+2rGY8Qlgwdqxsu+mvGqha8ikd07duxk8ItGdiISgvSv
q+JGkwc1Qx8lwWAw7HC7rwXRjGR2BsJNgcCfzdalOMfll1f7pMDnjOyCxbP1u94e105UwWAw1lcz
3vnMqGvGo69mPEl8tNTlLi91u042BYOqZrxiWLnpB9492B4KBPaaLE2RBpRDvwgcLo8HlLxQCTGm
hwKBn5mtSXGOEq/7qwCVJzUy61qW9euNp051miwrKQk1439V6nG/Q5KKjNpiGkIQRDSPSNzhcHmW
lXrdnU2BwIk0SVZMAFr9/ojLXdaSMjedaanKTZ8cKId+EbgcHska3ZzUSJRb7Cz/Y3OwodVkWQoA
S1asmA/Q3xvZmcUfdm/f9pyRfTxpCgROhIL+l1RkvGIsaAz4D6Xqmw6CFTq7QgH/702Wphhj1N7J
RaBpchckwoZ2oa8yU4/iHFLnVE1YIC140iwto2Xv228d2FNX+w3SxIcB+gUzRhz4xqBLpcC3frP5
t89WLl/x8RtuuGFkAXiKSYEU/O+pc9P52sVVKw2CfBUTBTVDvwiCwaB0ejyLQZiZdACDQkH/SybL
mvJUVFU5BeifQQYPrIzavbU1PzFX1egZiIwvKn+OrOghqSLjFSOjKRDocLg8BIJhbjoxL1W56RMb
NUO/SKRIUTVOYJnP58sxUY4CgGD6OFLkeEvijJ+dJ2PfvrOR8Ri7yPiKqqqR9nZXTFCs0B9PWY6Y
4IhDW2+iJMUYo2boF4ln1qwzrMuPG5g1nWiPCkwyjzk+3zR7iiYsAA7uqa39b1NFjTH9kfEL5897
OhKJXVRkvGC6U0XGTw2GmZteUeos/4vKTZ+YKId+kTSeOtXpcHuvB6EwmV1jam8M+N80W9dUpdxT
/kn0NchJimD5wGRpb3v8+PGByHin27ULQAGIkm//GHEuMn5Nqdtb7fC4z6gH0MlLKBBoLPW4nQRK
2m+CiEgIufDza9eqvukTELXkPgYQS8PuaxK40kwtU5m+gC/5sRRDgvNmz37FNEHmwbt37Kip31H7
9yy1u1jyy8wsR3oRIl5CoO9XVq14aqlvxU2q4MjkpEeI/yZmw+wbBi38zeaXjZsZKTIWNUMfA0q8
HiLQDUmNhHyvy/m7YDDYbrKsKUdWUfGHKEUTFpZ4+PXXfl9vpiazGZua8eivGX+jqhk/+RhebjpU
bvoERD2BjwFlxcV1qVKK4kKsNFPPVGTDhg1CMN9tOECiPc+mPWuipHGlfvv2hvra7d+VPdotDHoI
Eh0jvgixB4Qv+5tbNy+uql57SXV18gY3ignHrh3bX4Zk4x4GAjmI6P9goiTFGKBm6GPA4cOHdYfb
s4wIZUZjQoHA78zUNNVoDYffC+AjhgOIn6rbvt04I2GS0tzc0NMU8Nd53c5nJEQrAXNAyBvRRQjZ
BPisjDUOj3dGscd9tDkQ6EqTZIVJlHg9e8B0u+EKDmF2ibvs3aZAw3FzlSlGi3LoY4TD5SkiQtKZ
ODM5fEsqn1LLlunD4fJ8C4SSZDZmRGSP5Z+amxt6zNaVKSSJjC8nwvQRXmYgMt7p8VxSXOYNNPv9
zenQq0g/TYFAh9PtIRCqjMYQWPVNn0Aohz5GOEs8XbDgzmQ2Ilg6O3t3hoL+BrN1TQUqfb7LIYRh
ExYien7vrrdUWUsMjox3edw1zCgaTWQ8gDmCcbuKjJ/YeF3OvUP1TWcW9lDQP+VWtyYiyqGPEaGQ
/4zD7bkZhPxkdia0NQX8b5mtayrg8Hr/j1ETFmaWwqp9PdTQkBFNWDKJxkCgMRQIvOJwu/7EjGyM
vGY8iOAk0PUOj+cal8sTuerKVUf379+v0p0mCMFgULq97kMMlZs+GVAOfQxxeLyzAFyW1MjIawr6
nzFV0BRgkc83l0jcB4MfIwH64+6a7b8xWdaEIhQItDQFA6+7Zs58GRJ0MZHxLW3tNzncHiycP+/w
8ePH42kRrBhTGvty0x0qN33ioxz6GFLiLrMQcdK0KSIUeV1zXgwGT6pgojHE6Sn7WxAWGNk1jTY0
qn3eYRFqaOgcg5rx+SCs6onGby/1eLPzXM7DbcGgqhmf4RSUle1K2TcdVLL/4KHOpqB/j7nKFCNB
OfQxpMzlaJIk7oLB5xonPt4UaDhgsqxJy1BNWJi5bndtzWNm65rojGVkvA3anQ6Pd4bXNeeYepjN
XPpy090tTGSYm06MJSXl3peb/H6Vm56hqDz0MaSuri7MzIaFSwTze8zUM9nRWHwsVRMWJjxupp7J
Rl1dXbh+R83Pi/JybmPwV4mxf8QXIc4G+GNxEXm+cnnVD5ZVVyffklKMO7t27BgyN11I+XUTJSlG
iJqhjzFup6eYBa1IZmOg9LL58356/PjxEZflVAxmwYIF+Rab/V8Nm7Aw3t2zo/a/TJY1KTl+/Lhs
CgSOhgL+Z0cdGQ8QiGayiozPaIbMTQeVO8u8h0J+/3FThSmGhXLoY4yjzBuGQYETIth6Ir01oWAw
aLKsSYd3ziWfBOEKI7sA/XdjwD8pmrBkEudHxvctx9OIVvoGIuPdntUul6dXRcZnDk2BQIfL7UWq
3HQwLi8uKnyuubk5aqI0xTBQDn2MCfn9rQ6P+3aAcpPZGTjdFAjUmq1rMlGxZo1NtLX9u3EAD4JF
eTnfUSsh6aM/Mt45c+ZvIUFguiTV9kdSCDNUZHzmMWRuOpCjaVZ7KBhQuekZhnLoacDh9l5iFHlN
RDmhgF+lUV0Ejry8Wwl0vZGdJR6u2fbmbjM1TVX6I+NLZ0x/FhZbL0lcAkLWiC6iIuMziuHkphNR
Ramr/K2mYEOTyfIUKVAOPQ04XU47SLzPwDzD63I+GwwGw6aKmjwIh9Pzb0SYltTa14TlGw0NDWqm
ZyJNTU29ZyPjfzUmkfFuj8vrcp5QXQrHh8ZAoNHh9pSCsNBgCBFkxdVXXPGc2i7JHJRDTwP5ueXN
liz+lEHVLWIpDoeC/ndNFzYJWFJdvRrAGsMBxD+bik1YMoX+mvGhgP8XpR73AWIqM6qxbwjBCsJC
JrHG4XZf5i4rO6VqCZhPfo53ty0rRW460YzTre0qNz2DUA49DbS2+iMud9lKEBxJBxAioYD/jybL
mhScbcJSmsymmrBkFNwUCJxIQ2T8ybSoVVxAa6s/Uup2nyaia43GEGiZe/as3zWeOqVKK2cAyqGn
iVKP10GAL6mRUfL5dff+VJVRHBlLli9fBqK/MrIT8MLe3dtfNVOTYmj6I+OdXs8Wlqwi4ycQTYHA
YYfLvQRE3qQDCBYZlzObAv7fmixNkQTl0NOE0z0zApK3JTUSsg68e+zNUOCUCigZAU639x9BSDrL
62vCYvmaasKSuYT8/pamYOB19+zZL7POKjJ+gjBUbjoRyhxez+GQ33/MbG2KwSiHniZCgVOnHW7v
HSAk3X9i4qamgL/ObF0TlcVVVXNA9GUYRd2CXq9XTVgmBI2nTo1hZHzsw6Ueb5a7tORIY2Njb5ok
T2mGlZsOLFO56eOPKv2aPiTANUZGwVBlYEfGXTBw5gCgafQT86QoxoI9e/a07and/lCuTbtZQnyH
JUa+P04oJPBaabW9vNhXdb/P50vaRldxcVg4/iRLHE0xpFjLyVtvmiBFUkbU+1gxMpb6VtwkBb6V
zMbMspvlB47W1am0nCFYVF3tEDo/b7g8K+nt+rrta02WpRh7xOKqqiuJ6R6QQRviISBAMvObRHhk
d23tvrEWOJWpXL5qEVH8x2wwESRASqn91Z66bSrqfZxQM/Q0ErNp2wAkDdwhIpEPVJssaUIi4vKj
qfZaCXjCTD2KtCH31Nb+uX5Hzd0CfA+Y34DB98cIBgSIrmLQ44uXVz+6uKrqaqiJy5hQv2PrXmY8
Z2RnQBDFv7569eqRxUUoxgy1h55Gmhsaepwe9zUAFScfIcKhgP9P5qqaWPQ1Ycn6N6MmLCxxpL6u
5gdm61Kkl4TI+D+pyPjMobiocKewWm8yKm0Nohm9vdGuUDBg2HVSkT6UQ08zDo/HCdCyZDYCikMB
/1Nma5pIeGbN/TgErjSyC4kHVJGeyUs6IuPnzCw/oioJjo7m5uaow+lpgTDOTQeJpSo3fXxQDj3N
OFwuHSRuSWok5Di9ni0hv7/FZFkTgoo1a2zamTP/YVSpihiNRfk5/6qasEx++iPjXaUlv5Ga5aIi
42M6f9jp8kzzup1HVQnmkRMKBg47PO7LAEoegKhy08cN5dDTzNVXXtl0uq3940SwJbMLnYONwcAu
s3VNBJw5+TeD8EEjO0l+ZPu2reqzm0I0Njb2NgX8dcXTC39h0WwnJWOuYV1/IwhZICyVJO4sdbln
lrldR1TN+JHhnj27nuN8m9FWmMpNHx+UQ08z+/fvZ6fbexkIs5PZJUFrCgQ2m61rAiCcbu+/gVCY
zMhMnVbo/xIMBmNmC1OMP83NzXpj0H+oKeh/5mzNeK9RSeAUaEQ0r79mvMM9y6+KPQ2PxlOnOp1u
Lw2Vm16Yn/d8S0uLyk03CRXlbgKS6C0jG4GWVFRUjKwr1RRgcdXKq0Ccova3/qu6ujq1XKroj4z/
9MVGxoPiP1GR8cNn/uzyx8FIFb9SnJ0/7fOmCVKoGboZOGeVt0DKTyY1EgQsWXubAg3HzVWV2Tjc
nm8QwZnUyIhKq+XrzQ2qCYviHP2R8UVez5/ERUfGu9/rcnlVZHwK9u/fzw73zINE8lYYPQARFpaU
ebc3+f0hc9VNTZRDN4HQqVPdpS7P+4lQlMxOhM5QwP8Xs3VlKstWrFjCQKpCMS/srVFNWBTJOT0m
kfGkIuOHQShwqsnh9pSk7JsuuWLh/PnPqeDV9KOW3E2CiLYaGplXmigl45ESnzayESCtrD9pph7F
xGTnm28G6mu3f1fEIzcz6CEwzoz4IgQ3CF/uium/rayq/orP5zOoKTF10Xu6HwDYuF890SVtXT0f
N1HSlEXN0E3C4SpjEN+U1EjId5WWvNrY2DjyH5xJxlBNWCBpy6662l+Zq0oxkRmIjC8afWT82SyV
Rf2R8R6n42hjY6OKjEdfbrrT6T0NgfcZjyKVm24CaoZuEnpv504AhkFcumZbZaKcTCZlExYS8ifm
SVFMJvbt2xfdVVfz0p66mjsYfB+AvaO4jI0E3Sgt1mcql1f9oHL5qkVjrXMisvvtmlcANt42JM6K
R2JfNVHSlETN0E2iublZd3jcSwyLMQCY6oUYFlVXO4TEN0CGD5o762trHzVVlGIywk2BwIlQwP+c
y+OuYUYRiMoxssh2AtFMkLyt1O2tdnjcZ5oCgZF3i5tEeF1zd0vI21PmpnvcR0KBgMpNTxPKoZuI
0+OZBtAVyWwEOBbOn/fU8ePHp2zgjdPp/iuI5GVyAYDB/68pEDhhpibF5CYdkfGXLph3bCoGgAWD
J7ucHi8ArDAaQ0yXq9z09KEcuol4Xa5OSeKjSY0ErTsW3dUUCJwyWVZGsGDBgnzNnvWvRhX1WOLo
nh213zNbl2JqkCQyfq7RTNOQs5HxPbHYTQ6Xx1Y8vfBIc3PzlHJcV1+xak9LW/s1IMxIOoCQY7Nl
5TQG/G+aLG1KoBy6iQSDwXan23MDDAJyhMSZUDCwzWxdmYBn9tyPEeEqIztB/E8o0HDQTE2KqUdC
zfhnmbR2EOYCyBnhZfJBqCaLbY3T4y12O+Ycamw8OSWKIKnc9PFFOXSTcbk9M5lQkdwqCkIB/9Pm
Khp/fD6fVQr6jlFLRmI0Ts/L/vZUXMZUjA+NjY29oaB/d3FR4dMWzXaSQXOMyhAb0R8Zz0KfUpHx
Kjd9/FAO3WRKnR4BYdBwhFDonFn+UqihYUqldpR4Zt4Mwo1GdgI9un3rm6oJi8J0+mvGhwL+X5V6
3AcI5AFGVzMeQlvjcLsvK3XNDDQFGyZ1zfhh9E2f3hONhUN2iuitAAAgAElEQVQB/26TpU1qVNqa
yeTatR0ADPfVOCanWpEZAbBhIRlm6rRw/NdmClIoktBXM7625jMXWzOehP7YZK8Zv2/fvi7S6b9S
j6K1S1au9JijaGqgZugm09DQEHe4PD4Qkv4hE6CHAv4pU9Z0cdWqq4hk8kDBPn6+q26HCqBRZAz9
kfHTS71bBHEOgWanSLVMSkJk/LUul7dnMkbGh4L+Iw63eyGIkjdZIlhYZ9U3fQxRDn0ccHq800F4
T3IrOYqLCp9qbm7WzVU1Pjjdrn9ByiYs2tdUExZFJnK60d/aFAy87nXNeUmSFKOMjJ9+NjL+tlKP
N6ekqPDgZIqM97rm1g+Vm17qcR9tCgSOmq1tMqIc+jhQ4nJ2E4k1SY0Eq5VstY2N/oDJskxnUXV1
JQHrjOxM/OLe7dtfMVOTQjFSgsGTXaGAf6ujeMbT0CytIJ5nuHdsTA4BvskWGR8MnuxyOd3Mggxz
0wWT6ps+Rqg99HFgb13dEWI0GtmlwJTYR9ck7jayESAt8bhqwqKYMNTX13fX76j5uR4Of0hIfBNM
Iy6CRIRcgD+mWyLPL/ZV3b906dJZaZBqKvPmznoyVd90JszIyiv6gpmaJitqhj5OlHrccwh0aXIr
54YCgUkdCLa4qmoOgK/AICiIQH/aVbfjGXNVKRQXz/mR8QLCDcAxwsv0RcZr2h0Ot/uykrKy4ETN
296/fz87Pe53CPQhGH3fiVVu+hgwKSMsJwKVK1ZcC8Z/GpgZVstN9Vu3TtrUlsVVVf9MoNuM7AT+
9O7a2n1malIo0sXSqqqlkvFpEF2JUf7uMtNukHx8T23tiCPsM4HKquqvAfwRwwHMh6fn5d61ZcuW
YZe/3rRpU7EQYqau6zOJqJyZnUQkpJR5RGRh5rgQQmfmbgAQQgQBHJNSHs7Ly2u46667Oi7+nWUO
yqGPE5WVlbmwZf0BBEvSASzur9/x1gsmyzKFZcuuKtEtkeeB5GVewdhVv6PmHnNVKRTpZ+HS6nkW
TX6KiK4z/O4PBfNhwfRkYX7OKyNxfuNNZWVlLuz2XwFUYjiI8UD9jponjMyPPPLIdCnl5cy8HMBy
ALMuUlYAwFtCiLeklHXr1q2b0IV/lEMfRyqrVjwMIGkzEpb0+z11279msiRTWLx8xV8T4TNGdobl
vj21W/9soiSFwlR8vqtccUTukISPECFvNNcgRosk+nW048zPDx48OCGKUS3xVV/Hgr9jOICpl6zi
o7u3bfP3n/r+97+fnZOT814iuhF9jV/SFfslmbkWwEvhcPj1++67b8Jl1yiHPo4sWV79OSZOHgzC
6Fgwe+YHnnnmmUmVvlZRUZEnsnNf6gv+uRCWOLqnruajmIBLigrFSDm7UncriO9OOXNNATO6iehF
WLUnJsI2XeXyqh+AyLBvAzO27dlR8zebNm0qZ+a7AVxHRMOqp89SCmIWkFKAzzp+gmQhJIgkCTGs
XH9mDhPR74QQT9x7770Nw3lNJqAc+jiy6PL3LBSaNIzkloI+t3f79nozNaWbJcurP8XEf2s4YBJv
NSgURlRUVNisWbkfkESfBfGsUV4mxpJ/TzF6rL6+JmN7jvt8vvIYab+AQWfFosJp9vdf896dpSUz
LkWq2Xg0bkcskkOxeBakbkNct0HK1NsYQsRh0aIQWpStll622sNks0RSvEIy82sWi+XH99xzz+Hh
vL/xRDn08YWWLK96hYmmJzMy4+E9O2o2mS0qXfh8PmuMxPMgSl4LmxGanpfzoYm0L6hQjDFicVXV
lQLiswxePJoLUJ8TelNq4rFMnRBU+lZ8GgJ/k3gu256l+ZYtKZ43Z248OzurlYgGr9IxEyKRPPT2
FlA0ljOk8x4uQsTZZg0jK6sDdnsXzr8vAGbWmfnXsVhs45e+9KWMDaRTaWvjTKnLM4+I5iWzEZAV
CvifM1tTuijxem8C0U0phvx4+9Y3d5omSKHIPLgpEDgRCvifd3ncNcwoAlE5Rjb5IhDNJMaHSt3e
aofHfaYpEDiZLsGj4eorV+1N7Ju+4JK5hddceWVRudfbZrfbOokS3m4sZkNXdwl1dLqpp7eQ4rod
zGO3j84sKK7bqTdSQD09RYjrVmgiCk0b2O4kIkFEFZqmfeiWW27p2Lx5c0a2clYz9HFm8fLlNxCJ
byezESDjYe2D+/ZtazVbVxoQlcurnzZaTmSmTor23FxfX99tsi6FIqOpuHzlJYLid19MZDxLHGEh
fsmzyjbve+aZjKjItqSqqiIrK+uJVdXVpbPLy3vtdvvgCPNoLIu6u0oQiaYMGiRdsujoiNCZtii1
tUcRjUgRiemIRiRsdsEEgt0u2G7TZGGhTRZOs9G0aTY56KkhCXZbF+fmNcNm7U1i3RKJRO7PtNm6
cujjzNKlSwvZanuVjfaKdP7n+rdrf2eyrDGn8vIVV0HDDwwHSH6ivq72ARMlKRQTiktXrJhhZfoI
mD8xGSLjH3744coz7e0/yc3J0TRNiw0YdF2jzq5SikSmMfMFPooApsbGHq0h2K2dOBEW/kAPxeMj
63wnBMmZZdly1qxcvcybK4tnZHESf0hEzHZ7O+fnNSXO2M8SIKKvrV27NmPqZSiHngFULl/xOAgV
yWws+aU9dbXfNFvTWFPpq34Igi83MMe0uP3WnTvfaDZVlEIxAZkMkfEbN268kYi+AZy34hAOF1JX
dymkvGA7mNrbo5YD75yx7j3QTh0dYxpnIwsLrLGKimly4YJpsqDgwmA9IeKcl9uMnJwz51nizHz/
+vXrXx5LPaNFOfQMYPHyFeuIcG9SI1Nb/Y7t1wOYsK0VF1VXVwrJPzayM/iFPbW195upSaGY6Ph8
PqsO7bqJFhm/cePGvyGiTw86qesWam/3IBq7ID1Naz7dY926vVk7ciT923FE0OfPy4utWF6slxRn
X2C2WbvltGkBaNqgBwpmfnz9+vX/k3Z9Q6AcegYwlMOTuvjU3rffOmCmprGkcnn1f4L42mQ2AqSI
x9bs3LlzxI0sFAoFgP7IeBafYeLK0VzArMj4Bx988O+FEJ8cdDISyaX2Dvf5UevUHY7Z/rK1Sdu3
v8NsR8UA9MpFBbErVjpkdvbgVQQh4jytIAC7/fwHjJ+sW7fuf00TmQQV5Z4BfOHee5sPHDz0URDs
yeyC0BgK+Cdk9Hdl5YrZZME/wKgpA+ONXW/XPW2yLIViMjEhIuMffPDBe4UQnx10066u6dTR6UmM
Wicw2+r3tWa98KJfBBt7x2PWSQBEqCli3bPvDOfkCi4tyUL/58ksqLd3GgESNltiNbmlt9xyCzZv
3lw3DpIBKIeeEWzZsoVL3d5LiTA36QCCJRTwv2iyrDHBUeb5AgiXGdkF8bcbAwHDVrIKhWL4NAYC
jaFA4JUSl/OPBKEBmAsa2e88EZwEut7p9tzgcHtE8RWr3m3ev/+iKlY+9NBDnySivx50sqOzlLrD
g2IARFdX1P7si6csu+vboevjXy1S19ly5Gi3OHmqS59Vngeb7dxnGY3lQbI4b6buu/XWW7tffPHF
PeaLVQ49Y3B6ynJBfE1SI3NpYX7+L1taWjIi3WS4+Hy+YinEN2Hwd0ZM9bsnUeEchSJTaAoG20IB
/xtFXs9zAtQDpvlksAJoCGEaCKu0tjO3l3rKsovy894dzW/Qgw8+uJqI/gUJKwbU2VVM4XBx4jiL
P9Bl//Vzp0RLa+yCi4wzorMzbjl4qEN6XFmclzcQNEexWA4xALstnDC8+uabbz64efNm07cRlUPP
ELwuR4sk8UkkWyYjEpasrP0hvz9jyzkmo9jj+SwRLTeyS4j/1xRoOG6iJIViSnHa7+9pCvjrnMUz
fgXN0grwJSBK2kfBEKJsAnwWa9adDq93hmPWzMOhU6eGFaD28MMPzwbwP0jorEhdXdPR3T2oWqT1
wME2+/ObAxSNjv+s3ACKRqVl7/52FBZaZGLAXCyWe97yOwG46rbbbvvjCy+8YGr3NuXQM4RgMBh2
uN3XgmhG0gGMrlDA/4bJskZNRUVFHlnt3yGDes0scXRv3fbvmq1LoZiKhEKhWCjg3+t1uZ4Gi1MM
zAKhaEQXIVgBLIKUd5a63DMdXs+JpkCgzWj4hg0bbLm5uf9NRK6BS/T25lNnlwsJExdL/Z5W26uv
hSZKhLY4fKSL83I16SgdcOoUi+eyRYvAYokCABFZpZSLbrnllpc2b95sWoZSutrQKUYBMW01tvIV
5im5eCz2nNuMOqqd5WdQHdUUClOpq6uL7aqreal+R81HGXwfMY0mot1Kgm4UoF9ULq/6wbIVK5Yk
G+R0Ov+aiC4dOBGNZVF7hyexWIx134E2+2uvTxhnDvQ9idh+/8eQ5Z2DAznpzEyivcODaCxrYBxR
BYAvmqlNOfQMQkhsMzQSlS6uqppjopxR4/P5rCzwCeMR3Cx7uzOiEINCMUWRe2pr/7x7x/bPCfA9
YH4DI3zAZkCA6Cqd8eji5dWPLq6qev+GDRsEAPzv//7vfAAfHRgrpRDt7YOcueXosQ7bq69NyIBY
AmD/7atBy4mTA9X2mJmovd3DUib61U/86Ec/WmCWLrXknkF4PM5myeITZ5e2LkDo8IeCgYzsnpRI
qavsRgjjJixCx2N76neNW2qHQqE4R39kvNflfEWSxmDMH2Vk/PvfeffQB0tdHm3F8ss/I4Rw9ttF
e4cTsdjAip1obevN+vVzp6BfVPD8uKMdPtIp58/L4+ysvlx1Zo0ka8iyd50dQkQ0f/ny5S9u2bIl
7SuSaoaeQdTV1cWIUGtkZ8JKM/WMEsECnzYyMqNLxiPPmClIoVAMTV1d3cn62u3fJau2hqR4BkzJ
mpKkhAlll86be78ej1cPnIxEctHbWzhwHItJ++aX/YjFJvyWG8VibN/8sp/i8XP75D09RRSNDlS8
I6LFbrf7ZjP0KIeeYTDIeNld0DKfz3dBacRMYomvehUIs43sxPys6qimUGQuu7dt8++ue+v/Wjl+
HRjfA/Owa71rQlDlooosm83W9x1nJurodCaOsf/5jUZxemKl4KaCmk9HbX96Y/DWQUenEwnbC1LK
e55++um0r4grh55haHZLisA42GKs+UwTMwoYuDuFOQa79eemiVEoFKOmrq4uXL+j5udWlh8SEt8E
Y8i02flz5xZOKyg4l5Pd3V0EXR/IdNFONXRZdu81NZXLDCy797RbGvxdAyficTvC4YFVCSJynzlz
xnAbcqxQDj3D2PnmmwEwGRYkECJzl90XVVdXpuioBgb/djw6OykUitEz3Mh4TRAtXDA/x2639/UI
ZyYK9wyk4Qpmtm/5c8gk2aZj/eOfQsQ8sI1A3eHi82bpn+oPGkwXyqFnIMTScJbOyFyHLnS+y8hG
gNRisSfM1KNQKMaUQZHxBLzGzAN7x+Xe8rzCwsJzs/NwuDCx4YrYu6+Nmk9PmqX28xGnT0e1fQfO
tVeV0nLeLH22w+G4Oq0a0nlxxejQhXH6GhPKFlVVlZmpZzj4fL5yIqw2HMD4y65du46bJkihUKSN
XbW1u3bX1nyVCR8B6BdgROfOmZWVZbcPODQR7pne/3+SUtq21bSMj1rzsL1Vc1okzNITPwMAEEKk
NThOOfQMhGfN2jFEhGnGzdJjpN3FKf+e5JPmqVEoFGawt7b2VH3t9u8uXlxxz6zy8i4i6nNmkUgu
J+ydWw4eaqeurrjhhSYJ1NERF+8eGogRYF23IRJJLLC16oEHHihI1/2VQ89A9j3zTJTBbxvZBWeW
Q/f5fMUgGD559jVh2TEh278qFIqhuaq6erE9oZUo9fRMS7Rbdu42LBE72bC8Pfi9Uk9vogO3Wa3W
96Xr3sqhZyqMt4yNYnlFRUXSGunjQUyIO4HkNdsBABrU7FyhmNwMTDJYSoFINL//WGtt6xWNjZHx
kWU+WjDYK86cOfd+I5GCxOA4IUTayngrh56haHrUOH2NONuSnb3URDmG+Hy+HDDdYTiAcWz39u1b
zFOkUCjM5Gx+9UB2C0WjOWAe8C3aOwcnXZraUAx6z8yCE5bdmdmXrmh35dAzlF27dh0Hk9/IzkwZ
sewehXYbCIZ7QlKoJiwKxWTm9OnTFUR0ruBVNDao+JV2+EjXBS+a5FgPHelMPKaEz4SI8p1O56UX
vuriUQ49kyHjZXcGrTJTSjJ8Pp+VyDhVDcBp7u5+yTRBCoXCdIhoUO0JikbP1WwP98QmU1W44ULN
p6Oip3cgCFDEYudX+Fyejvtahh6iGC8YYitB/0gyGwnMraiqcu6rrR23bkU6WT4A4lIjO4F+uW/f
vin3ZVYophJENHfggJlI1+39S3JaIBBO/qq0CIHrA+/LL/vgdQXTLl2YbS0ssMjeqOw8ejRy8sXN
baeef7HDNC0AyO/vxiVz+4ID4/EsMBPOZgEQUVo6Z6oZegaTZ0ENAEOHSDSuy+4kIQ3LvDKjiyM9
T5spSKFQmA8RzRw4iMXtiS1SqbGpJ+mL0sDCv/5i8bJvfdOrZeeKmn/4asMr77/+3a3rv3gi3tOj
L/7qP3qWfuOfnENfZezQmpoHUo+ZmRA7l8bHzDOTv+riUA49g9m2bVsPMwzbpQo5fulri6qqVoLo
EiM7gZ5TTVgUikkPMfOsgSM9PijbRbS0mrZCp9mtInbmTLzmK//gb9+3r1cP98qOd9+N1H75H/2R
5uao+4YPFs1Y7ss2Sw+dHlwVj+S5z4aIDBtYXQzKoWc4xCmqxgHVq1evHpdtE2JK3YTFpv3MNDEK
hWJceOyxx6YlBsRRXB/k0Kml2TSH3hNqjvlf/f0ZvTssE8/LaJRb397ZDQCl76nOTf7qsUdrOzP4
vQ/+bPJ++tOfjnmBGbWHnuFENWyzMf4mmY0IuW1dXYsBmFq0ZbFv5WIi3Tiog/GKasKiUEx+wuFw
vsWS4EakHGgRSgCL9s6YWVqOPPlTw+I18fBZJ08mzmHbzsQICSk+uj7I30YikTwAY7qvr2boGc47
NTWHAG42svM47KMLoX/SyEaARBSPm6lHoVCMD4PS1QAk5p8jHmdwZmSs5pSV2QCg5e0604L0SEqG
rp9bLUj8bAD09PTkjfU9lUPPfJhhvOxOJtd19/l85ZL5WiM7g7fW19cM2TdZoVBMfM536IRzToti
MXnhK8zHVlioTV+6JK/z0KGepje3mRd1j8GfAWOwQ7fZbOensl00yqFPAISUqfLRL61YuXK6kX2s
iQvLJ4hSrFtJqVqkKhRTBGa2n3d87rchcXY6jlR8+e9Kwcy77/+3gNn35nj8XH/082bo5392Y4Fy
6BOA7nbLW2DWDcxkjcn3mKHj0hUrZjDzrUZ2Yqqvr6szbCqjUCgmFxaLZVBXSCKSCcZx9y8zP/yh
aa73vXfarg3f9nccPmJ6TQyyWAZS+DjxswHAzKk6ao6Kcf/AFUNz+PD2DoLYZ2Rnk7qvWYA1IOMm
LCz4p2boUCgU48+lK1bMeKu2drau69b+c4xzTout1nH1L87V1+Rd9vd/59rzn98LBv/4+riUn2Wb
7dwWBAY7dIvFMuZpvSrKfYIgibYRuDKZjYlXou/hLG1LXD6fLyem406jR0CWOLmnrmZLuu6vUChM
h5asXOlGLObRyeIV4DmQPAdEHoAdYFgOHTlqW1xRkZ+Tnd3S94oEp6VpAkQYj8A45zVX5y67/5ue
vd/7QfDUcy+MS3MYFoIgxLlfzPNm6EQ05vv5yqFPEAT0rQxal9RIKFxWXX3pzu3b96fr/jHSPpSq
CYsQ4qdI4wOFQqFID5WVlbnCbp8XhzZHk9IDAY+UmEMEL8d1G0hA9H+1BZDYaykajem6npBfLcTA
1iADkIUFVtHWblrqGgA4r74qd9m3N3j3/9cDjYnOvGD+fPu0BfPtp17cbEoJWC4qtA56lNG0eOJh
d3f3mK8aKIc+QdhdW3tgyfKqViZKGgCnx3kVgLQ49NWrV1tau8Ipm7DEw52b03FvhUJx8axevTrr
dEfvbNJ0D0nyMHiuEJjNTB4QCiQAATkQhz3cdO2eSK8ejSZsTVstg/qeyxkz7GY6dOdVV+Uu+9dv
eQ888L+NJ37z3KCZ+fTKRVllt9xUaJZDlzNmDNqeZIs28EExc/uXvvSlMdehHPrEQTKoBsAHkxmJ
aBWAR9Jx45aurg8QCYeRnZieVk1YFIrxZcOGDeLZV15xyXh8LkmaDYIHDC8E5rR2h4uFBgAECIBA
ffNsSn3N4dDZ1cUzpvfNM1hYoomX5BnTbTh89OJvMgxKr7wid9l37i+LdXbpxe+pzit+T/WgPO8c
h8PKUjdv/X/G9MEOPeGzIaIT6bilcugTCMHYJim5Q5eQiy6pri44vH37WD/1ESFFmVeJcHc7fjXG
91QoFAYsWbnS07+vrUnpYeI5gJjzm5deLgVgpbNOG8CYOOyhONPRIaSUQgghYdWiRMT9DVrY4chK
v4I+ym65aRpZLGQrKrSUXrEq6fZg57vvmpaHHi8tGagbT0RMVi1x0qMc+lQnZtO2aXGdkeRrSkSi
2GK54h82bXpXSjmTiGYKIQqYORdAPjPbAESIqAtAFzNHmbkBwPH8/PyTd911V9IHgUVVVSsBmmek
iYDnDh8e84cIhWJK4/P5ciJsnWkhOYeBORDwAOyRLLwc1/P797X7lsgHFRg1nfaOjogupU0I0Qsi
hkXrRSyeDQC62z3mxVOMqPs/Xw8AMD3XPBkMgD3n3jtbLT39rVMBgJnTUnxLOfQJxL5t21orl684
BMJ8ALDbbJrb6cpxOkpyXQ4HFxUV/QBAV39gJSdElxINfgYgooFz3d3d2Lhx42kAbwPYQUQ71q1b
dxIABNOnUjzlx9huUalqCsXooIqqKoeFuZyhlRNzuSTMEkBZDOwWQmqDo0wp0SdkCtHWljMHwVze
f4Kt9u5+hy5zsq1cUmyj5tNTakuOS0vtMitrwL+yxXb+ysCOdNxXOfQJRk5udu1Mj7d69qyZttLi
YmgWS4/VZmvWiIwKzwwLIioGcN3Zf9i4ceORxqam3a/+4Y8ru8LheLLXsOTf71FNWBSKVIglK1e6
EIt5GGIugNlgePtSv6QTII2pb4bNlDjXNmGtfLgw9RLJYwD5JegoII+yrvl7O9h/+PD2jn9++mmt
tbX1jwByAYDt1nBiQlZ8/rx8a/PplnFSPy7E5s3NTzymLFt3/6MYM3c2Nja+k477Koc+QfjRj360
QAjxCV3Xb2TmXqvVathZ6AJ0faADEoSQw3nMJ6K5jpKSBXfc9qGiYGPIcvjIke5jJ092yEGzfn5q
hG9DoZiU+Hy+4jjRnPP3tUFcynHdOihsvG93GZnktJlZEkQQkEeJ6aguhF/jeIPQs4/t3PmGYXMo
ALjzzjv1TZs2vQ3gKgCAzRYmIXQ+23kttmDeNOub26aUQ5cLFwzs4ZMQurRaexLMb2/YsCEtKb7K
oWc4GzduXE5En8bZJixnWxX2nD+O4nErotEcjut20uN2xHU7Eio4XTBeCJ0tWgSaJcIWLQKrrQc2
66BShEKIeG5OTvPc2bOozOMuWNza5ty7f3/PsRPHO+I6v7lnx46DY/x2FYqMxWhfm5k8sbM1GjJl
X9sABlMAzH4QGgAcI8gjsFr91mi0qa6udtTpZcz8BhH1OXQiZru9Az09RQDAhYV23e3K0gLBMS91
molIrydbFhQM1GmXdnvHeZOoP6fr3sqhZygPP/ywV9f1fzybjnYhzIRIJI96e/MRi+f0O+/hPvOz
lBqiMgeI5QykUgihs9USht3exXZ7JzRNB/oiNO12e7vH5WwvLp6Rt6S1orApdLpuz46ai36fCkUm
sWbNGu2d48dnAphDkjwgeBg0l8CzY4QCAYnz97UzaKINAGBGN0CHCXwEDD8L9rOu+WPdbQ0HDx7s
TMc9o9Hoa3a7/StAX2lozs5qp7MOHQDiy5YUaYFgMB33zjTily8tGnQiOysxHz6i6/of0nXvDPtT
VGzYsMHmcrnuBvBZABd244nGstDTUygikYL+Ja10QETMNmsXZ2efQVZW0opGUspXhBA/WLdu3el0
6VAo0sBASdML97XZAcr8iQ4zIoL4KEB+SPgJOBpncbR/X3s8NG3cuPE7RHRd/zGdbpmDeNwOAARw
1hNPHRWnWyZ1cJwsnmHrvfuTc7jft1osES6eMZCIz8y/Xb9+/b+k6/4Z/4c7lXjkkUdm6rr+HwAu
TBPr7c2jcHgGorEcIPVingj3xKijPUrtHTHE4pKiUUmxmJQAkd0mYM8SXJBv1acV2JGXZ+EkD3bM
TIhE8ykSzYfWFePsrFbk5rYlLh0JIa5n5uqHHnroG2vXrt06Bh+BQjFmVKxcOd0Si13Sv689UNJU
nCtpOsDAvnbmQIBkpgv2tWG1+hd4vY3PPPPMRQXCpoHf4WxQLQBwTnYLdXS6AYABivkun25/5feN
46bOBGIrls9I/D3l3JxBkx0hxG/TeX/l0DOEjRs3fjAej3+diAbnbUbjdurqcPY78vMhgEXz6V7h
94fFyVNhyyl/GJHIsAMu2GIh6Si16+XeXOn15ki3K4c1bXDhR123Ule3Az290zk/L4SsrIFlOyIq
ZOb/3rRp00+Kioo23nnnnZn2I6OYxKxcuTK7M8KzSNM9gJgjwHP697UR1wt4UL728EuamgqTf2Bf
u2+J/JiwWI5YotGmurq6pPvau83WOAwaGxv/4nQ6TxJRXwpbTk47dYeL+Wytd73i0kK5c3ebaGqK
pLzQBEV3ubL0SxdMGzihaVFkZw+sljDz0WAw+FY6Nagl93Fmw4YNwuVy/SOAOxLPs5RCdHaVUG9v
UX/VpUTozJmI5Z2D7da9B9qpoyNpWtmosNtFbOGCgvjCBdPY5cpONnuH3dbJ+fkhWCyDfmyY+e28
vLyvGBWpUShGw4YNG8SvX3ppFhL2tftLmgIoHmd5w0MiTIJPSIljBDrSv689nkvk6WDTpk03AfhW
/zGFw4Xo6HT1H2vNp3uyfvrz4+PRgS2tEKH37k/O1q4HnUgAABrcSURBVGdMH6iMxwX5QeTknBk4
Zv7a+vXrf59WGem8uCI1Tz/9tK2tre07AFYPMkSj2dTe4UkWpa4FG7utNXUt2pEjY95L93y4pNgW
W1ldHL9kTgFjcGUaImKZm9OEvLzWQa9hPkZEX1q3bt2UCIBRjBmpW3VOgH1tMKJEfKR/X1sXwm+B
frSrTRydTE47FRs2bLC4XK7nADgHTra0zKKzhWYAwLblz0Hr27vOJHn5hCXuu7wwcs2VAw8usFnD
PH36QHlXZm5obGz8cLrS1fpRDn2ceOKJJ3J7enq+B2B54nnq7CqmcLj4/Fk5tbZF7K//qVE7cdK0
WsT9yBnTbdErV5Xoc+dcWB85y94uCwoaSYjEP9RmXde/+IUvfMGcrgyKCUOqVp0g2Ia+wvgysK/N
7IegoxJ0tH9fe35m7mubzoMPPnizEGLDwIlo3C7aWmf3/6aRrsusX/76uGhsnBRL73GHIyv68TUz
+WyJTiJivWj6MbKd6zzHzN9Yv379y+nWohz6OPDYY49lRaPRHwJYknie2jucSEj1AACKx6W1tq7Z
sr22jaQc13Uqfe7s3Oh7r3Ek5lgCZ+sUFxae6k9zO0tTPB7/3Be/+MVJHQSjuJChWnWOt77hQIwW
Zhw5f1873tHRrDoLDglt3LhxExFdPnCivcOBnp6B1s+ioyOS9fhTxygWm9hr73ab6PnUJ2bLgoKB
h1HOyWlBQf5ABU1mfnv9+vXrYELUpXLoJvP0009rbW1t30V/VSUAYCY6c8aLSHRQuz+tubkn66Xf
+dHaZlo/4SGx20T0uvc7Y/MumZZ4mjQtKgunnYLVmtjz9xgR3bNu3br2Cy+kmMikatWJibKvDYQJ
fMKopOl4i5vI/PjHP54Ti8V+hrOB18xMoq2tPDG4Vzt+vDPr2RcbJup+OgtB0TUf9sY97nO/2zZr
WBYVnaRz2UBxq9X6ic997nOmrFYqh24ymzZt+icAtw+cMHDm1t17Wqyv/6l5vGflRsQrKwqiq69x
scVyLm5Y02JcVHgiMViOmfdMnz593Z133qlmNROQxFadg/a1iUsBGFYizBSYWYLpuBA4OlX3tceL
TZs2fR7AXw2ciMet1No2Gwn1M6wHDrbZfvvKhFvFYwDRm290xedfUjhwUog4z5h+DJqWGKT88Lp1
6zaZpSvzA00mERs3brwFCc6cmUmcOeNJdOYEZtsfXg9adu/N6FmtpX5fh2hsjkQ+clu5zD7bVUjX
raLtTLk+vegEnf2jJqLFbW1t/wfAt8dTr8KY4bbqBHC2z3bGPWOeK2l63r72dLs9tGXLlrHLAlEM
m6Kioofa2tqqAFQCACyWGBfkB0R7h7d/Pz22cEERpITt1dcaJ8xMnQjRD7zPkejMiYjltILAec58
Z1FR0SOmSjPzZlOZRx55ZGY8Hn8yMc/8/H0lYmbbb1/1W95JT3nGdKCXlNijH7mtTOZkD8zW2Grp
4aKik+cFyn193bp1r46DRAWAG264wX4q1DZnIu9rM6MLoCOJJU0BHJXhcIPa185MHnzwwVIi+hkR
nZvJ9vQUiI5Od2Lgr3byVKf9+c3+jN9Tt1lF7603u/XysoFuakTEsiA/kJhzDqBF07SP33PPPa1J
rpI2lEM3gbPlXB9HYgW47u4i6uwaSO0ggK2vvBaw7ts/4ZYB9ZISe2TN7TM5K2tgKY2z7B0oLPQP
HDOHdV3/5Be/+MVT46NySpC6VSdR2koFjxlDtOocb3mKkbNx48arieg/kbAiTJ1dxejuLkkcpwUb
u+0vvhygrq6MXFHhvDxL7603eqTTObjIV25uM+fnJVaEk7quf/kLX/jCG+YqVA7dFDZt2rQWwNqB
E9FYlmhrm5X4hGp9Y2ujrXbH8FuiZhi6x50V+chtMxP31Dk/rxG5uYnv6a1169b99TjIm1SkatWJ
CbqvPdxWnYqJydmCMxuQ6HPC4ULR2eVM/B0UPb1x2+9e8WvHTpienpsKfc6snOj1H/DI7OxzDyVE
LPPzGhOLxwAAM39n/fr1vzFfpXLoaeeHP/xhmaZpvySivi5EUgrR0jobZ8shAoBl74FW+6u/D42f
yrEhvvDS/MgN13kHThBJWTT9+Hn5mGmvljQZSNWqc4IskRu26kxV0lQxedm4ceNdRPR3g0729uZT
e4cbzAMTAQJY27O3zf7nN5tHUsY6LdjtInL1FSX64kVFg6pmEkmeVuBP0rhq47p160zdN09EOfQ0
89BDDz3AzOdaoHZ0llI4PKP/UDvd0mP/2S9PUDye2XtHwyRy3fud8UWXDeTSk9XaI2dMP54wpCk7
O3vN3XffnfZKd5lOqladE8Rpj0urTsXEZdOmTesA3DvopEFlTNHTG7du3dak7dnXYXq2DxHiSysL
YyurS2RW1uDgcU2L8bQCP2y2nsTTzPz4+vXr/8dUneehHHoaefDBB5cJIR4eOHHeUjtFo3rOz355
LKPyzC8StlgoctfHZ+nTiwxrGhPRj9auXfvj8VFoOin2tSdGSdNMbNWpmLg89NBDdzLzV3A2ZwLo
W7mkjg4X9UYueJAVnZ1RS21di6V+b3u6HTtbLKQvrpgWvXzpDJ427YLKhZxl7+CCguB5Ab+SiL6/
du3aX6RT23BQDj2NPPjggz8SQqzoP6bW1nJEY7n9x/Y//SVoqXt7UtU0BgDpdNp7P7Fm9kD9dyHi
XDzjCM5+CZi5g4huXrduXUbtk10MqVp1AhOopGmSVp2qpKlirHn44YevlVJ+G8CgqpMIhwupq7s0
MVe9H9HTG9fePdRu2bOvfaw7tuklJXZ98WXT9PnzCxIzds7dXMQ5L7c5yX55L4Bvrl+//g9jqWe0
KIeeJn74wx8utFgsT/YfUzSag9a2mf3HWtuZ3qyfPHlswuRejpDI9R9wxisWnitje14kKBH9YO3a
tU+Ni7hRkrJV5wRZIh9Nq06FIh1s3LhxHoD/IKKZgwy6rlFnVylFItOSdZoEANHa1qudaugWJ0+G
LScbRtQyGgCQk6PFy8ty9PKyHN3tyuXpRfZkw4iI2W5v5/y8pvNKWwPAUavV+lWzqsANB+XQ08TG
jRu/TUQ39B+fPzvPeu6FE9rR45Nmhno+nJWlhe/97CWwWvsaFgih68UzDtO5WXqosbHxlnR3Hxop
qlWnQmEemzZtygHwdQAfvMAYj1upOzwdvb2FiUFzyRA9vXFqPxOh020R6u3VKRaVFI1JJhDsdsF2
mwabTciiIhtPK7BxTo415VSKSCIr6wzn5rSe3yb6LJu7u7v/73333deTxDZuKIeeBh599NH8WCz2
Sn9kO6KxLGptnd1vF42N4eyfPX3C8AKThOjVVxXHli8byDXlvNxQYrtVZv6b9evXbxsHaapVp0KR
QWzatOk6Zr6PiC58aNZ1C3X3FCHSOy1ZS+kxRdNibM9qR25223lV3wAAzBwUQnx37dq1f0qrjlGS
+T9cExBd19874MwBUE9PYaLdtmNni/mqzMdW93ZbfOniGf256dQbKeQEh352BSNtDj1Vq06O67ZM
L2mqWnUqpgrr1q179YknnngzHA5/nojuRELAHDQtzgV5zUBeM0WjOejpLUA0mjdmzl3TYrDZujg7
qwM2m9GqaZyZnwqHw49k2qw8ETVDTwMbN258aKB1IDOJ5tPz+GyQh+joiGY98pMjU+WDj9x4vSt+
6YKBBxqePv0YbNZeoK96XDgcvv5iviCqVadCMbnYtGlTORF9hplvRKpJZyxmQzSaS7F4FqRuQ1y3
QcrUk1Qh4rBoUQgtylZLL2y27sQOkUmIMvPLRPTEunXrTo7uHZmHmqGPMQ888EABES0dOBGJ5HFC
xKb2zqH2qeLMAcBy4J32RIdOPT3T+KxDJ6Kc3NxcH4C/pLpGqladrd3hYqEBAAECIFDfPDvzPmTV
qlOhGAZnHef9jz766CPxePwzAG4AkH3BQKs1Cqs1mriuxlIKYhaQUoDPzvIJkoWQIJLnpZsZwszd
AF6MRqOPf+lLX5ow1QuVQx9jsrKylnFi1aPe3nNF/AG27MvsLmpjjTh2Iiy6u2MyN7dveez/t3ev
sXFc1x3Az7kzO7vcB3dJiSIpkZQEB7BkK3FV0ZLtyLETw3ASuUEcq0RbuG5R06BMGwSKNCnywY1Q
oGniRx5oHYiCBLsyCsQ2YjSJpfSD60RtGhmOlLSy06SBXiQlUpbE5Utc7s7jnn4Q9zGkWMvicna1
/P8AApqZ3eWdJcX/zp17z7XtBBGVVsXrpNlAX2ipztcPHlpFRCGeDW0iqsbAJhLxRHgAS3UCLN5j
jz02TERf6+/v/7bW+lNKqc/Slb8XCw6Qmw1sTYZ/1ts1/rnQIvI2ER2ybfsnfX19ZZ0aFwQEepmJ
SKdvR8nIdh5N59TYxLKaGsREpE6dntIf3XRlVTnPC5HjWPlurnR6fOdHO2/fyEwd4npN1X5fm4hI
hKeYZJCFB4VkgMkb1GQNWmQPHjt2rGZnLgBUwmy9ijeI6I3+/v6k1nozM3cy8xYi+ghd/8d7TURn
ROQYER3VWv+yt7f3hl1PgwiBXnbMvEXyc8sdx3dPxzw3vCzLnRoDQ9NuPtCJiB0nKrOBHg6H1kbC
4VjOtqtqgBeW6gSoPj09PRNE9NPZr/y0t478l9a6kZljRBQVkRgRETPbRJRh5sta6/PMPEBEg42N
jQNdXV019X8ZgV5Gr776qpFOp9fzbIE0chzfMntqIKAVhJhp1cfvirXcc3e8YdOmaKRpZYhNk7Oj
o87o0WPTJ196eTQzMhLYEoXmwGDGJpFC5TjbjuYrLinDcBpSqfD5CxeCv7LFUp0AN7TZq/ffzn4t
ewj0MhobG1vDzMWpFK7nK/mpzo0EMt0hVJ8wOp/9eoedTjvvPfvN86NHj2WUZXHrfZ9MbOx7qqX1
k/fW/8efd5+ZGR4Opvs/l9OUHrdpthoTe9rKd6QrZjuZSFhLFehYqhMAlgsEehmJyLrC1TkRsecW
Al3lci5nMoF2K7/3zPMj5w//e6Gb/8xr3x9PrF9ntT/0+RXrux5O/c+3/yGwQDMmxnNuvrxi6dKx
ppmrT9ZHF3zitVlwqc4QSpoCwDKBQC8jZm7z7fB0sbjMxGRg92qc6Yz+1dNfHbrw8yPzrnqnzgzY
RERWMjlv8YOlxGMTNs3WyhOtDfE8kw3DNQzDicfi19QWLNUJALAwBHp5JUo3WGuz0LU8ORncVaLr
ysibb12+2qHUhpsjRESj/3080GpHc8+fPW3mSyvWhcPZ/H4s1QkAcH0Q6GUkIrHSLvfSBQUkZ1d0
ERIrlTLW7vxCavWnH0iNvPlv40M/+FGw8+HnnX/xvVm5csVpYvqa5xqDdFPb4LuvvVZTI08BAIKA
QC+v4r1gES5d+o+dygR60+2ddVue/XqHCoeVOznp/vq550cGXv9B8MVtcln/+WtdCPREPD51/J13
3iIiol8G2ywAgFqBQC8jZo4UNkoCi4iIHK8igZ4+/m728J88eiq+ZrXZfM/diVu++JetzXdvT/zX
3/ztsD01FVib2POfPxNxScmYyNzHAwDAh/P/rjELH46IFLqKhdlf4ixkVOS99nI5mRkedi7+4ujM
e89968Lvvrv3/ZV33JHY9JUvtwTZDjFMXzUnKSkBJyI3XIlFAIBqg0AvI2YuTBFjpTSXhnrIqor3
+tT3XhkTz5OWe+9JhuKx4NoUnnP+/kUSUC4VAGCRqiJkaoWI+EaOl16FkhWqivdaPI+yFy86xEzx
deutD35Gmb5vKDRnahoXAr30gxAAAFyfqgiZGuKbKsZKFcqr6ng8sPEKN/3ZnzZu/dazaxY6bqVS
JhGRMzMd2D10SdT7z98ovjezSxUCAMAiINDLSETO+rZNo3hPPZUKB9UOMxLhxs2b45FVq+Z9iFh9
/31xIxJRuQsX7MsnTwc2PUw3lpw/s87PQb+yyeeCagcAQK1CoJeRUmrAv6Mk0Osipg6s211IhcNq
23e+2b5q+8djViKhIk0rzXUPP5Tc9OW/Wi2uK+8+89xIMG2ZlUwWa9wbhu+DxOzqRwAAsAiYtlZG
DQ0NQ2NjY5ryK3mbhp0f2i1EJGtWR+j00q+4duKll9PTQ+fs1fd/Kvmxr/x1ayhZb5II2em0c+Hn
R6ZOHHh5NMirczFN1g3FK/TSngsiIhFBoAMALBICvYy6urrsPXv2nGXmDiIiCoUzpbfVvfaOqBFA
oHu5nJw99OOps4d+XBX1zXX7mjoxSqbthUK+9yCXy50KvFEAADUGXe5lxsy/KmxYZo5KBsZ5ba2x
ijSqwnTHWt95SyhcCHQRGezr68MypgAAi4RALzNmPurbtopXo9LcXEfRaKCrnFUDd11HvLChlMuW
WSgkM/f9AgCA64NAL7NsNusLKG1ZhSlZwszOLRvqg29V5ehVq8J6RWOxtKsV8k1RE5FfBN4oAIAa
hEAvs76+vosiciK/LZHIJHGxiIq38eZkZVpWGe6mjf7zjUbHSw9rrXGFDgBQBgj0pXEo/w9WSlPY
KgxO85qa6rw1q5fFYiQSCrG3oeQDjGE4YlmlA+KO9Pb2jgXfMgCA2oNAXwKmab4hIl5+W+rqfMuV
OnduWxl8q4LnbtncoCOR4kyKcMT3PiilfhR4owAAahQCfQl0d3enmfmdwo5weFpCZqHOu+5oj+um
psAqx1WCmCY7t32ssbCDWUusLl04LjKVTCZ/VpHGAQDUIAT60nnFtxWLjeb/KURs37O9KfAWBcjd
trVRYtFidbhIZJwMo9Brwczf7+rqCqy4DQBArUOgL5Genp6ficjxwo5IZIrM4nQtr6M94d66MVGR
xi0xaVppuVu3FD6wMLNILFp6dZ4hopcr0jgAgBqFQF9CInLAt12fOF+6bW+/q5nC4Zr7Gdj3fqJZ
M+er3pJEo5fINJ2Sh/ywp6dn4ipPBQCA61RzYVJNnnjiicNE9JvCDsvKUCRSmLYlsVgo99kHWivR
tqVi397Z4La3FQvJmGZO4sXbDUR02XXdF4NvGQBAbUOgLy0homeIqDAPXSfiF0mpwr1kd/26evv2
zoZKNK7cvNWtEW/7nc2l+yQRf5+YJb/NzHueeuqp0fnPBgCAxUCgL7Genp53iehf8ttsGK4k689x
Sci52+9sdm9af0PXedepZCj3Bzva/F3tsUsUDpdWhvvf4eHhVyvQPACAmodAD0AsFvtHIipelYbD
01IXLY56Z2Z7x2fadNuaukq0b7EkGjWyD3++3Teq3QpNU328dNEV7XneN3bv3q3nvwIAACwWAj0A
jzzyyKTW+mkq6XqXROxSaV1zMU2V+9yONre5+YaqIifRqJHb+VC7JJPFefWG4UgyOex7nEh/b2/v
8XkvAAAAZbHsVv6qlIMHD5578MEHXWbeSkREzESRyCQ7dpQ8HSK6Eur61o1JNTaeU6Ppqp+jrVc0
Wtk/2rlOp1LFMFfKlYbUYOmodhE5vGvXrm9UpJEAAMsErtADdP78+X8iorcLO5hFksmzZBiF8BbD
UPaOT7c5m29LVaKN18prb6vL/eEXOiQeL3azM2tJJc9SKFQ8H5H3TdP8O7oyQBAAAJYIf/BDoJxe
fPHFiG3bLxDRbYWdnmfQ+Hg7O67vHro5MDhlHfzXEc5mvbmvUzHMZN+9faXbuXmllP7+KOVKKjVE
Viib3yUiacMw/uLxxx8/W5G2AgAsIwj0Cti3b1+j67r7mLkjv0+0Vmp8vI1sxzfaXY2P58Jv/mRE
DQ7NzH+lYOnGhpBz/30t7prV8dL9bBi2NKQGxd/NnmXmJ2ZH+QMAwBJDoFfI/v37V7uuu5eIWgo7
RZgnJlsom/V1tzMRmSdOTphvHb6gLl92A24qSSjEzh3bVrhbfm+FKKX8x8wZSibPzblnniWiL+3a
tetI0G0FAFiuEOgVtG/fvkbP875DRBt9B7LZhJqcahWtfYMWWUTMk6cmzf88cimIQXMSiRjOXdtW
uJtubRDT9AU5M4tEo5ckEb8052ljruv2Pfnkk78hAAAIDAK9wvbv359wHOd5Zv593wHHsXhqqmVu
FzwREXtazNOnJ41f/3bCOHVqmqS84830qlVhd9PGpLvh5pREIvNnQhiGLfWJ83OKxhARXTAMo6+7
u/tEWRsEAAAfCIFeBXbv3m22tLT0MfMf09yfSTab4KnLzeR5oas9V2VmHHXq9JQxOJQxB4cylMl8
6AF02gop3d5Wp9d2xLz29phe0Xj1ufDMWmLRSxSLpUvLuc562/O8p3t7e8c+7PcHAIDFQ6BXkb17
994jIl8lovp5B2dm6vnydBN5nrXQ85lIeGrKUROTNqXTtjE2kSM7pzlna/K0kGmwhEOKQmGl49GQ
NDRYkkpZujEVFuIFfxdYKU9H60YlGh1jpeZWetPMvGd4ePglVIEDAKgcBHqV6e/vbyWiLxHRJ+Yd
FGGamUmqmWxKHGfpy8QahkORyLhE68bIMOZd+TPz70Tk7zGSHQCg8hDoVeqFF164yzCMLzLz2qs+
wHEsnsklyc4lyHXDV33MdWDDcMSyLktdZJIsK3O1x4hIhpn3NDQ0vNLV1VU9c+QBAJYxBHoV6+/v
D4nITiJ6hJmbF3yg5xlk2zG2nTry3DB52lronruPUi6Zhk3KsMUKzVAolCmt8jaXiEwT0SvM/M89
PT0T13NOAACwNBDoN4DZQXOfoSvBftM1PUmE2fNM0WIQiSIRZmYRYk1MmpTyrtaNfvWXkkvM/Hou
l/teX1/f5GLOBQAAlgYC/QazZ8+eW5h5h4g8wMxLVu99ttLbT13XPXTx4sW3MeANAKC6IdBvULt3
7zabmpq2mqbZSUSdRLSBFrfYjhaRE0R0lIiORqPRY48++ujceeYAAFClEOg14sCBA7FMJvMRpdRa
rfVaImoVkRQzx4goyswWEU2KiBaRaaWUo7U+w8wDSqkhpdTJ7u7udIVPAwAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAACgFvwfRp5sZ/F47JIAAAAASUVORK5CYII=
"
>
</div>

</div>

<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>
Density is equal to 1.5

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[263]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[122]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre> 
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">
In&nbsp;[]:
</div>
<div class="inner_cell">
    <div class="input_area">
<div class="highlight"><pre> 
</pre></div>

</div>
</div>
</div>

</div>
    </div>
  </div>
</body>
</html>
