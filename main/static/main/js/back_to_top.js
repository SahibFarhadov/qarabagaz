let btn=document.getElementById('backtotop');
window.onscroll=function() {scrollFunction()};
function scrollFunction(){
	if (document.body.scrollTop>40 || document.documentElement.scrollTop>40){
		btn.style.display="block";
	}
	else{
		btn.style.display="none";
	}
}
function backTop(){
	document.body.scrollTop=0;
	document.documentElement.scrollTop=0;
}