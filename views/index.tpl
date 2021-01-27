<html>
<head>
 <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
<title>New Posts</title>
</head>
<div class="container">
  <div class="cont">
    <div class="flex">
      <form method="post" action="/" enctype="multipart/form-data" class="one">
           <label for="texte_chiffrer">Dechiffrer le texte </label><br />
             <textarea type="text" name="texte_chiffrer"  id="texte" class="">  </textarea><br />
             <input type="file" name="file" id="fichier" /><br />
           <input type="submit" name="submit" value="Dechiffrer" id="submit" />
      </form>
      <div class="two">
        <div class="">
          <div class="">
            chiffre de <br>
          </div>
          <div class="">
            {{ type_chiffrement }}
          </div>
        </div>
        <div class="">
          <div class="">
            <div class="">
              Clé <br>
            </div>
            <div class="">
              {{cle}}
            </div>
          </div>
        </div>
      </div>
      <div class="three" style="padding-bottom: 55px;">
        <div class="text">
          Texte déchifré
        </div>
        <div class="">
          {{texte }}
        </div>
      </div>

    </div>
  </div>
</div>






</html>
<style>

#submit{
	background-color:#a0ce4e;
	color:#ffffff;
	width:107px;
	height:42px;
	transition-duration: .5s;
	border-top-left-radius:25px;
	border-top-right-radius:25px;
	border-bottom-left-radius:25px;
	border-bottom-right-radius:25px;
	border-width:1px;
}

#submit:hover{
	background-color:#fff !important;
	color:#a0ce4e !important;
	border-width:1px;
	border-color:#a0ce4e !important;
}

.container{
	padding-top: 100px;
}

/* Division */
/* .flex > div:nth-child(2) > div:nth-child(1) div:nth-child(1){
	text-align:center;
} */

.flex{
	display: flex;
	align-items: center;
}

/* Division */
/* .flex div div div div:nth-child(1){
	text-align:center;
} */

/* Division */
.flex div:nth-child(3) div:nth-child(1){
	/* text-align:center; */
	padding-bottom:20px;
  padding-left: 60px;
  /* padding-top: : 30px; */
}

.one{
	flex: 1;
	padding: 20px;
}

.two{
	flex: 1;
	padding: 40px;
}

.three{
	flex: 1;
	padding: 40px;
}

/* Division */
.two > div > div{
	text-align:center;
	padding-top:25px !important;
	padding-bottom:4px !important;
	background-color:transparent;
}

/* Division */
.two > div:nth-child(1) div:nth-child(1){
	padding-top:0px;
	padding-bottom:0px;
	font-weight:500;
	font-size:28px;
	font-family:'Montserrat Alternates', sans-serif;
	color:#2c3e50;
}

body{
	background-color:rgba(245,245,245,1) !important;
	font-family:'Montserrat Alternates', sans-serif!important;
}

/* Form Division */
#main_content .flex form{
	border-top-right-radius:25px;
	border-bottom-left-radius:25px;
	border-bottom-right-radius:25px;
}

/* Division */
.two div div div{
	padding-left:25px;
	padding-right:25px;
	padding-top:5px !important;
	padding-bottom:25px;
	padding-left:25px;
	padding-right:25px;
	padding-top:26px !important;
	padding-bottom:25px;
}

/* Division */
.two > div:nth-child(1) div:nth-child(2){
	background-color:#ffffff;
	border-top-left-radius:25px;
	border-top-right-radius:25px;
	border-bottom-left-radius:25px;
	border-bottom-right-radius:25px;
	padding-bottom:25px !important;
}

/* Division */
.two div div div:nth-child(1){
	padding-left:25px;
	padding-top:0px;
	padding-bottom:21px;
	font-weight:500;
	font-size:26px;
	color:#2c3e50;
}

/* Division */
.two div div div:nth-child(2){
	padding-top:5px;
	padding-top:5px;
	background-color:#ffffff;
	border-top-left-radius:25px;
	border-top-right-radius:25px;
	border-bottom-left-radius:25px;
	border-bottom-right-radius:25px;
}

.cont{
	padding: 40px;
}

/* Main wrapper */
.site_wrapper .main_wrapper{
	background-color:rgba(245,245,245,1) !important;
}

/* Form Division */
.cont .flex form{
	flex-grow:1;
	border-top-left-radius:25px;
	border-top-right-radius:25px;
	border-bottom-left-radius:25px;
	border-bottom-right-radius:25px;
	border-width:1px;
	border-style:none;
	text-align:center;
	padding-top:0px;
	padding-right:0px;
	padding-left:0px;
	padding-bottom:0px;
}

/* Texte */
#texte{
  width:312px;
	height:243px;
	border-top-left-radius:25px;
	border-top-right-radius:25px;
	border-bottom-left-radius:25px;
	border-bottom-right-radius:25px;
	padding-left:0px;
	padding-right:0px;
	padding-top:0px;
	padding-bottom:0px;
}

/* Division */
.flex .three div:nth-child(2){
	border-style:solid;
	border-width:1px;
	border-color:#727e85;
	border-top-left-radius:25px;
	border-top-right-radius:25px;
	border-bottom-left-radius:25px;
	border-bottom-right-radius:25px;
	text-align:center;
	background-color:#ffffff;
  width:312px;
	height:243px;

}
.cont .flex .three{
	padding-top:0px;

}

/* Division */
.flex .three div{
	position:relative;
	top:-14px;
	left:-3px;
}

/* Fichier */
#fichier{
	position:relative;
	top:100px;
	font-size:16px;
	width:239px;
}

/* Input */
.flex .one input:nth-child(7){
	background-color:#a0ce4e;
	border-width:0px;
	color:#ffffff;
}

/* Division */
.flex .three div:nth-child(1){
	font-weight:500;
	font-size:28px;
	/* text-align:center; */
	/* top:-71px; */

}


/* Label */
.flex .one label{
	position:relative;
	top:-23px;
	left:0px;
	font-size:28px;
	font-weight:500;
}

/* Form Division */
.site_wrapper .main_wrapper .container .row .content-container #main_content .container .cont .flex form{
	background-color:rgba(245,245,245,1) !important;
}






</style>
