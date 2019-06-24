import json
from bs4 import BeautifulSoup

white_wines = """ "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Wine Recipes, Red wines Recipes, White Wines Recipes, Wineries, Fruity Wines</title>
<meta name="keywords" content="Chinese White Wine, Portuguese White Wine, Greek White Wine, Spanish White Wines, French White Wine, New Zealand White Wines, Italy White Wines" />
<meta name="description" content="Wine recipes page allows you to make recipes with the use of your favorite wines. Here you will see a list of wine recipes both added by us and submitted by our visitors"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<meta http-equiv="cache-control" content="public"/>
<meta name="revisit-after" content="1 days"/>
<meta name="copyright" content="www.all-about-wine.com"/>
<meta name="designer" content="www.aumkii.com"/>
<meta name="distribution" content="global"/>
<meta name="robots" content="index, follow"/>
<link href="/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
<link rel="icon" type="image/png" href="images/favicon.png"/>
<style>
.displayblock,.nav li a,.top-nav a{display:block}.by-color h4,.displayblock,.glossary,.quote,.sensory,.wine-gallery li,.wine-menu a,.wine-menu li,.wine-menu ul li,div.selectOptions,span.selected{overflow:hidden}*{margin:0;padding:0}li,ol,ul{list-style:none}h1,h2,h3,h4,h5,h6{font-weight:400}img{border:none}:focus{outline:0}a{text-decoration:none}.top-nav a.current_page,a:hover{text-decoration:underline}.clear{clear:both;height:0}.clearfix:after,.page-nav:after{content:" . ";display:block;height:0;clear:both;visibility:hidden;font-size:0;line-height:0}* html .clearfix{zoom:1}.floatleft{float:left}.floatright{float:right}.red{color:#b42903}.green{color:#427a2f}input,select,textarea{border:none;font-family:"Trebuchet MS",Verdana}h1{font-size:30px;line-height:30px}.discover,h2{font-size:22px}h3{font-size:20px}.font_13{font-size:14px}.font_13a{font-size:13px}.light-black{color:#666}.verdana_font{font-family:Verdana,Arial,Helvetica,sans-serif}body{background:#62622e;font-family:"Trebuchet MS",Verdana;font-size:15px;color:#333}.content-lbc,.content-lbc-white,.content-ltc,.content-ltc-white,.content-rbc,.content-rtc,.history,.history-hover,.home,.home-hover,.quality,.quality-hover,.temperature,.temperature-hover,.top-menu-blc,.top-menu-brc,.wine-accessories,.wine-accessories-hover,.wine-arrow,.wine-blc,.wine-bottle,.wine-bottle-hover,.wine-brc,.wine-glass,.wine-glass-hover,.wine-glossary,.wine-glossary-hover,.wine-grape,.wine-grape-hover,.wine-health,.wine-health-hover,.wine-info,.wine-info-hover,.wine-make,.wine-make-hover,.wine-menu-bc,.wine-menu-tc,.wine-selection,.wine-selection-hover,.wine-storage,.wine-storage-hover,.wine-tlc,.wine-trc,.wine-type-3,.wine-type-3-hover{background:url(../images/wine-sprite.png) no-repeat}#wrapper{margin:0 auto}#design-view{max-width:1057px;width:auto;margin:0 auto;background:url(../images/wine-banner.jpg) top center no-repeat #282c09;padding:0 24px}.wine-leaf{position:absolute;left:0}.wine-leaf-rht{position:absolute;right:0}.menu,.shop-soon,.top-menu{position:relative}.search-icon,.top-nav{float:left; margin-bottom:0px;} .social-icon {float:right; margin-bottom:0px;}.top-menu{border-top:none;background:#61692e;padding:0 8px 0px;float:none; overflow:hidden; height:auto; border-radius:0 0 10px 10px}.lft-content,.nav li,.top-menu li{float:left}.top-nav li.search_space{padding:4px 30px 0;width:220px}.top-nav a{font-size:12px; text-transform:uppercase; color:#fff;border-right:1px solid #656300;padding:10px 15px}.top-nav a.current_page,.top-nav a:hover{color:#ade036}.top-nav a.bor_non{border-right:none}.search{background:url(../images/search.png) no-repeat;height:18px;padding:3px 8px;width:165px}.social-icon li:last-child { border:none}.social-icon li{padding:10px 15px; border-right:solid 1px #737b42;}.logo{ margin-left:20px;}.logo-add{clear:both;padding:13px 0}.nav{background:url(../images/wine-menu-mid-4.jpg) bottom repeat-x #2d950a;border-radius:0 0 10px 10px;padding:0 8px}.nav li a{color:#fff;padding:14px 12px 14px;font-weight:700;font-size:14px;text-transform:uppercase}.nav li a:hover{color:#cde212;text-decoration:none}.nav li a.current_page{background:#a20101;color:#fff}.shop-soon img{position:absolute;right:-17px;top:-5px}.btn-new{position:relative}.btn-new img{position:absolute;right:-25px;top:-5px}.cart{position:absolute;top:3px;right:30px}.nav li a.cart:hover{background:0 0}.page-nav li{float:left;padding:5px;color:#fff}.page-nav a{color:#fff;font-size:12px}.page-nav a.page-active,.page-nav a:hover{color:#ade036}.content{padding-bottom:30px}.lft-content{max-width:811px;position:relative;background:#fff;border:2px solid #9a9a9a;min-height:300px;border-radius:10px;display:table}.lft-content div.floatleft{float:none}.rht-content{width:237px;position:relative}.sponser{margin-top:0;float:right}.wine-lft-menu{width:28%;min-height:100px;position:relative;padding:15px 0 15px 15px;background:#e5e3dd;border-radius:10px 10px 0;border-right:2px solid #9a9a9a;display:table-cell;vertical-align:top}.wine-arrow{background-position:0 -132px;height:19px;position:absolute;left:239px;top:50px;width:15px}.wine-menu{padding-top:15px}.sitemap{width:45%;float:left}.wine-menu li{margin:5px 0 10px}.wine-menu a{display:block;font-size:14px;color:#000;padding-left:55px}.sitemap a,.wine-article a{padding-left:0}.wine-menu ul li{padding-left:10px;margin:5px 0 8px}.wine-menu ul li a{font-size:13px;color:#666}.wine-menu a.current_page,.wine-menu a:hover{color:#427A2F;text-decoration:underline}.home,.home-hover{height:21px;background-position:0 -183px;padding-top:5px}.wine-menu a.home-hover,.wine-menu a.home:hover{background-position:0 -956px}.history,.history-hover,.quality,.quality-hover,.wine-make,.wine-make-hover,.wine-selection,.wine-selection-hover,.wine-type-3,.wine-type-3-hover{background-position:0 -228px;height:25px;padding-top:5px}.wine-menu a.history-hover,.wine-menu a.history:hover{background-position:0 -1001px}.wine-grape,.wine-grape-hover,.wine-health,.wine-health-hover{background-position:0 -278px;height:25px;padding-top:14px}.wine-menu a.wine-grape-hover,.wine-menu a.wine-grape:hover{background-position:1px -1051px}.wine-make{background-position:0 -337px}.wine-menu a.wine-make-hover,.wine-menu a.wine-make:hover{background-position:0 -1110px}.wine-type-3{background-position:0 -387px}.wine-menu a.wine-type-3-hover,.wine-menu a.wine-type-3:hover{background-position:0 -1160px}.quality{background-position:0 -438px}.wine-menu a.quality-hover,.wine-menu a.quality:hover{background-position:1px -1211px}.wine-storage,.wine-storage-hover{background-position:0 -489px;height:18px;padding-top:2px}.wine-menu a.wine-storage-hover,.wine-menu a.wine-storage:hover{background-position:0 -1262px}.temperature,.temperature-hover{background-position:0 -529px;height:40px;padding-top:9px}.wine-menu a.temperature-hover,.wine-menu a.temperature:hover{background-position:0 -1302px}.wine-bottle,.wine-bottle-hover,.wine-glass,.wine-glass-hover{background-position:0 -583px;height:27px;padding-top:11px}.wine-menu a.wine-bottle-hover,.wine-menu a.wine-bottle:hover{background-position:0 -1356px}.wine-glass{background-position:0 -640px}.wine-menu a.wine-glass-hover,.wine-menu a.wine-glass:hover{background-position:0 -1413px}.wine-selection{background-position:0 -700px}.wine-menu a.wine-selection-hover,.wine-menu a.wine-selection:hover{background-position:0 -1473px}.wine-accessories,.wine-accessories-hover{background-position:0 -750px;height:21px;padding-top:6px}.wine-menu a.wine-accessories-hover,.wine-menu a.wine-accessories:hover{background-position:1px -1523px}.wine-health{background-position:0 -797px}.wine-menu a.wine-health-hover,.wine-menu a.wine-health:hover{background-position:0 -1570px}.wine-glossary,.wine-glossary-hover{background-position:0 -855px;height:22px}.wine-menu a.wine-glossary-hover,.wine-menu a.wine-glossary:hover{background-position:1px -1628px}.wine-info,.wine-info-hover{background-position:0 -897px;height:18px}.wine-menu a.wine-info-hover,.wine-menu a.wine-info:hover{background-position:1px -1670px}.main-content{width:65%;color:#333;line-height:20px;padding:0 2% 20px;display:table-cell}.main-content img{max-width:100%}.quote{border-bottom:1px solid #dfdede;padding:15px 0; margin:0px;}h1{color:#427a2f}.quote em{text-align:right;letter-spacing:-1px;font:400 12px Verdana,Arial,Helvetica,sans-serif}.footer,.input-butn,.red_grape td{text-align:center}.quote span{width:350px;padding-left:25px}.wine-content{width:275px;padding-top:20px}.wine-content img{margin:15px 0 0}.wine-type{background:url(../images/wine-type-bg.gif) repeat-y;width:220px;margin-left:20px;padding:30px 0 0 20px}.wine-type ul{padding-bottom:25px}.wine-type li{background:url(../images/wine-type-menu-icon.gif) 0 16px no-repeat;padding:10px 0 0 18px;color:#333}.wine-type a:hover{color:#427A2F}.wine-month{padding:15px;background:#f9f8f8;overflow:hidden;margin-bottom:15px;position:relative}.wine-blc,.wine-brc,.wine-tlc,.wine-trc{position:absolute;width:8px;height:8px}.wine-tlc{background-position:0 -40px;top:0;left:0}.wine-trc{background-position:-18px -40px;top:0;right:0}.wine-blc{background-position:0 -58px;bottom:0;left:0}.wine-brc{background-position:-18px -58px;bottom:0;right:0}.wine-month h3{padding-bottom:20px}.month-content{width:130px;padding-left:15px;font:400 13px Verdana,Arial,Helvetica,sans-serif}.input-butn,.month-content b{padding:5px 0}.month-content h4{font-size:16px}.input-butn{border:2px solid #dbdad8;background:#fff;clear:both;color:#666;margin:15px 0 10px}.lft_img,.rht_img{border:1px solid #DFDEDE}.glossary,.red_grape td{border-bottom:1px solid #DFDEDE}.glass img,.sponser h1{padding-top:15px}.sponser h1{font:700 24px/18px Verdana,Arial,Helvetica,sans-serif}.wine-store{background:#f0f0f0;padding:5px;margin-bottom:8px}.top-space{padding-top:20px}.top-space-10{padding-top:10px}.content_list li{padding:5px 0;font-weight:700}.content_list p{padding:5px 0 10px;font-weight:400}.wine-recipes label{width:250px;padding-top:4px}.wine-recipes input,.wine-recipes textarea{border:1px solid #DFDEDE;padding:5px;font-size:13px;color:#666;width:50%}.wine-recipes em{float:right;color:red;font:400 13px "Trebuchet MS",Verdana;padding-right:5px}.wine-recipes li{list-style-type:disc;color:#666;margin:0 0 5px 15px}.wine-recipes li a{color:#b42903}.wine-recipes li a:hover{text-decoration:underline;color:#427a2f}.extra-line-ht{line-height:30px}.rht_img{margin:15px 0 15px 15px}.lft_img{margin:15px 15px 15px 0}.red_grape{border-right:1px solid #DFDEDE;margin-top:20px}.red_grape td{border-left:1px solid #DFDEDE;padding:10px}.wine-calories td{padding:5px}.row_1 td{border-top:1px solid #DFDEDE}.wine-link a{color:#b42903}.glossary{padding:15px 0}.glossary a{font-size:13px;color:#666}.glossary a.glos-active{font-size:13px;color:#b42903;text-decoration:underline}.captcha,.submit-query{margin-left:250px}.captcha input{margin-top:10px;width:269px}.captcha em{font:400 13px "Trebuchet MS",Verdana}.wine-gallery li{float:left;margin-bottom:15px}.wine-gallery li img{border:5px solid #9a9a9a}.wine-gallery li:nth-child(even){float:right}.footer{color:#fff;font-size:13px;padding-bottom:30px;clear:both}.footer li{display:inline}.footer a{color:#9aa82b;border-left:1px solid #586018;padding:0 15px}.footer a.bor-lft-non{border-left:none}.footer a:hover{color:#fff}.footer a.current_page{color:#fff;text-decoration:underline}.coming-soon{margin-top:200px}.highlight-search{background:#ff330f;color:#fff;font-weight:700}.wine-review-outer,span.selected{background:#fff}.page_title,.search_list_title{color:#427A2F}.top_space_10{margin-top:10px}.top_space_20{margin-top:20px}.prev_nav{float:left}.next_nav{float:right}.next_nav a,.prev_nav a{color:#B42903;text-decoration:none}.main-content-review{width:auto;margin-right:20px}.wine-review label{width:235px;display:block;font-weight:700}.wine-review input,.wine-review select,.wine-review textarea{border:1px solid #DFDEDE;padding:6px 9px;font-size:13px;width:751px;resize:none}.wine-review div.name-opt input{width:355px}.wine-recipes-form{clear:both;padding-top:20px}.wine-review input[type=reset]{float:right;margin-right:0}div.selectBox{position:relative;display:inline-block;text-align:left;line-height:30px;color:#666;float:left}span.selected{width:738px;border:1px solid #DFDEDE;border-right:none;text-indent:9px}span.selectArrow{width:30px;border:1px solid #DFDEDE;border-left:none;text-align:center;font-size:15px;cursor:pointer;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-o-user-select:none;user-select:none;background:url(../images/sele-arrow.gif) 7px 13px no-repeat}span.selectArrow,span.selected{position:relative;float:left;height:29px;z-index:1}div.selectOptions{position:absolute;top:29px;left:-232px;width:530px;border:1px solid #ccc;border-bottom-right-radius:5px;border-bottom-left-radius:5px;background:#f6f6f6;padding-top:2px;display:none;z-index:5}span.selectOption{display:block;float:left;line-height:26px}span.selectOption:hover{color:#f6f6f6;background:#4096ee}div.sel-wine-type{width:768px;left:0}div.sel-wine-type span.selectOption{left:0;float:none;padding:2px 9px}.submit-query input{width:137px;float:left;margin-right:5px;cursor:pointer}.wine-recipes-form input:focus,.wine-recipes-form textarea:focus{border:1px solid #d4d4d4;background:#f0f0f0}.sensory{background:#f0f0f0;border:1px solid #dfdede;padding:10px;position:relative;top:-1px}.sensory li{float:left;width:50%;padding-bottom:5px}.sensory input{width:auto;float:left;margin:5px 10px 0 0;border:none}.by-color{padding-bottom:20px}.by-color h4{border-bottom:1px solid #dfdede;padding-bottom:10px;margin-bottom:10px}.sensory #div_sensory_by_redwine li{width:33%}#div_sensory_by_color h4,#div_sensory_by_redwine h4,#div_sensory_by_whitewine h4{font-weight:700}#div_red_grapes li,#div_white_grapes li{float:left;width:32%;padding-bottom:5px}#red_grapes_others,#white_grapes_others{width:728px;border:1px solid #DFDEDE;margin-right:0}.chktxt{float:left;width:210px;padding-top:1px;text-transform:capitalize}#div_sensory_by_redwine .chktxt{width:125px}.review-captcha{margin-left:490px}.wine-region li{float:left;margin:20px 10px 0 0;text-align:center}.wine-region li:nth-child(2n){float:right;margin-right:0}.wine-region a{color:#666}.mob-ads{display:none}.mob-ads img{max-width:536px;width:100%;margin:0 auto;display:block;padding-top:15px}#dl-menu button,.mob-social-icon,.mob-topnav{display:none}@media only screen and (min-width:769px) and (max-width:999px){.nav li a{font-size:14px}.btn-new img{right:-32px}}@media only screen and (min-width:320px) and (max-width:568px){.btn-new img{right:-3px!important}.footer li{display:block;line-height:2;text-align:left}.footer a{border:none}}@media only screen and (min-width:320px) and (max-width:768px){.main-content,.wine-lft-menu{width:92%;padding:4%;display:block}.btn-new img{right:45px;top:-4px}#design-view{padding:0 4%}.logo img{max-width:100%}.nav li,.social-icon,.top-menu,.top-nav{float:none;text-align:center}.top-nav li a:last-child{border-right:none;}.social-icon,.top-nav{display:inline-block}.top-nav:after{content:" ";display:block;height:0;clear:both;visibility:hidden;font-size:0;line-height:0}.top-nav li.search_space{display:none}.lft-content{float:none;display:block}.wine-lft-menu{min-height:0;border-radius:10px 10px 0 0}.wine-arrow{display:none}.dl-menu{float:none;padding-top:0}#dl-menu button{display:block;background:#7ac142;border:none;text-indent:-9999px;width:41px;height:41px;position:relative;float:right;margin-top:-34px}#dl-menu button:after{background:#fff;box-shadow:0 10px 0 #fff,0 20px 0 #fff;content:"";height:3px;right:16%;position:absolute;top:9px;width:68%}#dl-menu .dl-menu{-webkit-transform:translateY(10px);-moz-transform:translateY(10px);transform:translateY(10px);display:none}#dl-menu .dl-menu.dl-menu-toggle{-webkit-transition:all .3s ease;-moz-transition:all .3s ease;transition:all .3s ease}#dl-menu .dl-menu.dl-menuopen{display:block;-webkit-transform:translateY(0);-moz-transform:translateY(0);transform:translateY(0);z-index:1}#dl-menu button:hover,#navigationFirstLevelMenu button.dl-active{background:#919191}#dl-menu ul{position:absolute;right:0;width:100%;background:#E5E3DD;top:55px}#dl-menu ul ul{position:relative;top:0}#dl-menu li{float:none;padding:5px 0;border-bottom:1px solid #a4a4a4}#dl-menu li ul li{border-bottom:none}#dl-menu a{display:block}.wine-menu li{margin:0}.captcha input,.wine-recipes input,.wine-recipes textarea{width:90%}.submit-query input{margin-bottom:15px}}@media only screen and (min-width:320px) and (max-width:837px){.captcha,.submit-query{margin-left:0}}@media (max-width:1099px){/*#sponser{display:none}*/.mob-ads{display:block}.lft-content{max-width:100%}.wine-arrow{display:none}}@media (max-width:640px){.mob-social-icon,.mob-topnav{display:block}.nav li a{height:50px;font-size:22px;padding:13px 0}.search-icon,.social-icon,.top-nav{display:none!important}li.mob-social-icon a{display:inline-block!important;overflow:hidden;height:auto}.mob-topnav{margin-top:15px}.top-menu{position:absolute;width:88%;z-index:10000}}
@media (max-width:767px) {
.mrgn-top-none {margin-top:20px !important;}
.topn-space-5 {margin-top:15px !important;}.quoteofWeek {margin-top:20px !important;}
/*.logo-add {float:left;}*/
.logo {max-width:200px;}
.form-search {display:none;}
.footer-social-icon {display:block !important; max-width:230px; margin:0 auto; padding-bottom: 15px; overflow:hidden}
.footer-social-icon li {float:left; padding:0 15px;}
.advertise-top {padding: 15px 0 15px;clear: both;}/*.wineType .col-xs-12 {margin-bottom:15px;}*/
/*.rht-ads {display:none;}*/
.right-sidebar {padding-left: 30px;}
}

h2 {font-size:18px; color:#666; text-transform:uppercase; font-weight:bold; margin-bottom:25px;}
hr {height: 1px; background-color:#CCCCCC; border:none;}
h4 {font-size:16px; color:#61692e; margin:16px 0;}
.topn-space-5 {margin-top:-7px;}

.main-content-new {width: 100%;color: #333;line-height: 20px; background-color: #fff; padding-left:20px; padding-right:20px; padding-bottom:20px; height:auto; overflow:hidden}
.main-content-new img{max-width:100%}
.quoteofWeek { background:url(../images/red-wine.jpg) no-repeat; width:100%; height:100%; max-height:220px;}
.clr-green {color:#9dc022;}
.box-quote {max-width:200px; margin:0 auto; padding:50px 0}
.box-quote h2 {margin-bottom:10px;}
.clr-white {color:#fff;}
.rht-ads {margin:20px 0;}
.link-readmore {color:#9aa81e;}
.wine-reviews {margin-bottom:25px;}
.wine-reviews img {max-width:100%;}
.wine-reviews h2 {margin-bottom:15px;}
.wine-reviews p {color:#d1d3bd; padding:15px 0;}
.wine-reviews a {color:#9aa81e; display:block; text-align:right;}

.footer-new {border-top:solid 1px #454c0e; border-bottom:solid 1px #454c0e; padding:25px 0; margin:20px 0; overflow:hidden; height:auto; clear:both}
.footer-new a {color:#84901d; font-size:13px;}
.bottom-fotter {color:#d1d3bd; padding-bottom:20px; text-align:center}
.bottom-fotter a {color:#84901d; font-size:13px; text-align:center; clear:left;}
.bottom-newslater {float:left; margin:0; padding:5px;}
.btn-submit {background-color:#2a860a; padding:5px; color:#fff}
.advertise-top {padding:0 0 15px;}
.search-query {max-width:190px; height:35px; background-color:#999e78; color:#dde2ba; padding:10px;}
.form-search {margin-top:10px; margin-right:20px;}
.footer-social-icon {display:none;}
#design-view-new {background: url(../images/wine-banner.jpg) top center no-repeat #282c09;}
.jsn1 {width:50% !important;}
.jsn2 {width:50% !important; left:130px;}
.jsn3 {width:40% !important; left:340px;}
.jsn4 {width:30% !important; left:480px;}
.jsn5 {width:30% !important; left:600px;}
.jsn6 {width:25% !important; left:700px;}
.mrgn-top-none {margin-top:0px;}
h1.glossary {margin:0px;}
.abc-txt {display:block;}
.bottom-20 {padding-bottom:20px;}
h1.light-black {padding-bottom:15px;}
.footer-new a:hover {color:#646e09; text-decoration:none}
.blog {background-color:#f0f0f0;}
.blog #design-view-new {
    background: url(/images/wine-banner.jpg) top center no-repeat #fff;}
.blog .page-nav a {color:#666;}
.blog .page-nav {padding-left:15px;}
.blog .footer-new {
    border-top: solid 1px #ccc;
    border-bottom: solid 1px #ccc;}
.category-txt {font-size:13px; font-weight:bold; color:#666;}
.clr-ornge {color:#ffa02f;}.clr-grn {color:#2a860a;} .clr-prl {color:#410a86;} .clr-brwn {color:#865f0a;} .clr-blu-grn {color:#0a866d;} .clr-cld-blu {color:#00c3e8;}
.clr-red {color:#ff0000;} .clr-dgrn {color:#999e78;}
.clr-ornge, .clr-grn, .clr-prl, .clr-brwn, .clr-blu-grn, .clr-cld-blu, .clr-red, .clr-dgrn {font-weight:bold;}
.category::before {
    content: "\2022";
    font-size: 28px;
    position: absolute;
    display: block;
    font-family: Arial, Helvetica, sans-serif;
    line-height: 0;
    top: 36px;
    left: 0;
}
.category {padding-left:17px;}
.category-main a {font-weight:bold}
.category-main h2 {font-size:24px; font-weight:bold; color:#333333; margin-bottom:15px !important;}
.category-main h2 a {color:#333 !important;}
.category-main {padding:25px 0 20px 0; border-bottom:solid 1px #e9e9e9; position:relative}
time {font-style:italic;}
.readmore {padding:10px 0 0 0; display:inline-block}
.widget-header { font-size:18px; color:#2a860a; text-transform:uppercase; padding-bottom:15px; font-weight:bold}
.right-widget ul {background-color:#fefefe; border:solid 1px #CCCCCC; padding:15px; margin-bottom:20px;}
.rpwwt-widget ul {background-color:#fff; border:none !important; padding:0; margin-bottom:20px;}

.right-widget li.cat-item {
    border-bottom: solid 1px #ccc; background:url(/images/arrow.png) no-repeat left center; padding:10px 15px}
.children li.cat-item {border-bottom: none !important; background:none !important;}
ul.children {border: none !important;}
.right-sidebar {padding-right:30px; padding-top: 20px; font-size:13px;}
.right-sidebar .screen-reader-text {display:none;}

.right-widget select{display: block;
width: 100%;
height: 34px;
padding: 6px 12px;
font-size: 14px;
line-height: 1.42857143;
color: #555;
background-color: #fff;
background-image: none;
border: 1px solid #ccc;}

.comment-respond {margin-top:10px; border-top: solid 1px #e9e9e9; padding-top:5px}
.comment-form label {display:block !important;}
.comment-form input[type=text] {width:100%; border:solid 1px #CCCCCC; padding:10px;}
.comment-form textarea {width:100%; border:solid 1px #CCCCCC; padding:10px;}
.comment-form .submit {background-color: #2a860a; color:#fff; padding:10px;}

</style>
<style type="text/css">
.mb-0 {
	margin-bottom:0px !important;
}

.mega-dropdown li.sub { margin-left:10px;}.mega-dropdown li.sub a::before { content: ">";font-size:14px;font-weight:bold;padding: 0 5px;
color:#FFCCCC}#menu {opacity:0;height:0px;width:0px;display:none;}

@media (max-width:798px) {.mobile .navbar-header {width:100%;}
 .mh-head {float:left;} #menu, .mh-head, .mobile {opacity:1;height:auto;width:auto;display:block;}#navnav, #navbar {display:none;}
 .mh-heads .hamburger-inner, .mh-heads .hamburger-inner:after, .mh-heads .hamburger-inner:before { background: red;}
}
.navbar-nav > li > .dropdown-menu {	margin-top:0px;
}.navbar-nav>li>.dropdown-menu {
	margin-top: 0px; border-top: 0px;}
.navbar-default .navbar-nav>li>a {width: 200px;font-weight: bold;}
.mega-dropdown{position: static !important;}
.mega-dropdown-menu {padding: 10px 0px;width: 100%;	box-shadow: none;	-webkit-box-shadow: none;}
.dropdown-menu{	border:none !important;}
.dropdown-menu .divider{	padding-bottom:0px !important;}
.mega-dropdown-menu > li > ul {	padding: 0;	margin: 0;}.mega-dropdown-menu > li > ul > li {	list-style: none;	border-bottom: solid 1px #efefef; padding:5px 0; float:none;}
.mega-dropdown-menu > li > ul > li > a {display: block;	padding: 3px 8px;	clear: both;	font-weight: normal;	line-height: 1.428571429;	color: #999;	white-space: normal;}.mega-dropdown-menu > li ul > li > a:hover, .mega-dropdown-menu > li ul > li > a:focus {
	text-decoration: none;	color: #444;}
.mega-dropdown-menu .dropdown-header {	color: #2a860a;	font-size: 18px;	font-weight: bold;}
.mega-dropdown-menu .dropdown-header a {	color: #2a860a; font-weight: bold;}
.mega-dropdown-menu form {	margin: 3px 20px;}
.mega-dropdown-menu .form-group {	margin-bottom: 3px;}
.dropdown.mega-dropdown:hover > .dropdown-menu.mega-dropdown-menu.row {	display: block;}
.navbar-default .navbar-nav>li>a {	color: #fff;}
navbar-default .navbar-nav>li>a:hover {	color: #000;	background: #fff;}
.megamenu-headline {	padding: 0 32px;}
</style>
</head>
<body class="">
<!--Wrapper start-->
<!--wine leaf left-->
<img src="/images/wine-leaf-lft.png" alt="wine-leaf" align="left" class="wine-leaf" />
<!--wine leaf right-->
<img src="/images/wine-leaf-rht.png" alt="wine-leaf" align="right" class="wine-leaf-rht" />
<div id="wrapper">
  <!--Design view start -->
  <div id="design-view-new" class="container">
    <!--Top menu start-->
        <div id="top-menu" class="top-menu">
      <ul class="top-nav">
        <li><a href="/wine-about-us.html" title="wine about us" class="">About Us</a></li>
        <li><a href="/wine-contact-us.php" title="wine contact us" class="">Contact Us</a></li>
        <li><a href="/wine-FAQ.html" title="Wine Frequently asked Questions" class="bor_non">FAQ</a></li>
        <li><a href="http://www.all-about-wine.com/aboutwines" title="Blog">Blog</a></li>
       <!-- <li class="search_space">
          <form id="searchform" action="search.php" method="get" >
  <input type="text" value="search" name="s" id="s" class="search floatleft" onclick="mouse_event('onclick');" onblur="mouse_event('onblur'); " />
  <input type="image" src="images/search-icon.jpg" class="search-icon floatright" id="searchsubmit" alt="" />
</form>
<script type="text/javascript">
function mouse_event(event_name){
	var search_key = $.trim($("#s").val());
	if(event_name == "onclick"){
		if(search_key=='search')
			$("#s").val('');
	}		 
	if(event_name == "onblur"){
		if(search_key=='')
			$("#s").val('search');
	} 
}
</script>        </li> -->
      </ul>
      <ul class="social-icon">
        <li><a href="https://www.facebook.com/allaboutwinesonline" title="all about wine facebook page" target="_blank" class="bor_non"><img src="/images/facebook-icon.png" alt="icon" class="hoverable" /></a></li>
        <li><a href="http://twitter.com/allaboutwinerie" title="all about wine tweets" target="_blank"><img src="/images/social-icon-twit.png" alt="twit" class="hoverable" /></a></li>
        <li><a href="https://plus.google.com/101390476745825259167" title="all about wine google plus" target="_blank"><img src="/images/google-plus.png" alt="google" class="hoverable" /></a></li>
        <li><a href="http://de.linkedin.com/in/allaboutwine" title="all about wine linkedin" target="_blank"><img src="/images/linkedin.png" alt="linkedin" class="hoverable" /></a></li>
      </ul>
    </div>
        <!--Top menu end-->
    <!--logo - add - start-->
    <div class="logo-add displayblock">
      <!-- Logo start-->
      <a href="/" class="logo floatleft"><img src="/images/wine-logo.png" alt="all about wine" /></a><form id="custom-search-form" method="GET" action="/search.html" class="form-search form-horizontal pull-right">
                  <div class="input-append span12">
                    <input class="search-query" placeholder="Search" name="q" type="text">
                    <button type="submit" class="btn"><img src="/images/search-icon.png" alt="search icon"></button>
                  </div>
                </form>
            <div class="mobile">
              </div>
      <!-- Logo end-->
      <!--Wine - addsense start-->
      <!--Wine - addsense end-->
    </div>
    <!--logo - add - end-->
    <!-- Menu - start -->
        
	<nav id="navnav" class="navbar navbar-inverse navbar-static-top">
        <div class="navbar-header">
          <button aria-controls="navbar" aria-expanded="false" data-target="#navbar" data-toggle="collapse" class="navbar-toggle collapsed" type="button"> <span class="sr-only">Toggle navigation</span><span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>
         </div>
        <div class="collapse navbar-collapse js-navbar-collapse" id="navbar">
          <ul class="nav navbar-nav">
            <li class="dropdown mega-dropdown"><a href="types-of-wine.html" class="dropdown-toggle" data-toggle="">Wine Types <b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn1">
                <li class="col-sm-4">
                  <ul>
                    <li><a href="types-of-red-wine.html">Red Wines</a></li>
                    <li><a href="types-of-white-wine.html">White Wines</a></li>
					<li><a href="rose-wines.html">Rose Wines</a></li>
					<li><a href="sparkling-wines.html">Sparkling Wines</a></li>
				  </ul>
                </li>
				<li class="col-sm-4">
                  <ul>
                    <li><a href="dessert-wine.html">Dessert Wines</a></li>
					<li><a href="fortified-wine.html">Fortifies Wines</a></li>
					<li><a href="table-wine.html">Table Wines</a></li>
				  </ul>
                </li>
                <li class="col-sm-4">
                  <ul>
                    <li><a href="red-wine-list.html">Red Wine List</a></li>
                    <li><a href="white-wine-list.html">White Wine List</a></li>
                  </ul>
                </li>
                
              </ul>
            </li>
            
            <li class="dropdown mega-dropdown"> <a href="#" class="dropdown-toggle " data-toggle="">Wine Bottles & Glasses <b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn2">
                <li class="col-sm-4">
                  <ul>
                    <li class="dropdown-header"><a href="wine-bottles.html">Wine Bottles</a></li>
                    <li><a href="types-of-wine-bottles.html">Types of Wine Bottles</a></li>
                  </ul>
                </li>
				<li class="col-sm-4">
                  <ul>
                    <li class="dropdown-header"><a href="wine-glasses.html">Wine Glasses</a></li>
                    <li><a href="white-wine-glass.html">White Wine Glasses</a></li>
					<li><a href="red-wine-glasses.html">Red Wine Glasses</a></li>
					<li><a href="sparkling-wine-glass.html">Sparkling Wine Glasses</a></li>
					<li><a href="dessert-wine-glass.html">Dessert Wine Glasses</a></li>
					<li><a href="other-types-glasses.html">Other Types of Wine Glasses</a></li>
			     </ul>
                </li>
				<li class="col-sm-4">
                  <ul>
                    <li class="dropdown-header"><a href="wine-accessories.html">Wine Accessories</a></li>
                    <li><a href="wine-coolers.html">Wine Coolers</a></li>
					<li><a href="wine-labels.html">Wine Labels</a></li>
					<li><a href="how-to-open-wine-bottle.html">Wine Openers</a></li>
					<li><a href="other-wine-accessories.html">Other Wine Accessories</a></li>
				 </ul>
                </li>
              </ul>
            </li>
			
			<li class="dropdown mega-dropdown"><a href="#" class="dropdown-toggle" data-toggle="">Wine Drinking <b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn3">
                <li class="col-sm-6">
                  <ul>
                    <li class="dropdown-header"><a href="wine-selection.html">Wine Selection</a></li>
					<li ><a href="wine-evaluation.html">Wine Evaluation</a></li>
					<li ><a href="wine-tasting-skill.html">Wine Tasting Skills</a></li>
					<li ><a href="wine-and-food-pairing.html">Wine Food Pairing</a></li>
					<li ><a href="wine-calories.html">Wine Calories</a></li>
                   </ul>
                </li>
                <li class="col-sm-6">
                  <ul>
                    <li class="dropdown-header"><a href="wine-serving-temperature.html">Wine Serving Temperature</a></li>
                    <li ><a href="red-wine-serving-temperature.html">Red Wine Serving Temperature</a></li>
                    <li ><a href="white-wine-serving-temperature.html">White Wine Serving Temperature</a></li>
					<li ><a href="sparkling-wine-serving-temperature.html">Sparkling Wine Serving Temperature</a></li>
					<li ><a href="fortified-wine-stroing-temperature.html">Dessert & Fortified Wine Serving Temperature</a></li>
                  </ul>
                </li>
			 </ul>
            </li>
			
			<li class="dropdown mega-dropdown"><a href="wine-grapes.html" class="dropdown-toggle" data-toggle="">Wine Grapes <b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn4">
                <li class="col-sm-6">
                  <ul>
                    <li><a href="popular-wine-making-grapes.html">Wine Making Grapes</a></li>
					<li ><a href="wine-grape-varieties.htm">Wine Grape Varieties</a></li>
				 </ul>
                </li>
                <li class="col-sm-6">
                  <ul>
                    <li><a href="red-grapes.html">Red Grapes</a></li>
                    <li ><a href="white-grapes.html">White Grapes</a></li>
                  </ul>
                </li>
			 </ul>
            </li>
           <li class="dropdown mega-dropdown"><a href="wine-making.html" class="dropdown-toggle" data-toggle="">Wine Making<b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn5">
                <li class="col-sm-6">
                  <ul>
                    <li><a href="wine-making-process.html">Wine Making Process</a></li>
					<li ><a href="wine-equipment.html">Wine Making Equiment</a></li>
					<li><a href="wine-color.html">Colours of Wine</a></li>
				  </ul>
                </li>
				 <li class="col-sm-6">
                  <ul>
                    <li ><a href="wine-producing-countries.html">Wine Producing Countries</a></li>
					<li><a href="wine-exporting-countries.html">Wine Exporting Countries</a></li>
				 </ul>
                </li>
              </ul>
            </li>
			<li class="dropdown mega-dropdown"><a href="wine-storage.html" class="dropdown-toggle" data-toggle="">Wine Storage<b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn6">
                <li class="col-sm-12">
                  <ul>
                    <li><a href="how-to-store-your-wine-optimal.html">How to store your wine</a></li>
					<li ><a href="conditions-that-affect-wine.html">Conditions that affect wine</a></li>
				 </ul>
                </li>
              </ul>
            </li>
			<li class="dropdown mega-dropdown"><a href="wine-sommelier.html" class="dropdown-toggle" data-toggle="">Wine Sommilier</a></li>
			<li class="dropdown mega-dropdown"><a href="wine-reviews.html" class="dropdown-toggle" data-toggle="">Wine Reviews</a></li>
          </ul>
        </div>
      </nav>
	
        <!-- Menu - end -->
    
    <!--page navigation start-->
	<!-- InstanceBeginEditable name="pagenav" -->
	<!-- page top ads start -->
		<div class="col-sm-12 advertise-top">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- AAW -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-9208166189076321"
     data-ad-slot="9483231912"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
<!-- page top ads end -->
  
    <!-- InstanceEndEditable -->
    <!--page navigation end-->
<!--Content start-->
<div class="row">
  <ul class="page-nav col-sm-12">
     <li><a href="http://www.all-about-wine.com" title="all about wine home">Home</a></li>
      <li> > </li>
      <li><a href="types-of-wine.html" title="types of wines">Types of Wine</a></li>
      <li> > </li>
      <li><a href="types-of-white-wine.html" title="types of white wine">Types of White Wine</a></li>
      <li> > </li>
      <li><a href="white-wine-list.html" class="page-active" title="list of white wines">White Wine List</a></li>
  </ul>
</div>
<div class="row clearfix">
  <!--Left Content start-->
  <div class="col-xs-12 col-sm-9">
    <div class="main-content-new font_13">
      <h1 class="verdana_font quote">White Wine List</h1>
      <p class="top-space">The most popluare white wine types are as follows:</p>
      <ul class="wine-recipes top-space">
        <li>Aligot&eacute;</li>
        <li>Alvarinho</li>
        <li>Auxerrois</li>
        <li>Bacchus</li>
        <li>Bual</li>
        <li>Chardonnay</li>
        <li>Chasselas</li>
        <li>Chenin Blanc</li>
        <li>Colombard</li>
        <li>Emerald Riesling</li>
        <li>Fum&eacute; Blanc</li>
        <li>Folle Blanche</li>
        <li>Furmint</li>
        <li>Gew&uuml;rztraminer</li>
        <li>Gr&uuml;ner Veltliner</li>
        <li>H&aacute;rslevel&uuml;</li>
        <li>Jacqu&egrave;re</li>
        <li>Kerner</li>
        <li>Malvasia</li>
        <li>Marsanne</li>
        <li>Morio-Muscat</li>
        <li>M&uuml;ller-Thurgau</li>
        <li>Muscadelle</li>
        <li>Muscadet</li>
        <li>Moscato</li>
        <li>Palomino</li>
        <li>Pedro Ximenez</li>
        <li>Picolit</li>
        <li>Pinot Blanc</li>
        <li>Pinot Gris</li>
        <li>Riesling</li>
        <li>Rkatsiteli</li>
        <li>Sacy</li>
        <li>Savagnin</li>
        <li>Sauvignon Blanc</li>
        <li>Scheurebe</li>
        <li>S&eacute;millon</li>
        <li>Sercial</li>
        <li>Seyval Blanc</li>
        <li>Silvaner</li>
        <li>Trebbiano</li>
        <li>Verdelho</li>
        <li>Verdicchio</li>
        <li>Vidal</li>
        <li>Viognier</li>
        <li>Viura</li>
        <li>Welschriesling</li>
      </ul>
    </div>
  </div>
  <!--Left Content end-->
  <!--Right Content start-->
  <div class="col-xs-12 col-sm-3" >
  <div class="wine-reviews">
    <h2 class="clr-white mrgn-top-none">Wine Recipes</h2>
    <div class="img-wine-reviews"><img src="/images/gl-wine-img.jpg" alt="Wine Reviews" class="img-responsive"/></div>
    <p class="font_13a">Wine recipes page allows you to make recipes with the use of your favorite wines. Here you will see a list of wine recipes both added by us and submitted by our visitors. Enjoy them all.</p>
    <a href="/wine-recipes.html" class="link-readmore font_13a">Read More</a> </div>
  <div class="rht-ads">
	<style>.ads-right{ max-width:265px; }
	
	</style>
	
	<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- AAW -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-9208166189076321"
     data-ad-slot="9483231912"
     data-ad-format="rectangle"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
	

  </div>
  <div class="wine-reviews">
    <h2 class="clr-white">Wine Reviews</h2>
    <div class="img-wine-reviews"><img src="/images/dessert-wine-glass.jpg" alt="Wine Reviews" class="img-responsive"/></div>
    <p class="font_13a">White wines are generally colorless and they are made from the white grape varieties.</p>
    <a href="/wine-reviews.html" class="link-readmore font_13a">Read More</a> </div>
  <div class="rht-ads">
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- AAW -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-9208166189076321"
     data-ad-slot="9483231912"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
  </div>
</div>
  <!--Right Content end-->
</div>
<!--Content end-->
 <!--Footer start-->
    <div class="footer-new">
      <div class="col-xs-6 col-sm-3 col-md-2"><ul>
	  <li><a href="http://www.all-about-wine.com" title="All About Wine">Home</a></li>
        <li><a href="/about-wine.html" title="wine" class="bor-lft-non">About Wine</a></li>
		<li><a href="/wine-contact-us.php" title="All About Wine">Contact Us</a></li>
		<li><a href="/wine-FAQ.html" title="FAQ">FAQ</a></li>
		<li><a href="http://www.all-about-wine.com/aboutwines" title="Blog">Blog</a></li>
		</ul>
	  </div>
	  <div class="col-xs-6 col-sm-3 col-md-2"><ul>
		<li><a href="/history-of-wine.html" title="History of Wine">History of Wine</a></li>
		<li><a href="/about-wine.html" title="About Wine">About Wine</a></li>
		<li><a href="/wine-and-your-health.html" title="Wine & Health">Wine & Health</a></li>
		<li><a href="/wine-misconceptions.html" title="Misconceptions about wine">Misconceptions about wine</a></li>
		<li><a href="/wine-recipes.html" title="Wine Recipes">Wine Recipes</a></li>
	  </ul>
	  </div>
	  <div class="col-xs-6 col-sm-3 col-md-2"><ul>
	    <li><a href="/wine-region.html" title="Wine Regions">Wine Regions</a></li>
		<li><a href="/wineries.html" title="Wineries">Wineries</a></li>
		<li><a href="/all-about-wine-glossary.html" title="Wine Glossary">Wine Glossary</a></li>
		<li><a href="/wine-quotes.html" title="Wine Quotes">Wine Quotes</a></li>
		<li><a href="/wine-gallery.html" title="Wine Gallery">Wine Gallery</a></li>
      </ul>
	  </div>
	  <div class="col-xs-6 col-sm-3 col-md-2"><ul>
        <li><a href="/wine-site-map.html" title="wine site map" class="">Site map</a></li>
        <li><a href="/imprint.html" title="wine imprint" class="">Imprint</a></li>
      </ul>
	  </div>
	  <!--
	  	<div class="col-xs-12 col-sm-12 col-md-4"><div class="navbar-form" role="search">
			<input type="text" placeholder="search text here" class="bottom-newslater" /><input type="submit" value="Submit"  class='btn-submit' />
		</div></div>
		-->
		
   </div>
    <!--Footer end-->
	<div class="bottom-fotter"> 
	<div class="col-sm-12 clearfix">
		 <ul class="footer-social-icon">
        <li><a href="https://www.facebook.com/allaboutwinesonline" title="all about wine facebook page" target="_blank" class="bor_non"><img src="/images/facebook-icon.png" alt="icon" /></a></li>
        <li><a href="http://twitter.com/allaboutwinerie" title="all about wine tweets" target="_blank"><img src="/images/social-icon-twit.png" alt="twit" /></a></li>
        <li><a href="https://plus.google.com/101390476745825259167" title="all about wine google plus" target="_blank"><img src="/images/google-plus.png" alt="google" /></a></li>
        <li><a href="http://de.linkedin.com/in/allaboutwine" title="all about wine linkedin" target="_blank"><img src="/images/linkedin.png" alt="linkedin" /></a></li>
      </ul>
	</div>
	<p>Copyright © 2017 all about wine.com - All rights reserved. <a href="http://www.aumkii.de/" target="_blank" class="bor-lft-non" title="web development and search engine optimization">Web development and SEO by aumkii</a></p>
	</div>
  </div>
  <!--Design view end-->
</div>
<!--Wrapper end-->
<script src="https://code.jquery.com/jquery-3.2.0.min.js" integrity="sha256-JAW99MJVpJBGcbzEuXk4Az05s/XyDdBomFqNlM3ic+I=" crossorigin="anonymous"></script>
<script>
	$(document).ready(function() {
			
		$("#navnav .dropdown").hover(
				function() { 
					$('.dropdown-menu', this).fadeIn("fast");
					if( $(this).hasClass("jsn") || $(this).hasClass("jsn2") || $(this).hasClass("jsn3") ){
						
						var nW="100%";
						
						var width = $('.dropdown-menu', this).width() ;
						
						
					}
				},
				function() { $('.dropdown-menu', this).fadeOut("fast");
		});
		
		
		
	});
</script>

<script>


	function isMobile(){
		if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
			// some code..
			return true;
		}else return false;
	}
</script>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-10140274-1");
pageTracker._trackPageview();
} catch(err) {}</script></body></html> """

red_wines = """ <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>List of red wines, Types of  Red Wines, White Wines, Wineries, Fruity Wines</title>
<meta name="keywords" content="Chinese White Wine, Portuguese White Wine, Greek White Wine, Spanish White Wines, French White Wine, New Zealand White Wines, Italy White Wines" />
<meta name="description" content="The fact that everyone knows is that red wines are produced from red or black grapes. But all the grapes have colorless juice. This fact is not known by anyone. But the red wine get its color by letting the sinks soak in the juice until the color releases out"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<meta http-equiv="cache-control" content="public"/>
<meta name="revisit-after" content="1 days"/>
<meta name="copyright" content="www.all-about-wine.com"/>
<meta name="designer" content="www.aumkii.com"/>
<meta name="distribution" content="global"/>
<meta name="robots" content="index, follow"/>
<link href="/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
<link rel="icon" type="image/png" href="images/favicon.png"/>
<style>
.displayblock,.nav li a,.top-nav a{display:block}.by-color h4,.displayblock,.glossary,.quote,.sensory,.wine-gallery li,.wine-menu a,.wine-menu li,.wine-menu ul li,div.selectOptions,span.selected{overflow:hidden}*{margin:0;padding:0}li,ol,ul{list-style:none}h1,h2,h3,h4,h5,h6{font-weight:400}img{border:none}:focus{outline:0}a{text-decoration:none}.top-nav a.current_page,a:hover{text-decoration:underline}.clear{clear:both;height:0}.clearfix:after,.page-nav:after{content:" . ";display:block;height:0;clear:both;visibility:hidden;font-size:0;line-height:0}* html .clearfix{zoom:1}.floatleft{float:left}.floatright{float:right}.red{color:#b42903}.green{color:#427a2f}input,select,textarea{border:none;font-family:"Trebuchet MS",Verdana}h1{font-size:30px;line-height:30px}.discover,h2{font-size:22px}h3{font-size:20px}.font_13{font-size:14px}.font_13a{font-size:13px}.light-black{color:#666}.verdana_font{font-family:Verdana,Arial,Helvetica,sans-serif}body{background:#62622e;font-family:"Trebuchet MS",Verdana;font-size:15px;color:#333}.content-lbc,.content-lbc-white,.content-ltc,.content-ltc-white,.content-rbc,.content-rtc,.history,.history-hover,.home,.home-hover,.quality,.quality-hover,.temperature,.temperature-hover,.top-menu-blc,.top-menu-brc,.wine-accessories,.wine-accessories-hover,.wine-arrow,.wine-blc,.wine-bottle,.wine-bottle-hover,.wine-brc,.wine-glass,.wine-glass-hover,.wine-glossary,.wine-glossary-hover,.wine-grape,.wine-grape-hover,.wine-health,.wine-health-hover,.wine-info,.wine-info-hover,.wine-make,.wine-make-hover,.wine-menu-bc,.wine-menu-tc,.wine-selection,.wine-selection-hover,.wine-storage,.wine-storage-hover,.wine-tlc,.wine-trc,.wine-type-3,.wine-type-3-hover{background:url(../images/wine-sprite.png) no-repeat}#wrapper{margin:0 auto}#design-view{max-width:1057px;width:auto;margin:0 auto;background:url(../images/wine-banner.jpg) top center no-repeat #282c09;padding:0 24px}.wine-leaf{position:absolute;left:0}.wine-leaf-rht{position:absolute;right:0}.menu,.shop-soon,.top-menu{position:relative}.search-icon,.top-nav{float:left; margin-bottom:0px;} .social-icon {float:right; margin-bottom:0px;}.top-menu{border-top:none;background:#61692e;padding:0 8px 0px;float:none; overflow:hidden; height:auto; border-radius:0 0 10px 10px}.lft-content,.nav li,.top-menu li{float:left}.top-nav li.search_space{padding:4px 30px 0;width:220px}.top-nav a{font-size:12px; text-transform:uppercase; color:#fff;border-right:1px solid #656300;padding:10px 15px}.top-nav a.current_page,.top-nav a:hover{color:#ade036}.top-nav a.bor_non{border-right:none}.search{background:url(../images/search.png) no-repeat;height:18px;padding:3px 8px;width:165px}.social-icon li:last-child { border:none}.social-icon li{padding:10px 15px; border-right:solid 1px #737b42;}.logo{ margin-left:20px;}.logo-add{clear:both;padding:13px 0}.nav{background:url(../images/wine-menu-mid-4.jpg) bottom repeat-x #2d950a;border-radius:0 0 10px 10px;padding:0 8px}.nav li a{color:#fff;padding:14px 12px 14px;font-weight:700;font-size:14px;text-transform:uppercase}.nav li a:hover{color:#cde212;text-decoration:none}.nav li a.current_page{background:#a20101;color:#fff}.shop-soon img{position:absolute;right:-17px;top:-5px}.btn-new{position:relative}.btn-new img{position:absolute;right:-25px;top:-5px}.cart{position:absolute;top:3px;right:30px}.nav li a.cart:hover{background:0 0}.page-nav li{float:left;padding:5px;color:#fff}.page-nav a{color:#fff;font-size:12px}.page-nav a.page-active,.page-nav a:hover{color:#ade036}.content{padding-bottom:30px}.lft-content{max-width:811px;position:relative;background:#fff;border:2px solid #9a9a9a;min-height:300px;border-radius:10px;display:table}.lft-content div.floatleft{float:none}.rht-content{width:237px;position:relative}.sponser{margin-top:0;float:right}.wine-lft-menu{width:28%;min-height:100px;position:relative;padding:15px 0 15px 15px;background:#e5e3dd;border-radius:10px 10px 0;border-right:2px solid #9a9a9a;display:table-cell;vertical-align:top}.wine-arrow{background-position:0 -132px;height:19px;position:absolute;left:239px;top:50px;width:15px}.wine-menu{padding-top:15px}.sitemap{width:45%;float:left}.wine-menu li{margin:5px 0 10px}.wine-menu a{display:block;font-size:14px;color:#000;padding-left:55px}.sitemap a,.wine-article a{padding-left:0}.wine-menu ul li{padding-left:10px;margin:5px 0 8px}.wine-menu ul li a{font-size:13px;color:#666}.wine-menu a.current_page,.wine-menu a:hover{color:#427A2F;text-decoration:underline}.home,.home-hover{height:21px;background-position:0 -183px;padding-top:5px}.wine-menu a.home-hover,.wine-menu a.home:hover{background-position:0 -956px}.history,.history-hover,.quality,.quality-hover,.wine-make,.wine-make-hover,.wine-selection,.wine-selection-hover,.wine-type-3,.wine-type-3-hover{background-position:0 -228px;height:25px;padding-top:5px}.wine-menu a.history-hover,.wine-menu a.history:hover{background-position:0 -1001px}.wine-grape,.wine-grape-hover,.wine-health,.wine-health-hover{background-position:0 -278px;height:25px;padding-top:14px}.wine-menu a.wine-grape-hover,.wine-menu a.wine-grape:hover{background-position:1px -1051px}.wine-make{background-position:0 -337px}.wine-menu a.wine-make-hover,.wine-menu a.wine-make:hover{background-position:0 -1110px}.wine-type-3{background-position:0 -387px}.wine-menu a.wine-type-3-hover,.wine-menu a.wine-type-3:hover{background-position:0 -1160px}.quality{background-position:0 -438px}.wine-menu a.quality-hover,.wine-menu a.quality:hover{background-position:1px -1211px}.wine-storage,.wine-storage-hover{background-position:0 -489px;height:18px;padding-top:2px}.wine-menu a.wine-storage-hover,.wine-menu a.wine-storage:hover{background-position:0 -1262px}.temperature,.temperature-hover{background-position:0 -529px;height:40px;padding-top:9px}.wine-menu a.temperature-hover,.wine-menu a.temperature:hover{background-position:0 -1302px}.wine-bottle,.wine-bottle-hover,.wine-glass,.wine-glass-hover{background-position:0 -583px;height:27px;padding-top:11px}.wine-menu a.wine-bottle-hover,.wine-menu a.wine-bottle:hover{background-position:0 -1356px}.wine-glass{background-position:0 -640px}.wine-menu a.wine-glass-hover,.wine-menu a.wine-glass:hover{background-position:0 -1413px}.wine-selection{background-position:0 -700px}.wine-menu a.wine-selection-hover,.wine-menu a.wine-selection:hover{background-position:0 -1473px}.wine-accessories,.wine-accessories-hover{background-position:0 -750px;height:21px;padding-top:6px}.wine-menu a.wine-accessories-hover,.wine-menu a.wine-accessories:hover{background-position:1px -1523px}.wine-health{background-position:0 -797px}.wine-menu a.wine-health-hover,.wine-menu a.wine-health:hover{background-position:0 -1570px}.wine-glossary,.wine-glossary-hover{background-position:0 -855px;height:22px}.wine-menu a.wine-glossary-hover,.wine-menu a.wine-glossary:hover{background-position:1px -1628px}.wine-info,.wine-info-hover{background-position:0 -897px;height:18px}.wine-menu a.wine-info-hover,.wine-menu a.wine-info:hover{background-position:1px -1670px}.main-content{width:65%;color:#333;line-height:20px;padding:0 2% 20px;display:table-cell}.main-content img{max-width:100%}.quote{border-bottom:1px solid #dfdede;padding:15px 0; margin:0px;}h1{color:#427a2f}.quote em{text-align:right;letter-spacing:-1px;font:400 12px Verdana,Arial,Helvetica,sans-serif}.footer,.input-butn,.red_grape td{text-align:center}.quote span{width:350px;padding-left:25px}.wine-content{width:275px;padding-top:20px}.wine-content img{margin:15px 0 0}.wine-type{background:url(../images/wine-type-bg.gif) repeat-y;width:220px;margin-left:20px;padding:30px 0 0 20px}.wine-type ul{padding-bottom:25px}.wine-type li{background:url(../images/wine-type-menu-icon.gif) 0 16px no-repeat;padding:10px 0 0 18px;color:#333}.wine-type a:hover{color:#427A2F}.wine-month{padding:15px;background:#f9f8f8;overflow:hidden;margin-bottom:15px;position:relative}.wine-blc,.wine-brc,.wine-tlc,.wine-trc{position:absolute;width:8px;height:8px}.wine-tlc{background-position:0 -40px;top:0;left:0}.wine-trc{background-position:-18px -40px;top:0;right:0}.wine-blc{background-position:0 -58px;bottom:0;left:0}.wine-brc{background-position:-18px -58px;bottom:0;right:0}.wine-month h3{padding-bottom:20px}.month-content{width:130px;padding-left:15px;font:400 13px Verdana,Arial,Helvetica,sans-serif}.input-butn,.month-content b{padding:5px 0}.month-content h4{font-size:16px}.input-butn{border:2px solid #dbdad8;background:#fff;clear:both;color:#666;margin:15px 0 10px}.lft_img,.rht_img{border:1px solid #DFDEDE}.glossary,.red_grape td{border-bottom:1px solid #DFDEDE}.glass img,.sponser h1{padding-top:15px}.sponser h1{font:700 24px/18px Verdana,Arial,Helvetica,sans-serif}.wine-store{background:#f0f0f0;padding:5px;margin-bottom:8px}.top-space{padding-top:20px}.top-space-10{padding-top:10px}.content_list li{padding:5px 0;font-weight:700}.content_list p{padding:5px 0 10px;font-weight:400}.wine-recipes label{width:250px;padding-top:4px}.wine-recipes input,.wine-recipes textarea{border:1px solid #DFDEDE;padding:5px;font-size:13px;color:#666;width:50%}.wine-recipes em{float:right;color:red;font:400 13px "Trebuchet MS",Verdana;padding-right:5px}.wine-recipes li{list-style-type:disc;color:#666;margin:0 0 5px 15px}.wine-recipes li a{color:#b42903}.wine-recipes li a:hover{text-decoration:underline;color:#427a2f}.extra-line-ht{line-height:30px}.rht_img{margin:15px 0 15px 15px}.lft_img{margin:15px 15px 15px 0}.red_grape{border-right:1px solid #DFDEDE;margin-top:20px}.red_grape td{border-left:1px solid #DFDEDE;padding:10px}.wine-calories td{padding:5px}.row_1 td{border-top:1px solid #DFDEDE}.wine-link a{color:#b42903}.glossary{padding:15px 0}.glossary a{font-size:13px;color:#666}.glossary a.glos-active{font-size:13px;color:#b42903;text-decoration:underline}.captcha,.submit-query{margin-left:250px}.captcha input{margin-top:10px;width:269px}.captcha em{font:400 13px "Trebuchet MS",Verdana}.wine-gallery li{float:left;margin-bottom:15px}.wine-gallery li img{border:5px solid #9a9a9a}.wine-gallery li:nth-child(even){float:right}.footer{color:#fff;font-size:13px;padding-bottom:30px;clear:both}.footer li{display:inline}.footer a{color:#9aa82b;border-left:1px solid #586018;padding:0 15px}.footer a.bor-lft-non{border-left:none}.footer a:hover{color:#fff}.footer a.current_page{color:#fff;text-decoration:underline}.coming-soon{margin-top:200px}.highlight-search{background:#ff330f;color:#fff;font-weight:700}.wine-review-outer,span.selected{background:#fff}.page_title,.search_list_title{color:#427A2F}.top_space_10{margin-top:10px}.top_space_20{margin-top:20px}.prev_nav{float:left}.next_nav{float:right}.next_nav a,.prev_nav a{color:#B42903;text-decoration:none}.main-content-review{width:auto;margin-right:20px}.wine-review label{width:235px;display:block;font-weight:700}.wine-review input,.wine-review select,.wine-review textarea{border:1px solid #DFDEDE;padding:6px 9px;font-size:13px;width:751px;resize:none}.wine-review div.name-opt input{width:355px}.wine-recipes-form{clear:both;padding-top:20px}.wine-review input[type=reset]{float:right;margin-right:0}div.selectBox{position:relative;display:inline-block;text-align:left;line-height:30px;color:#666;float:left}span.selected{width:738px;border:1px solid #DFDEDE;border-right:none;text-indent:9px}span.selectArrow{width:30px;border:1px solid #DFDEDE;border-left:none;text-align:center;font-size:15px;cursor:pointer;-webkit-user-select:none;-khtml-user-select:none;-moz-user-select:none;-o-user-select:none;user-select:none;background:url(../images/sele-arrow.gif) 7px 13px no-repeat}span.selectArrow,span.selected{position:relative;float:left;height:29px;z-index:1}div.selectOptions{position:absolute;top:29px;left:-232px;width:530px;border:1px solid #ccc;border-bottom-right-radius:5px;border-bottom-left-radius:5px;background:#f6f6f6;padding-top:2px;display:none;z-index:5}span.selectOption{display:block;float:left;line-height:26px}span.selectOption:hover{color:#f6f6f6;background:#4096ee}div.sel-wine-type{width:768px;left:0}div.sel-wine-type span.selectOption{left:0;float:none;padding:2px 9px}.submit-query input{width:137px;float:left;margin-right:5px;cursor:pointer}.wine-recipes-form input:focus,.wine-recipes-form textarea:focus{border:1px solid #d4d4d4;background:#f0f0f0}.sensory{background:#f0f0f0;border:1px solid #dfdede;padding:10px;position:relative;top:-1px}.sensory li{float:left;width:50%;padding-bottom:5px}.sensory input{width:auto;float:left;margin:5px 10px 0 0;border:none}.by-color{padding-bottom:20px}.by-color h4{border-bottom:1px solid #dfdede;padding-bottom:10px;margin-bottom:10px}.sensory #div_sensory_by_redwine li{width:33%}#div_sensory_by_color h4,#div_sensory_by_redwine h4,#div_sensory_by_whitewine h4{font-weight:700}#div_red_grapes li,#div_white_grapes li{float:left;width:32%;padding-bottom:5px}#red_grapes_others,#white_grapes_others{width:728px;border:1px solid #DFDEDE;margin-right:0}.chktxt{float:left;width:210px;padding-top:1px;text-transform:capitalize}#div_sensory_by_redwine .chktxt{width:125px}.review-captcha{margin-left:490px}.wine-region li{float:left;margin:20px 10px 0 0;text-align:center}.wine-region li:nth-child(2n){float:right;margin-right:0}.wine-region a{color:#666}.mob-ads{display:none}.mob-ads img{max-width:536px;width:100%;margin:0 auto;display:block;padding-top:15px}#dl-menu button,.mob-social-icon,.mob-topnav{display:none}@media only screen and (min-width:769px) and (max-width:999px){.nav li a{font-size:14px}.btn-new img{right:-32px}}@media only screen and (min-width:320px) and (max-width:568px){.btn-new img{right:-3px!important}.footer li{display:block;line-height:2;text-align:left}.footer a{border:none}}@media only screen and (min-width:320px) and (max-width:768px){.main-content,.wine-lft-menu{width:92%;padding:4%;display:block}.btn-new img{right:45px;top:-4px}#design-view{padding:0 4%}.logo img{max-width:100%}.nav li,.social-icon,.top-menu,.top-nav{float:none;text-align:center}.top-nav li a:last-child{border-right:none;}.social-icon,.top-nav{display:inline-block}.top-nav:after{content:" ";display:block;height:0;clear:both;visibility:hidden;font-size:0;line-height:0}.top-nav li.search_space{display:none}.lft-content{float:none;display:block}.wine-lft-menu{min-height:0;border-radius:10px 10px 0 0}.wine-arrow{display:none}.dl-menu{float:none;padding-top:0}#dl-menu button{display:block;background:#7ac142;border:none;text-indent:-9999px;width:41px;height:41px;position:relative;float:right;margin-top:-34px}#dl-menu button:after{background:#fff;box-shadow:0 10px 0 #fff,0 20px 0 #fff;content:"";height:3px;right:16%;position:absolute;top:9px;width:68%}#dl-menu .dl-menu{-webkit-transform:translateY(10px);-moz-transform:translateY(10px);transform:translateY(10px);display:none}#dl-menu .dl-menu.dl-menu-toggle{-webkit-transition:all .3s ease;-moz-transition:all .3s ease;transition:all .3s ease}#dl-menu .dl-menu.dl-menuopen{display:block;-webkit-transform:translateY(0);-moz-transform:translateY(0);transform:translateY(0);z-index:1}#dl-menu button:hover,#navigationFirstLevelMenu button.dl-active{background:#919191}#dl-menu ul{position:absolute;right:0;width:100%;background:#E5E3DD;top:55px}#dl-menu ul ul{position:relative;top:0}#dl-menu li{float:none;padding:5px 0;border-bottom:1px solid #a4a4a4}#dl-menu li ul li{border-bottom:none}#dl-menu a{display:block}.wine-menu li{margin:0}.captcha input,.wine-recipes input,.wine-recipes textarea{width:90%}.submit-query input{margin-bottom:15px}}@media only screen and (min-width:320px) and (max-width:837px){.captcha,.submit-query{margin-left:0}}@media (max-width:1099px){/*#sponser{display:none}*/.mob-ads{display:block}.lft-content{max-width:100%}.wine-arrow{display:none}}@media (max-width:640px){.mob-social-icon,.mob-topnav{display:block}.nav li a{height:50px;font-size:22px;padding:13px 0}.search-icon,.social-icon,.top-nav{display:none!important}li.mob-social-icon a{display:inline-block!important;overflow:hidden;height:auto}.mob-topnav{margin-top:15px}.top-menu{position:absolute;width:88%;z-index:10000}}
@media (max-width:767px) {
.mrgn-top-none {margin-top:20px !important;}
.topn-space-5 {margin-top:15px !important;}.quoteofWeek {margin-top:20px !important;}
/*.logo-add {float:left;}*/
.logo {max-width:200px;}
.form-search {display:none;}
.footer-social-icon {display:block !important; max-width:230px; margin:0 auto; padding-bottom: 15px; overflow:hidden}
.footer-social-icon li {float:left; padding:0 15px;}
.advertise-top {padding: 15px 0 15px;clear: both;}/*.wineType .col-xs-12 {margin-bottom:15px;}*/
/*.rht-ads {display:none;}*/
.right-sidebar {padding-left: 30px;}
}

h2 {font-size:18px; color:#666; text-transform:uppercase; font-weight:bold; margin-bottom:25px;}
hr {height: 1px; background-color:#CCCCCC; border:none;}
h4 {font-size:16px; color:#61692e; margin:16px 0;}
.topn-space-5 {margin-top:-7px;}

.main-content-new {width: 100%;color: #333;line-height: 20px; background-color: #fff; padding-left:20px; padding-right:20px; padding-bottom:20px; height:auto; overflow:hidden}
.main-content-new img{max-width:100%}
.quoteofWeek { background:url(../images/red-wine.jpg) no-repeat; width:100%; height:100%; max-height:220px;}
.clr-green {color:#9dc022;}
.box-quote {max-width:200px; margin:0 auto; padding:50px 0}
.box-quote h2 {margin-bottom:10px;}
.clr-white {color:#fff;}
.rht-ads {margin:20px 0;}
.link-readmore {color:#9aa81e;}
.wine-reviews {margin-bottom:25px;}
.wine-reviews img {max-width:100%;}
.wine-reviews h2 {margin-bottom:15px;}
.wine-reviews p {color:#d1d3bd; padding:15px 0;}
.wine-reviews a {color:#9aa81e; display:block; text-align:right;}

.footer-new {border-top:solid 1px #454c0e; border-bottom:solid 1px #454c0e; padding:25px 0; margin:20px 0; overflow:hidden; height:auto; clear:both}
.footer-new a {color:#84901d; font-size:13px;}
.bottom-fotter {color:#d1d3bd; padding-bottom:20px; text-align:center}
.bottom-fotter a {color:#84901d; font-size:13px; text-align:center; clear:left;}
.bottom-newslater {float:left; margin:0; padding:5px;}
.btn-submit {background-color:#2a860a; padding:5px; color:#fff}
.advertise-top {padding:0 0 15px;}
.search-query {max-width:190px; height:35px; background-color:#999e78; color:#dde2ba; padding:10px;}
.form-search {margin-top:10px; margin-right:20px;}
.footer-social-icon {display:none;}
#design-view-new {background: url(../images/wine-banner.jpg) top center no-repeat #282c09;}
.jsn1 {width:50% !important;}
.jsn2 {width:50% !important; left:130px;}
.jsn3 {width:40% !important; left:340px;}
.jsn4 {width:30% !important; left:480px;}
.jsn5 {width:30% !important; left:600px;}
.jsn6 {width:25% !important; left:700px;}
.mrgn-top-none {margin-top:0px;}
h1.glossary {margin:0px;}
.abc-txt {display:block;}
.bottom-20 {padding-bottom:20px;}
h1.light-black {padding-bottom:15px;}
.footer-new a:hover {color:#646e09; text-decoration:none}
.blog {background-color:#f0f0f0;}
.blog #design-view-new {
    background: url(/images/wine-banner.jpg) top center no-repeat #fff;}
.blog .page-nav a {color:#666;}
.blog .page-nav {padding-left:15px;}
.blog .footer-new {
    border-top: solid 1px #ccc;
    border-bottom: solid 1px #ccc;}
.category-txt {font-size:13px; font-weight:bold; color:#666;}
.clr-ornge {color:#ffa02f;}.clr-grn {color:#2a860a;} .clr-prl {color:#410a86;} .clr-brwn {color:#865f0a;} .clr-blu-grn {color:#0a866d;} .clr-cld-blu {color:#00c3e8;}
.clr-red {color:#ff0000;} .clr-dgrn {color:#999e78;}
.clr-ornge, .clr-grn, .clr-prl, .clr-brwn, .clr-blu-grn, .clr-cld-blu, .clr-red, .clr-dgrn {font-weight:bold;}
.category::before {
    content: "\2022";
    font-size: 28px;
    position: absolute;
    display: block;
    font-family: Arial, Helvetica, sans-serif;
    line-height: 0;
    top: 36px;
    left: 0;
}
.category {padding-left:17px;}
.category-main a {font-weight:bold}
.category-main h2 {font-size:24px; font-weight:bold; color:#333333; margin-bottom:15px !important;}
.category-main h2 a {color:#333 !important;}
.category-main {padding:25px 0 20px 0; border-bottom:solid 1px #e9e9e9; position:relative}
time {font-style:italic;}
.readmore {padding:10px 0 0 0; display:inline-block}
.widget-header { font-size:18px; color:#2a860a; text-transform:uppercase; padding-bottom:15px; font-weight:bold}
.right-widget ul {background-color:#fefefe; border:solid 1px #CCCCCC; padding:15px; margin-bottom:20px;}
.rpwwt-widget ul {background-color:#fff; border:none !important; padding:0; margin-bottom:20px;}

.right-widget li.cat-item {
    border-bottom: solid 1px #ccc; background:url(/images/arrow.png) no-repeat left center; padding:10px 15px}
.children li.cat-item {border-bottom: none !important; background:none !important;}
ul.children {border: none !important;}
.right-sidebar {padding-right:30px; padding-top: 20px; font-size:13px;}
.right-sidebar .screen-reader-text {display:none;}

.right-widget select{display: block;
width: 100%;
height: 34px;
padding: 6px 12px;
font-size: 14px;
line-height: 1.42857143;
color: #555;
background-color: #fff;
background-image: none;
border: 1px solid #ccc;}

.comment-respond {margin-top:10px; border-top: solid 1px #e9e9e9; padding-top:5px}
.comment-form label {display:block !important;}
.comment-form input[type=text] {width:100%; border:solid 1px #CCCCCC; padding:10px;}
.comment-form textarea {width:100%; border:solid 1px #CCCCCC; padding:10px;}
.comment-form .submit {background-color: #2a860a; color:#fff; padding:10px;}

</style>
<style type="text/css">
.mb-0 {
	margin-bottom:0px !important;
}

.mega-dropdown li.sub { margin-left:10px;}.mega-dropdown li.sub a::before { content: ">";font-size:14px;font-weight:bold;padding: 0 5px;
color:#FFCCCC}#menu {opacity:0;height:0px;width:0px;display:none;}

@media (max-width:798px) {.mobile .navbar-header {width:100%;}
 .mh-head {float:left;} #menu, .mh-head, .mobile {opacity:1;height:auto;width:auto;display:block;}#navnav, #navbar {display:none;}
 .mh-heads .hamburger-inner, .mh-heads .hamburger-inner:after, .mh-heads .hamburger-inner:before { background: red;}
}
.navbar-nav > li > .dropdown-menu {	margin-top:0px;
}.navbar-nav>li>.dropdown-menu {
	margin-top: 0px; border-top: 0px;}
.navbar-default .navbar-nav>li>a {width: 200px;font-weight: bold;}
.mega-dropdown{position: static !important;}
.mega-dropdown-menu {padding: 10px 0px;width: 100%;	box-shadow: none;	-webkit-box-shadow: none;}
.dropdown-menu{	border:none !important;}
.dropdown-menu .divider{	padding-bottom:0px !important;}
.mega-dropdown-menu > li > ul {	padding: 0;	margin: 0;}.mega-dropdown-menu > li > ul > li {	list-style: none;	border-bottom: solid 1px #efefef; padding:5px 0; float:none;}
.mega-dropdown-menu > li > ul > li > a {display: block;	padding: 3px 8px;	clear: both;	font-weight: normal;	line-height: 1.428571429;	color: #999;	white-space: normal;}.mega-dropdown-menu > li ul > li > a:hover, .mega-dropdown-menu > li ul > li > a:focus {
	text-decoration: none;	color: #444;}
.mega-dropdown-menu .dropdown-header {	color: #2a860a;	font-size: 18px;	font-weight: bold;}
.mega-dropdown-menu .dropdown-header a {	color: #2a860a; font-weight: bold;}
.mega-dropdown-menu form {	margin: 3px 20px;}
.mega-dropdown-menu .form-group {	margin-bottom: 3px;}
.dropdown.mega-dropdown:hover > .dropdown-menu.mega-dropdown-menu.row {	display: block;}
.navbar-default .navbar-nav>li>a {	color: #fff;}
navbar-default .navbar-nav>li>a:hover {	color: #000;	background: #fff;}
.megamenu-headline {	padding: 0 32px;}
</style>
</head>
<body class="">
<!--Wrapper start-->
<!--wine leaf left-->
<img src="/images/wine-leaf-lft.png" alt="wine-leaf" align="left" class="wine-leaf" />
<!--wine leaf right-->
<img src="/images/wine-leaf-rht.png" alt="wine-leaf" align="right" class="wine-leaf-rht" />
<div id="wrapper">
  <!--Design view start -->
  <div id="design-view-new" class="container">
    <!--Top menu start-->
        <div id="top-menu" class="top-menu">
      <ul class="top-nav">
        <li><a href="/wine-about-us.html" title="wine about us" class="">About Us</a></li>
        <li><a href="/wine-contact-us.php" title="wine contact us" class="">Contact Us</a></li>
        <li><a href="/wine-FAQ.html" title="Wine Frequently asked Questions" class="bor_non">FAQ</a></li>
        <li><a href="http://www.all-about-wine.com/aboutwines" title="Blog">Blog</a></li>
       <!-- <li class="search_space">
          <form id="searchform" action="search.php" method="get" >
  <input type="text" value="search" name="s" id="s" class="search floatleft" onclick="mouse_event('onclick');" onblur="mouse_event('onblur'); " />
  <input type="image" src="images/search-icon.jpg" class="search-icon floatright" id="searchsubmit" alt="" />
</form>
<script type="text/javascript">
function mouse_event(event_name){
	var search_key = $.trim($("#s").val());
	if(event_name == "onclick"){
		if(search_key=='search')
			$("#s").val('');
	}		 
	if(event_name == "onblur"){
		if(search_key=='')
			$("#s").val('search');
	} 
}
</script>        </li> -->
      </ul>
      <ul class="social-icon">
        <li><a href="https://www.facebook.com/allaboutwinesonline" title="all about wine facebook page" target="_blank" class="bor_non"><img src="/images/facebook-icon.png" alt="icon" class="hoverable" /></a></li>
        <li><a href="http://twitter.com/allaboutwinerie" title="all about wine tweets" target="_blank"><img src="/images/social-icon-twit.png" alt="twit" class="hoverable" /></a></li>
        <li><a href="https://plus.google.com/101390476745825259167" title="all about wine google plus" target="_blank"><img src="/images/google-plus.png" alt="google" class="hoverable" /></a></li>
        <li><a href="http://de.linkedin.com/in/allaboutwine" title="all about wine linkedin" target="_blank"><img src="/images/linkedin.png" alt="linkedin" class="hoverable" /></a></li>
      </ul>
    </div>
        <!--Top menu end-->
    <!--logo - add - start-->
    <div class="logo-add displayblock">
      <!-- Logo start-->
      <a href="/" class="logo floatleft"><img src="/images/wine-logo.png" alt="all about wine" /></a><form id="custom-search-form" method="GET" action="/search.html" class="form-search form-horizontal pull-right">
                  <div class="input-append span12">
                    <input class="search-query" placeholder="Search" name="q" type="text">
                    <button type="submit" class="btn"><img src="/images/search-icon.png" alt="search icon"></button>
                  </div>
                </form>
            <div class="mobile">
              </div>
      <!-- Logo end-->
      <!--Wine - addsense start-->
      <!--Wine - addsense end-->
    </div>
    <!--logo - add - end-->
    <!-- Menu - start -->
        
	<nav id="navnav" class="navbar navbar-inverse navbar-static-top">
        <div class="navbar-header">
          <button aria-controls="navbar" aria-expanded="false" data-target="#navbar" data-toggle="collapse" class="navbar-toggle collapsed" type="button"> <span class="sr-only">Toggle navigation</span><span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>
         </div>
        <div class="collapse navbar-collapse js-navbar-collapse" id="navbar">
          <ul class="nav navbar-nav">
            <li class="dropdown mega-dropdown"><a href="types-of-wine.html" class="dropdown-toggle" data-toggle="">Wine Types <b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn1">
                <li class="col-sm-4">
                  <ul>
                    <li><a href="types-of-red-wine.html">Red Wines</a></li>
                    <li><a href="types-of-white-wine.html">White Wines</a></li>
					<li><a href="rose-wines.html">Rose Wines</a></li>
					<li><a href="sparkling-wines.html">Sparkling Wines</a></li>
				  </ul>
                </li>
				<li class="col-sm-4">
                  <ul>
                    <li><a href="dessert-wine.html">Dessert Wines</a></li>
					<li><a href="fortified-wine.html">Fortifies Wines</a></li>
					<li><a href="table-wine.html">Table Wines</a></li>
				  </ul>
                </li>
                <li class="col-sm-4">
                  <ul>
                    <li><a href="red-wine-list.html">Red Wine List</a></li>
                    <li><a href="white-wine-list.html">White Wine List</a></li>
                  </ul>
                </li>
                
              </ul>
            </li>
            
            <li class="dropdown mega-dropdown"> <a href="#" class="dropdown-toggle " data-toggle="">Wine Bottles & Glasses <b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn2">
                <li class="col-sm-4">
                  <ul>
                    <li class="dropdown-header"><a href="wine-bottles.html">Wine Bottles</a></li>
                    <li><a href="types-of-wine-bottles.html">Types of Wine Bottles</a></li>
                  </ul>
                </li>
				<li class="col-sm-4">
                  <ul>
                    <li class="dropdown-header"><a href="wine-glasses.html">Wine Glasses</a></li>
                    <li><a href="white-wine-glass.html">White Wine Glasses</a></li>
					<li><a href="red-wine-glasses.html">Red Wine Glasses</a></li>
					<li><a href="sparkling-wine-glass.html">Sparkling Wine Glasses</a></li>
					<li><a href="dessert-wine-glass.html">Dessert Wine Glasses</a></li>
					<li><a href="other-types-glasses.html">Other Types of Wine Glasses</a></li>
			     </ul>
                </li>
				<li class="col-sm-4">
                  <ul>
                    <li class="dropdown-header"><a href="wine-accessories.html">Wine Accessories</a></li>
                    <li><a href="wine-coolers.html">Wine Coolers</a></li>
					<li><a href="wine-labels.html">Wine Labels</a></li>
					<li><a href="how-to-open-wine-bottle.html">Wine Openers</a></li>
					<li><a href="other-wine-accessories.html">Other Wine Accessories</a></li>
				 </ul>
                </li>
              </ul>
            </li>
			
			<li class="dropdown mega-dropdown"><a href="#" class="dropdown-toggle" data-toggle="">Wine Drinking <b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn3">
                <li class="col-sm-6">
                  <ul>
                    <li class="dropdown-header"><a href="wine-selection.html">Wine Selection</a></li>
					<li ><a href="wine-evaluation.html">Wine Evaluation</a></li>
					<li ><a href="wine-tasting-skill.html">Wine Tasting Skills</a></li>
					<li ><a href="wine-and-food-pairing.html">Wine Food Pairing</a></li>
					<li ><a href="wine-calories.html">Wine Calories</a></li>
                   </ul>
                </li>
                <li class="col-sm-6">
                  <ul>
                    <li class="dropdown-header"><a href="wine-serving-temperature.html">Wine Serving Temperature</a></li>
                    <li ><a href="red-wine-serving-temperature.html">Red Wine Serving Temperature</a></li>
                    <li ><a href="white-wine-serving-temperature.html">White Wine Serving Temperature</a></li>
					<li ><a href="sparkling-wine-serving-temperature.html">Sparkling Wine Serving Temperature</a></li>
					<li ><a href="fortified-wine-stroing-temperature.html">Dessert & Fortified Wine Serving Temperature</a></li>
                  </ul>
                </li>
			 </ul>
            </li>
			
			<li class="dropdown mega-dropdown"><a href="wine-grapes.html" class="dropdown-toggle" data-toggle="">Wine Grapes <b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn4">
                <li class="col-sm-6">
                  <ul>
                    <li><a href="popular-wine-making-grapes.html">Wine Making Grapes</a></li>
					<li ><a href="wine-grape-varieties.htm">Wine Grape Varieties</a></li>
				 </ul>
                </li>
                <li class="col-sm-6">
                  <ul>
                    <li><a href="red-grapes.html">Red Grapes</a></li>
                    <li ><a href="white-grapes.html">White Grapes</a></li>
                  </ul>
                </li>
			 </ul>
            </li>
           <li class="dropdown mega-dropdown"><a href="wine-making.html" class="dropdown-toggle" data-toggle="">Wine Making<b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn5">
                <li class="col-sm-6">
                  <ul>
                    <li><a href="wine-making-process.html">Wine Making Process</a></li>
					<li ><a href="wine-equipment.html">Wine Making Equiment</a></li>
					<li><a href="wine-color.html">Colours of Wine</a></li>
				  </ul>
                </li>
				 <li class="col-sm-6">
                  <ul>
                    <li ><a href="wine-producing-countries.html">Wine Producing Countries</a></li>
					<li><a href="wine-exporting-countries.html">Wine Exporting Countries</a></li>
				 </ul>
                </li>
              </ul>
            </li>
			<li class="dropdown mega-dropdown"><a href="wine-storage.html" class="dropdown-toggle" data-toggle="">Wine Storage<b class="caret"></b></a>
              <ul class="dropdown-menu mega-dropdown-menu jsn6">
                <li class="col-sm-12">
                  <ul>
                    <li><a href="how-to-store-your-wine-optimal.html">How to store your wine</a></li>
					<li ><a href="conditions-that-affect-wine.html">Conditions that affect wine</a></li>
				 </ul>
                </li>
              </ul>
            </li>
			<li class="dropdown mega-dropdown"><a href="wine-sommelier.html" class="dropdown-toggle" data-toggle="">Wine Sommilier</a></li>
			<li class="dropdown mega-dropdown"><a href="wine-reviews.html" class="dropdown-toggle" data-toggle="">Wine Reviews</a></li>
          </ul>
        </div>
      </nav>
	
        <!-- Menu - end -->
    
    <!--page navigation start-->
	<!-- InstanceBeginEditable name="pagenav" -->
	<!-- page top ads start -->
		<div class="col-sm-12 advertise-top">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- AAW -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-9208166189076321"
     data-ad-slot="9483231912"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
<!-- page top ads end -->
  
    <!-- InstanceEndEditable -->
    <!--page navigation end-->
<!--Content start-->
<div class="row">
  <ul class="page-nav col-sm-12">
    <li><a href="http://www.all-about-wine.com" title="all about wine home">Home</a></li>
      <li> > </li>
      <li><a href="types-of-wine.html" title="types of wines">Types of Wine</a></li>
      <li> > </li>
      <li><a href="types-of-red-wine.html" title="types of red wine">Types of Red Wine</a></li>
      <li> > </li>
      <li><a href="red-wine-list.html" class="page-active" title="list of red wines">Red Wine List</a></li>
  </ul>
</div>
<div class="row clearfix">
  <!--Left Content start-->
  <div class="col-xs-12 col-sm-9">
    <div class="main-content-new font_13">
      <h1 class="verdana_font quote">Red Wine List</h1>
      <p class="top-space">The most popluare red wine types are as follows:</p>
      <ul class="wine-recipes top-space">
        <li>Cabernet Sauvignon </li>
        <li>Pinot Noir</li>
        <li>Syrah</li>
        <li>Zinfandel</li>
      </ul>
      <h3 class="top-space green">Italian Reds</h3>
      <ul class="wine-recipes top-space">
        <li>Sangiovese</li>
        <li>Chianti</li>
        <li>Barolo</li>
        <li>Amarone</li>
        <li>Barbera</li>
        <li>Lambrusco</li>
        <li>Montepulciano</li>
        <li>Valpolicella</li>
        <li>Barbaresco</li>
        <li>Bardolino</li>
        <li>Brunello di Montalcino</li>
        <li>Vino nobile di Montepulciano</li>
      </ul>
      <h3 class="top-space green">French Reds</h3>
      <ul class="wine-recipes top-space">
        <li>Bordeaux</li>
        <li>Burgundy</li>
        <li>Beaujolais</li>
      </ul>
      <h3 class="top-space green">Spanish Reds</h3>
      <ul class="wine-recipes top-space">
        <li>Rioja</li>
        <li>Garnacha</li>
      </ul>
    </div>
  </div>
  <!--Left Content end-->
  <!--Right Content start-->
  <div class="col-xs-12 col-sm-3" >
  <div class="wine-reviews">
    <h2 class="clr-white mrgn-top-none">Wine Recipes</h2>
    <div class="img-wine-reviews"><img src="/images/gl-wine-img.jpg" alt="Wine Reviews" class="img-responsive"/></div>
    <p class="font_13a">Wine recipes page allows you to make recipes with the use of your favorite wines. Here you will see a list of wine recipes both added by us and submitted by our visitors. Enjoy them all.</p>
    <a href="/wine-recipes.html" class="link-readmore font_13a">Read More</a> </div>
  <div class="rht-ads">
	<style>.ads-right{ max-width:265px; }
	
	</style>
	
	<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- AAW -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-9208166189076321"
     data-ad-slot="9483231912"
     data-ad-format="rectangle"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
	

  </div>
  <div class="wine-reviews">
    <h2 class="clr-white">Wine Reviews</h2>
    <div class="img-wine-reviews"><img src="/images/dessert-wine-glass.jpg" alt="Wine Reviews" class="img-responsive"/></div>
    <p class="font_13a">White wines are generally colorless and they are made from the white grape varieties.</p>
    <a href="/wine-reviews.html" class="link-readmore font_13a">Read More</a> </div>
  <div class="rht-ads">
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- AAW -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-9208166189076321"
     data-ad-slot="9483231912"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
  </div>
</div>
  <!--Right Content end-->
</div>
<!--Content end-->
 <!--Footer start-->
    <div class="footer-new">
      <div class="col-xs-6 col-sm-3 col-md-2"><ul>
	  <li><a href="http://www.all-about-wine.com" title="All About Wine">Home</a></li>
        <li><a href="/about-wine.html" title="wine" class="bor-lft-non">About Wine</a></li>
		<li><a href="/wine-contact-us.php" title="All About Wine">Contact Us</a></li>
		<li><a href="/wine-FAQ.html" title="FAQ">FAQ</a></li>
		<li><a href="http://www.all-about-wine.com/aboutwines" title="Blog">Blog</a></li>
		</ul>
	  </div>
	  <div class="col-xs-6 col-sm-3 col-md-2"><ul>
		<li><a href="/history-of-wine.html" title="History of Wine">History of Wine</a></li>
		<li><a href="/about-wine.html" title="About Wine">About Wine</a></li>
		<li><a href="/wine-and-your-health.html" title="Wine & Health">Wine & Health</a></li>
		<li><a href="/wine-misconceptions.html" title="Misconceptions about wine">Misconceptions about wine</a></li>
		<li><a href="/wine-recipes.html" title="Wine Recipes">Wine Recipes</a></li>
	  </ul>
	  </div>
	  <div class="col-xs-6 col-sm-3 col-md-2"><ul>
	    <li><a href="/wine-region.html" title="Wine Regions">Wine Regions</a></li>
		<li><a href="/wineries.html" title="Wineries">Wineries</a></li>
		<li><a href="/all-about-wine-glossary.html" title="Wine Glossary">Wine Glossary</a></li>
		<li><a href="/wine-quotes.html" title="Wine Quotes">Wine Quotes</a></li>
		<li><a href="/wine-gallery.html" title="Wine Gallery">Wine Gallery</a></li>
      </ul>
	  </div>
	  <div class="col-xs-6 col-sm-3 col-md-2"><ul>
        <li><a href="/wine-site-map.html" title="wine site map" class="">Site map</a></li>
        <li><a href="/imprint.html" title="wine imprint" class="">Imprint</a></li>
      </ul>
	  </div>
	  <!--
	  	<div class="col-xs-12 col-sm-12 col-md-4"><div class="navbar-form" role="search">
			<input type="text" placeholder="search text here" class="bottom-newslater" /><input type="submit" value="Submit"  class='btn-submit' />
		</div></div>
		-->
		
   </div>
    <!--Footer end-->
	<div class="bottom-fotter"> 
	<div class="col-sm-12 clearfix">
		 <ul class="footer-social-icon">
        <li><a href="https://www.facebook.com/allaboutwinesonline" title="all about wine facebook page" target="_blank" class="bor_non"><img src="/images/facebook-icon.png" alt="icon" /></a></li>
        <li><a href="http://twitter.com/allaboutwinerie" title="all about wine tweets" target="_blank"><img src="/images/social-icon-twit.png" alt="twit" /></a></li>
        <li><a href="https://plus.google.com/101390476745825259167" title="all about wine google plus" target="_blank"><img src="/images/google-plus.png" alt="google" /></a></li>
        <li><a href="http://de.linkedin.com/in/allaboutwine" title="all about wine linkedin" target="_blank"><img src="/images/linkedin.png" alt="linkedin" /></a></li>
      </ul>
	</div>
	<p>Copyright © 2017 all about wine.com - All rights reserved. <a href="http://www.aumkii.de/" target="_blank" class="bor-lft-non" title="web development and search engine optimization">Web development and SEO by aumkii</a></p>
	</div>
  </div>
  <!--Design view end-->
</div>
<!--Wrapper end-->
<script src="https://code.jquery.com/jquery-3.2.0.min.js" integrity="sha256-JAW99MJVpJBGcbzEuXk4Az05s/XyDdBomFqNlM3ic+I=" crossorigin="anonymous"></script>
<script>
	$(document).ready(function() {
			
		$("#navnav .dropdown").hover(
				function() { 
					$('.dropdown-menu', this).fadeIn("fast");
					if( $(this).hasClass("jsn") || $(this).hasClass("jsn2") || $(this).hasClass("jsn3") ){
						
						var nW="100%";
						
						var width = $('.dropdown-menu', this).width() ;
						
						
					}
				},
				function() { $('.dropdown-menu', this).fadeOut("fast");
		});
		
		
		
	});
</script>

<script>


	function isMobile(){
		if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
			// some code..
			return true;
		}else return false;
	}
</script>

<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-10140274-1");
pageTracker._trackPageview();
} catch(err) {}</script></body></html> """

soup = BeautifulSoup(white_wines, 'html.parser')
uls = soup.find_all('ul')
whitelist = uls[23].findAll('li')
lisW = []
for var in whitelist:
	lisW.append(var.text)
print(lisW)

soup = BeautifulSoup(red_wines, 'html.parser')
uls = soup.find_all('ul')
lisR = []
redlist = []
i = 0
for avr in uls:
	if i >= 23 and i <= 26:
		redlist.append(avr)
	i += 1
for var in redlist:
	for sort in var.text.split('\n'):
		if len(sort) > 0:
			lisR.append(sort)

print(lisR)

wine_Varieties = {"white": lisW, "red": lisR}
with open('wine_varieties.json', 'w') as output:
	json.dump(wine_Varieties, output)
# lis =
# print(lis)

