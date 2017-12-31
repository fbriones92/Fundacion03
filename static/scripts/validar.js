
function valida(e){
    tecla = (document.all) ? e.keyCode : e.which;

    //Tecla de retroceso para borrar, siempre la permite
    if (tecla==8){
        return true;
    }
        
    // Patron de entrada, en este caso solo acepta numeros
    patron =/[0-9]/;
    tecla_final = String.fromCharCode(tecla);
    return patron.test(tecla_final);
}





function validarcedula()
{
 var i;
 var cedula;
 var acumulado;
 
 cedula=document.formacedula.cedula.value;
 var instancia;
 acumulado=0;
 
 for (i=1;i<=9;i++)
 {
  if (i%2!=0)
  {
   instancia=cedula.substring(i-1,i)*2;
   if (instancia>9) instancia-=9;
  }
  else instancia=cedula.substring(i-1,i);
  acumulado+=parseInt(instancia);
 }
 while (acumulado>0)
  acumulado-=10;
 if (cedula.substring(9,10)!=(acumulado*-1))
 {
  alert("Campo cedula no valido, verificar!!");
  document.formacedula.textocedula.setfocus();
 }
 	    
}
function SoloNumeros(event){
	if(window.event){//asignamos el valor de la tecla a keynum
	keynum = event.keyCode; //IE

	}
	else{
	keynum = event.which; //FF
	}
	//comprobamos si se encuentra en el rango numérico y que teclas no recibirá.
	if((keynum == 47 || keynum == 58) || keynum == 8 || keynum == 13 || keynum
	== 6 ){
	return true;
	}
	else{
	alert("INGRESE SU Nº");
	return false;
	}
	}