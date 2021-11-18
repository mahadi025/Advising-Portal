btn=document.getElementById("cross")
btn.style.visibility="hidden"

function add(tbl_id){
    let table=document.getElementById(tbl_id),
    frst_tr=table.firstElementChild

    tr_clone=frst_tr.cloneNode(true)
    tr_clone.cells[0].children[0].value=" "
    tr_clone.cells[1].children[0].value=" "
    tr_clone.cells[2].children[0].value=" "
    tr_clone.cells[3].children[0].style.visibility="visible"
    table.append(tr_clone)

}
function remove(This){
 
     This.closest('tr').remove()

}
function count(tbody){
  let tbl=document.getElementById(tbody),sum1=0,sum2=0,cgpa
  for(let i=0;i<tbl.rows.length;i++){
      sum2=sum2+parseFloat(tbl.rows[i].cells[1].children[0].value)
       sum1=sum1+ parseFloat(tbl.rows[i].cells[2].children[0].value)*parseInt(tbl.rows[i].cells[1].children[0].value)
  }
   cgpa=sum1/sum2
   document.getElementById("CGPAcount").innerHTML=cgpa.toFixed(2)
   
   
}
