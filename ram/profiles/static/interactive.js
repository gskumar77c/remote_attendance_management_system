function new_form() {
    // var x = document.getElementById("student");   
    // x.style.display = "none";
    var submit_button = document.getElementById("submit");   
    submit_button.style.visibility = "visible";
    var qualification = document.getElementById("id_user-qualification");
    var strUser = qualification.options[qualification.selectedIndex].value;
    var qtype_form=document.getElementById(strUser);
    qtype_form.classList.remove("initial_hiding");
    
    if (strUser!="instructor")
    {
        var iform=document.getElementById("instructor");
        iform.parentNode.removeChild(iform)
    }
    if (strUser!="ta")
    {
        var tform=document.getElementById("ta");
        tform.parentNode.removeChild(tform)
    }
    if (strUser!="student")
    {
        var sform=document.getElementById("student");
        sform.parentNode.removeChild(sform)
    }
        
    var next_button=document.getElementById("next");
    next_button.classList.add("initial_hiding");
    var reg_text=document.getElementById("reg_name")
    reg_text.value=strUser
    // y.style.display="block"
    


}   