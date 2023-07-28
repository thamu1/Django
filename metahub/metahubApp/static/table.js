window.addEventListener('load',()=>
{
    var val = localStorage.getItem("sa");

    var sub_area = document.getElementById("subject_area");
    var in_source = document.getElementById("ingestion_source");
    var ing_con = document.getElementById("ingestion_controller");
    var gcp_sche = document.getElementById("gcp_scheduler");
    var sche_ing_map = document.getElementById("gcp_scheduler_ingestion_mapping");
    var con_obj = document.getElementById("gcp_config_objects");
    var air_sche = document.getElementById("gcp_airflow_scheduler");
    var air_con_map = document.getElementById("airflow_configobjs_mapping");
    var con_ing_map = document.getElementById("gcp_configobjs_ingestion_mapping");
    var sche_sche_tri = document.getElementById("gcp_scheduler_scheduler_trigger");
    var con_depen = document.getElementById("airflow_configobjs_dependency");

    var blk = val.slice(0,5)
    var con_val = val.slice(6,val.length)

    alert("you enter into : " +con_val)

    if(blk === "block")
    {
        if(con_val == "sub_area")
        {
            sub_area.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "in_source")
        {
            in_source.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "ing_con")
        {
            ing_con.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "gcp_sche")
        {
            gcp_sche.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "sche_ing_map")
        {
            sche_ing_map.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "con_obj")
        {
            con_obj.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "air_sche")
        {
            air_sche.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "air_con_map")
        {
            air_con_map.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "con_ing_map")
        {
            con_ing_map.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "sche_sche_tri")
        {
            sche_sche_tri.style.display = blk;
            localStorage.removeItem("sa");
        }
        else if(con_val == "con_depen")
        {
            con_depen.style.display = blk;
            localStorage.removeItem("sa");
        }
    }
    
})

