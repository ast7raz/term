var currentSelection = -1;

function isNumber(data) {
   var numStr="0123456789";
   var thisChar; 
   var counter = 0;
   for (var i=0; i < data.length; i++) {
      thisChar = data.substring(i, i + 1);
      if (numStr.indexOf(thisChar) != -1) counter++;
   }
   if (counter == data.length) {
// Все введенные символы являются цифрами 
      return false;
} else{
      return true;}
}

var valform=function(data){
}
var ValidationRequest= function(val){var tester=$.ajax({
	url:"./valid/",
	type:"POST",
	cache:true,
	dataType:"json",
	data:({value:val,csrfmiddlewaretoken:getCode()}),
	success:valform,
	async: false
	}).responseText
	return tester
	}

	
Array.range= function(a, b, step){
    var A= [];
    if(typeof a== 'number'){
        A[0]= a;
        step= step || 1;
        while(a+step<= b){
            A[A.length]= a+= step;
        }
    }
    else{
        var s= 'abcdefghijklmnopqrstuvwxyz';
        if(a=== a.toUpperCase()){
            b=b.toUpperCase();
            s= s.toUpperCase();
        }
        s= s.substring(s.indexOf(a), s.indexOf(b)+ 1);
        A= s.split('');        
    }
    return A;
}
function livevalidate(event){
var element=$(this).parents("section")
//console.log($(this))
var element2=$(event.relatedTarget).parents("section")
//console.log($(event.relatedTarget))
//console.log(element.attr("id"))
//console.log(element)
//console.log(element2.attr("id"))
//console.log(element2)
if (element.attr("id")!=element2.attr("id")){
if ($(this).attr("type")=="radio"){
	var parr=$(this).parent("div")
	var inps=parr.children("input:checked")
	var inpus=inps.children("input:checked")
	len=inps.length
	//console.log(len)
	if ((len==0)&&($(this).attr("name")!='level')){
		var erhid=parr.children(".errorhiden")
		erhid.attr("class", "errorvisible")
		parr.addClass("ulvis")
	}else if ((len>0)&&($(this).attr("name")!='level')){
		var erhid=parr.children(".errorvisible")
		erhid.attr("class", "errorhiden")
		parr.removeClass("ulvis")
	}
}else if ($(this).attr("type")=="text"){
	if (($(this).attr("name")=="coment")||($(this).attr("name")=="duration")){
		if ($(this).val()==''){
			var el=$(this).prev(".errorhiden, .errorvisible")
			el.attr("class", "errorvisible")
			el.text("Это обязательное поле! Введите ответ.")
				//console.log("Введите ответ")
				
		}else{
			var el=$(this).prev(".errorvisible")
			el.attr("class", "errorhiden")
			if ($(this).attr("name")=="duration"){
				var values=($(this).val())
				if (isNumber(values)){
					//console.log("True")
					var el=$(this).prev(".errorhiden, .errorvisible")
					el.attr("class", "errorvisible")
					el.text("Поле может быть заполнено только цифрами!")
				}else{
					var el=$(this).prev(".errorvisible")
					el.attr("class", "errorhiden")
					el.text("Это обязательное поле! Введите ответ.")
				}
			}
		}
	}else if ($(this).attr("name")=="casher"){
		setTimeout(function(){$('.listBox').hide( )},300)
		if ($(this).val()==''){
			var el=$("div .casher").children("#error")
			el.text("Это обязательное поле! Введите ответ.")
			el.attr("class", "errorvisible")
				//console.log("Введите ответ")
		}else if (element2.attr("id")!=undefined){
			//console.log(undefined)
			var tester=ValidationRequest($(this).val())
			var otv=JSON.parse(tester)
			if (otv.error!="True"){
				$(this).attr("value", otv.value)
				$(this).attr("priznak", otv.priznak)
				$(this).val(otv.text)
				var el=$("div .casher").children("#error")
				el.text("Это обязательное поле! Введите ответ.")
				el.attr("class", "errorhiden")
			}else{
				$(this).attr("value", otv.value)
				$(this).attr("priznak", otv.priznak)
				//$(this).val(otv.text)
				var el=$("div .casher").children("#error")
				el.text("Нет такой партнёрской группы или кассы. Заполните поле правильно!")
				el.attr("class", "errorvisible")
			}
				
		}
		
	}
}
}
}

function setScrol(){
var listposition=$(".listbox").offset().top
var listheight=$(".listbox").height()
var elposition=$(".itemhover").offset().top
var elheight=$(".itemhover").height()
var listtest=listposition+listheight
//console.log(elposition+" "+listtest)
if(elposition<listposition){
$(".listbox").scrollTop($(".listbox").scrollTop()-elheight)
}else if(elposition>listposition+listheight){
$(".listbox").scrollTop($(".listbox").scrollTop()+elheight)
}

}
function setSelected(menuitem) {
$("#Listbox>*").removeClass("itemhover");
$("#Listbox>*").eq(menuitem).addClass("itemhover");
setScrol()
}
function Navigate(direction) {
// Проверяем, не выбран ли какой-либо пункт меню
if($("#Listbox>* .itemhover").size() == -1) {
	currentSelection = 0;
}
if(direction == 'up' && currentSelection != 0) {
	//console.log(direction)
	if(currentSelection != -1) {
		currentSelection--;
	}
} else if (direction == 'down') {
	//console.log(direction)
	if(currentSelection != $("#Listbox>*").size()-1) {
		//console.log(currentSelection+"  "+$("#Listbox>*").size()-1)
		currentSelection++;
	}
	}
setSelected(currentSelection);
}
var clickFunc=function(event){
//sect=$(this).parents("section").attr("id")
var pu=$(this)
var val=pu.text()
var id=pu.attr("con")
var priz=pu.attr("id")
//console.log("click on listPunct "+val+' '+id+" "+priz)
$('#listinp').val(val)
$('#listinp').attr("priznak",priz)
$('#listinp').attr("value",id)
$('#listinp').trigger("focus")
$('.listBox').hide( )
}
var listContext= function(data){
currentSelection = -1;
	var lis=$('#Listbox')
	lis.empty()
	ls=0
	for(da in data){
		var ListPunct="<dt foc='0' ls="+ls+" id="+data[da].pr+" con="+data[da].id+">"+data[da].name+"</dt>"
		lis.append(ListPunct)
		ls=ls+1
		for (i in data[da].dop){
			var ListPunctCash="<dd foc='0' ls="+ls+" id="+data[da].dop[i].pr+" con="+data[da].dop[i].id+">"+data[da].dop[i].name+"</dd>"
			lis.append(ListPunctCash)
			ls=ls+1
		}
		
	}
	$("dt").bind("click", clickFunc).bind("mouseover", function(){$("#Listbox>*").removeClass("itemhover");$(this).addClass("itemhover"); currentSelection=$(this).attr("ls")})
	$("dd").bind("click", clickFunc).bind("mouseover", function(){$("#Listbox>*").removeClass("itemhover");$(this).addClass("itemhover"); currentSelection=$(this).attr("ls")})
	function deset(){
	
	var height=$('#listinp').height()
	var off=$('#listinp').offset()
	var got=off.top+height
	var obj=new Object({"top":got, "left":off.left})
	//console.log(obj)
	return (obj)
	}
	$('.listBox').show()
	$('.listbox').offset(deset)
	
};
var ListRequest= function(val){$.ajax({
	url:"./cash/",
	type:"POST",
	cache:true,
	dataType:"json",
	data:({value:val,csrfmiddlewaretoken:getCode()}),
	success:listContext,
	})
	}
function testfunc(event){
if ((event.keyCode==13) || (event.keyCode==16) || (event.keyCode==17) || (event.keyCode==9) || (event.keyCode==27) || (event.keyCode==37) || (event.keyCode==38) || (event.keyCode==39) || (event.keyCode==40)){
	if ((event.keyCode==38)||(event.keyCode==40)){
		if(event.type=="keydown"){	
			if (event.keyCode==40){
				Navigate("down")
			}
			else{
				Navigate("up")
			}
		}
	}
	if (event.keyCode==13){
		if(event.type=="keyup"){
			$(".itemhover").trigger("click")
		}
	}
}
else{
	if(event.type=="keyup"){
		$("input[name=casher]").removeAttr("value").removeAttr("priznak")
		ListRequest($(this).val())
	}
}
}