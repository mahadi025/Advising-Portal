document.getElementById("str1").style.visibility="hidden"
document.getElementById("str2").style.visibility="hidden"
function clk(){
 var x,y,z;
 x=document.getElementById("semester").value;
 y=document.getElementById("year").value;
 z=document.getElementById("note").innerText;
 
  
 if(x==null|| x==""||!(x=="Fall"||x=="FALL"||x=="fall"||x=="Spring"||x=="spring"||x=="SPRING"||x=="Summer"||x=="SUMMER"||x=="summer") ){
    document.getElementById("semester").style.borderWidth="3px" 
    document.getElementById("semester").style.borderColor="#FF0101";
    document.getElementById("str1").style.visibility="visible"
     alert("Invalid Semester");
     }
 if(y==null || y==""||y<=2019){
    document.getElementById("year").style.borderWidth="3px"
    document.getElementById("year").style.borderColor="#FF0101";
    alert("Invalid year");
    document.getElementById("str2").style.visibility="visible"
    
}
if(x=="Fall"||x=="FALL"||x=="fall"||x=="Spring"||x=="spring"||x=="SPRING"||x=="Summer"||x=="SUMMER"||x=="summer"){
    document.getElementById("semester").style.borderWidth="3px"
    document.getElementById("semester").style.borderColor="green";
    document.getElementById("str1").style.visibility="hidden"
    
}

if(y>=2019){
    document.getElementById("year").style.borderWidth="3px"
    document.getElementById("year").style.borderColor="green";
    document.getElementById("str2").style.visibility="hidden"
}
}








