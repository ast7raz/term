function addCh(otvet){
	console.log(otvet)
	var elem=["id_partner", "id_club", "id_cash"]
	for (el in elem){
		var loo=elem[el]
		var clms=document.getElementById(loo)
		var iter=loo.substr(3)
		var iterat=otvet[iter]
		var sel=otvet["select"][iter]
		
		for (key in iterat){
			var option=document.createElement("option")
			option.value=key
			option.text=iterat[key]
			
			if (parseInt(key)==sel){
				option.selected=true
				}
			clms.add(option)
			
		}
		
		}
	
}
function SendRequest(param){
	xmlhttp= new XMLHttpRequest();
	xmlhttp.open("GET","/pb/?"+param,true);
	xmlhttp.onload = function() {
		var otvet=JSON.parse(this.responseText)
		addCh(otvet)
		}
	xmlhttp.send();
	}
function clearSelect(id){
	var clms=document.getElementById(id)
	if (clms.length>1){
		clms.remove(clms.length-1);
		clearSelect(id)
		}
	}
function addChoise() {
	var select={}
	var selectid=this.id
	var param=this.value
	var elem=["id_partner", "id_club", "id_cash"]
	for (el in elem){
		var para=(elem[el].substr(3))
		var element=document.getElementById(elem[el])
		var text= element.options[element.selectedIndex].value
		select[para]=text
	}
	for (el in elem){
		clearSelect(elem[el])
		}
	var param=[]
	for (k in select){
		param.push(k+"="+select[k])
	}
	param=param.join("&")
	console.log(param)
	SendRequest(param)
}