from django.shortcuts import render,redirect
from django.db import connection
import mysql.connector as mc
from pathlib import Path
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

BASE_DIR = Path(__file__).resolve().parent.parent


sql_ing_com = """select sa.subjectarea_id,
sa.subjectarea_name,
 ins.sourceid as "ingestion_source_id",
 sch.group_binding_id as "ingestion_group_binding_id",
 sch.trigger_script as "ingestion_trigger_script",
 sch.comments,
 sst.trigger_group_binding_id as "compute_group_binding_id",
ache.dag_name as "airflow_dag_name",
ache.parent_bash_script as "compute_generic_script",
trigger_bash_script as "airflow_trigger_script",
coj.object_id as "config_object_id",
coj.object_name as "config_object_name"
from gcp_subjectarea sa join 
gcp_ingestion_sources ins on sa.subjectarea_id = ins.subjectarea_id join
gcp_scheduler_ingestion_mapping gmp on ins.sourceid=gmp.sourceid join
gcp_scheduler_scheduler_trigger sst on gmp.group_binding_id = sst.group_binding_id join
gcp_scheduler sch on sch.group_binding_id = sst.group_binding_id join
gcp_airflow_scheduler ache on ache.group_binding_id = sst.trigger_group_binding_id join
gcp_config_objects coj on coj.subjectarea_id = sa.subjectarea_id
where sa.subjectarea_id = 90
group by coj.object_id;"""


conn = mc.connect(
    host='127.0.0.1',
    user='root',
    password='Mysql.08',
    database='world'
)

cursor = conn.cursor()


def home(request):
    # selsql = 'select * from city limit 50'
    # cursor.execute(selsql)
    # result = cursor.fetchall()
    context = {'get':"Pch"}
    return render(request,'home.html',context)

@xframe_options_exempt
def insert(request):
    context = {'path':BASE_DIR}
    return render(request,'insert.html',context)

@xframe_options_exempt
def tables(request):
    return render(request,'tables.html')

@xframe_options_exempt
def metainsert(request):
    form_name = request.POST.get('formname')
    
    if request.method == 'POST' and form_name == 'subject_area':
        subjectarea_id = request.POST.get('subjectarea_id')
        project_id = request.POST.get('project_id')
        subjectarea_name = request.POST.get('subjectarea_name')
        subjectarea_desc = request.POST.get('subjectarea_desc')
        status_flag = request.POST.get('status_flag')
        
        val = (int(subjectarea_id),int(project_id),subjectarea_name,subjectarea_desc,int(status_flag))
        context = {'sub': val}
        
        
        query = "INSERT INTO gcp_subjectarea (subjectarea_id, project_id, subjectarea_name, subjectarea_desc, status_flag) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()
        
        return render(request, 'content.html',context)
    
    elif request.method == 'POST' and form_name == 'ingestion_source':
        source_id = request.POST.get('sourceid')
        classification_id = request.POST.get('classification_id')
        subject_area_id = request.POST.get('subjectarea_id')
        credential_id = request.POST.get('credential_id')
        data_type_id = request.POST.get('data_type_id')
        application = request.POST.get('application')
        sourcedb = request.POST.get('sourcedb')
        tablebase = request.POST.get('tablebase')
        hdl_loadtype = request.POST.get('hdl_loadtype')
        hdl_subtype = request.POST.get('hdl_subtype')
        frequency = request.POST.get('frequency')
        id_column = request.POST.get('idcolumn')
        date_column = request.POST.get('datecolumn')
        column_list = request.POST.get('columnlist')
        sa_db = request.POST.get('sa_db')
        sa_table_name = request.POST.get('satablename')
        staging1_db = request.POST.get('staging1_db')
        staging1_name = request.POST.get('staging1name')
        staging2_db = request.POST.get('staging2_db')
        staging2_name = request.POST.get('staging2name')
        server_ip = request.POST.get('serverip')
        status_flag = request.POST.get('status_flag')
        
        
        val = (int(source_id),int(classification_id),int(subject_area_id),int(credential_id),
    int(data_type_id),application,sourcedb,tablebase,hdl_loadtype,hdl_subtype,
    frequency,id_column,date_column,column_list,sa_db,sa_table_name,staging1_db,staging1_name,staging2_db,
    staging2_name,server_ip,int(status_flag)
    )
        
        query = "INSERT INTO gcp_ingestion_sources (sourceid, classification_id, subjectarea_id, credential_id, data_type_id, application, sourcedb, tablebase, hdl_loadtype, hdl_subtype, frequency, idcolumn, datecolumn, columnlist, sa_db, satablename, staging1_db, staging1name, staging2_db, staging2name, serverip, status_flag) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()
    
        context = {"sub":val}
        return render(request, 'content.html',context)
        
    elif request.method == 'POST' and form_name == 'ingestion_controller':
        controller_id = request.POST.get('controller_id')
        source_id = request.POST.get('sourceid')
        file_format = request.POST.get('fileformat')
        append_mode = request.POST.get('appendmode')
        sql_query = request.POST.get('sqlquery')
        boundary_query = request.POST.get('boundaryquery')
        number_of_mappers = request.POST.get('numberofmappers')
        split_by_column = request.POST.get('splitbycolumn')
        target_directory = request.POST.get('targetdir')
        warehouse_directory = request.POST.get('warehousedir')
        null_string = request.POST.get('nullstring')
        fields_terminator = request.POST.get('fieldsterminater')
        lines_terminator = request.POST.get('linesterminater')
        log_file_location = request.POST.get('logfilelocation')
        reload_date_from = request.POST.get('reloaddatefrom')
        staging1_directory = request.POST.get('staging1dir')
        staging2_directory = request.POST.get('staging2dir')
        table_load_in_process_flag = request.POST.get('tableloadinprocessflag')
        etl_reload_list = request.POST.get('etl_reloadlist')
        etl_reload_from = request.POST.get('etl_reloadfrom')
        cdc_backtrace_days = request.POST.get('cdcbacktracedays')
        end_trace_days = request.POST.get('endtracedays')
        where_clause = request.POST.get('whereclause')
        threshold_for_upper_limit = request.POST.get('threshold_for_upperlmt')
        
        val = (
    int(controller_id),int(source_id),file_format,append_mode,sql_query,boundary_query,
    int(number_of_mappers),split_by_column,target_directory,warehouse_directory,null_string,fields_terminator,
    lines_terminator,log_file_location,reload_date_from,staging1_directory,staging2_directory,table_load_in_process_flag,
    etl_reload_list,etl_reload_from,cdc_backtrace_days,end_trace_days,where_clause,int(threshold_for_upper_limit)
    )
        
        query = "INSERT INTO gcp_ingestion_controller (controller_id, sourceid, fileformat, appendmode, sqlquery, boundaryquery, numberofmappers, splitbycolumn, targetdir, warehousedir, nullstring, fieldsterminater, linesterminater, logfilelocation, reloaddatefrom, staging1dir, staging2dir, tableloadinprocessflag, etl_reloadlist, etl_reloadfrom, cdcbacktracedays, endtracedays, whereclause, threshold_for_upperlmt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()

        context = {"sub":val}
        return render(request, 'content.html',context)
        
    
    elif request.method == 'POST' and form_name == 'gcp_scheduler':
        group_binding_id = request.POST.get('group_binding_id')
        classification_id = request.POST.get('classification_id')
        trigger_script = request.POST.get('trigger_script')
        params = request.POST.get('params')
        target = request.POST.get('target')
        base_trigger_type = request.POST.get('base_trigger_type')
        status_flag = request.POST.get('status_flag')
        exec_flag = request.POST.get('exec_flag')
        developed_by = request.POST.get('developed_by')
        comments = request.POST.get('comments')
        
        val = (
    int(group_binding_id),int(classification_id),trigger_script,params,
    target,base_trigger_type,int(status_flag),exec_flag,developed_by,comments
    )

        query = "INSERT INTO gcp_scheduler (group_binding_id, classification_id, trigger_script, params, target, base_trigger_type, status_flag, exec_flag, developed_by, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()


        context = {"sub":val}
        return render(request, 'content.html',context)
        
    elif request.method == 'POST' and form_name == 'gcp_scheduler_ingestion_mapping':
        mapping_id = request.POST.get('mapping_id')
        source_id = request.POST.get('sourceid')
        group_binding_id = request.POST.get('group_binding_id')
        exec_order = request.POST.get('exec_order')
        skip_flag = request.POST.get('skip_flag')
        avg_execution_time = request.POST.get('avgexectime')
        
        val = (
    int(mapping_id),int(source_id),int(group_binding_id),
    int(exec_order),int(skip_flag),int(avg_execution_time)
    )

        
        query = "INSERT INTO gcp_scheduler_ingestion_mapping (mapping_id, sourceid, group_binding_id, exec_order, skip_flag, avgexectime) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()

        context = {"sub":val}
        return render(request, 'content.html',context)
        
    elif request.method == 'POST' and form_name == 'gcp_config_objects':
        object_id = request.POST.get('object_id')
        classification_id = request.POST.get('classification_id')
        subjectarea_id = request.POST.get('subjectarea_id')
        data_type_id = request.POST.get('data_type_id')
        object_name = request.POST.get('object_name')
        source_name = request.POST.get('sourcename')
        application = request.POST.get('application')
        dataset_name = request.POST.get('datset_name')
        object_description = request.POST.get('object_desc')
        load_type = request.POST.get('loadtype')
        recon_start_limit = request.POST.get('recon_start_limit')
        recon_end_limit = request.POST.get('recon_end_limit')
        status_flag = request.POST.get('status_flag')
        bypass_recon_start_limit_hrly_loads = request.POST.get('bypass_recon_start_limit_hrly_loads')
        control_flag = request.POST.get('control_flag')
        partition_flag = request.POST.get('partition_flag')
        frequency = request.POST.get('frequency')
        developed_by = request.POST.get('development_by')
        development_date = request.POST.get('development_date')
        updated_by = request.POST.get('updated_by')
        update_date = request.POST.get('update_date')
        
        val = (
    int(object_id),int(classification_id),int(subjectarea_id),int(data_type_id),object_name,source_name,application,
    dataset_name,object_description,load_type,int(recon_start_limit),int(recon_end_limit),int(status_flag),int(bypass_recon_start_limit_hrly_loads),
    control_flag,int(partition_flag),frequency,developed_by,
    development_date,updated_by,update_date
    )


        query = "INSERT INTO gcp_config_objects (object_id, classification_id, subjectarea_id, data_type_id, object_name, sourcename, application, dataset_name, object_desc, loadtype, recon_start_limit, recon_end_limit, status_flag, bypass_recon_start_limit_hrly_loads, control_flag, partition_flag, frequency, developed_by, development_date, updated_by, update_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()

        context = {"sub":val}
        return render(request, 'content.html',context)
        
    elif request.method == 'POST' and form_name == 'gcp_airflow_scheduler':
        airflow_binding_id = request.POST.get('airflow_binding_id')
        group_binding_id = request.POST.get('group_binding_id')
        dag_name = request.POST.get('dag_name')
        parent_bash_script = request.POST.get('parent_bash_script')
        trigger_bash_script = request.POST.get('trigger_bash_script')
        params = request.POST.get('params')
        json_file_loc = request.POST.get('json_file_loc')
        status_flag = request.POST.get('status_flag')
        exec_order = request.POST.get('exec_order')
        exec_flag = request.POST.get('exec_flag')
        developed_by = request.POST.get('developed_by')
        comments = request.POST.get('comments')
        
        val = (
    int(airflow_binding_id),int(group_binding_id),dag_name,parent_bash_script,trigger_bash_script,params,
    json_file_loc,int(status_flag),int(exec_order),exec_flag,developed_by,comments
    )

        
        query = "INSERT INTO gcp_airflow_scheduler (airflow_binding_id, group_binding_id, dag_name, parent_bash_script, trigger_bash_script, params, json_file_loc, status_flag, exec_order, exec_flag, developed_by, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()

        context = {"sub":val}
        return render(request, 'content.html',context)
        
    elif request.method == 'POST' and form_name == 'airflow_configobjs_mapping':
        airflow_mapping_id = request.POST.get('airflow_mapping_id')
        airflow_binding_id = request.POST.get('airflow_binding_id')
        exec_order = request.POST.get('exec_order')
        object_id = request.POST.get('object_id')
        skip_flag = request.POST.get('skip_flag')
        airflow_control_flag = request.POST.get('airflow_control_flag')
        gcp_schema_initial = request.POST.get('gcp_schema_initial')
        gcp_schema_intermediate = request.POST.get('gcp_schema_intermediate')
        gcp_schema_final = request.POST.get('gcp_schema_final')
        gcp_schema_sas_final = request.POST.get('gcp_schema_sas_final')
        gcp_partition_cols = request.POST.get('gcp_partition_cols')
        gcp_cluster_cols = request.POST.get('gcp_cluster_cols')
        obj_gcs_path = request.POST.get('obj_gcs_path')
        obj_gcs_final_alter_name = request.POST.get('obj_gcs_final_alter_name')
        obj_gcs_stg_to_final_split_flag = request.POST.get('obj_gcs_stg_to_final_split_flag')
        vw_sql_except_columns = request.POST.get('vw_sql_except_columns')
        vw_sql_loc = request.POST.get('vw_sql_loc')
        comments = request.POST.get('comments')
        
        val = (
    int(airflow_mapping_id),int(airflow_binding_id),int(exec_order),int(object_id),int(skip_flag),airflow_control_flag,
    gcp_schema_initial,gcp_schema_intermediate,gcp_schema_final,gcp_schema_sas_final,gcp_partition_cols,
    gcp_cluster_cols,obj_gcs_path,obj_gcs_final_alter_name,int(obj_gcs_stg_to_final_split_flag),
    vw_sql_except_columns,vw_sql_loc,comments
    )
        
        query = "INSERT INTO gcp_airflow_configobjs_mapping (airflow_mapping_id, airflow_binding_id, exec_order, object_id, skip_flag, airflow_control_flag, gcp_schema_initial, gcp_schema_intermmediate, gcp_schema_final, gcp_schema_sas_final, gcp_partition_cols, gcp_cluster_cols, obj_gcs_path, obj_gcs_final_alter_name, obj_gcs_stg_to_final_split_flag, vw_sql_except_columns, vw_sql_loc, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()

        context = {"sub":val}
        return render(request, 'content.html',context)
        
    elif request.method == 'POST' and form_name == 'gcp_configobjs_ingestion_mapping':
        mapping_id = request.POST.get('mapping_id')
        object_id = request.POST.get('object_id')
        source_id = request.POST.get('sourceid')
        skip_flag = request.POST.get('skip_flag')
        
        val = (int(mapping_id),int(object_id),int(source_id),int(skip_flag))
        
        query = "INSERT INTO gcp_configobjs_ingestion_mapping (mapping_id, object_id, sourceid, skip_flag) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()

        context = {"sub":val}
        return render(request, 'content.html',context)
        
    elif request.method == 'POST' and form_name == 'gcp_scheduler_scheduler_trigger':
        trigger_id = request.POST.get('trigger_id')
        group_binding_id = request.POST.get('group_binding_id')
        trigger_group_binding_id = request.POST.get('trigger_group_binding_id')
        exec_order = request.POST.get('exec_order')
        skip_flag = request.POST.get('skip_flag')
        
        val = (int(trigger_id),int(group_binding_id),int(trigger_group_binding_id),int(exec_order),int(skip_flag))
        
        query = "INSERT INTO gcp_scheduler_scheduler_trigger (trigger_id, group_binding_id, trigger_group_binding_id, exec_order, skip_flag) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()

        context = {"sub":val}
        return render(request, 'content.html',context)
        
    elif request.method == 'POST' and form_name == 'airflow_configobjs_dependency':
        linking_id = request.POST.get('linking_id')
        airflow_mapping_id = request.POST.get('airflow_mapping_id')
        dependent_airflow_mapping_id = request.POST.get('dependent_airflow_mapping_id')
        skip_flag = request.POST.get('skip_flag')
        
        val = (int(linking_id),int(airflow_mapping_id),int(dependent_airflow_mapping_id),int(skip_flag))
        
        query = "INSERT INTO gcp_airflow_configobjs_dependency (linking_id, airflow_mapping_id, dependent_airflow_mapping_id, skip_flag) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, val)
        conn.commit()
        conn.close()

        context = {"sub":val}
        return render(request, 'content.html',context)
        
