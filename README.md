# Django
Django Project

<!DOCTYPE html>
<html>
    <head><title>Analytic HUB</title></head>
    <body>
        <style>
            table,tr,th, td{
                border: 1px solid black;
                border-collapse: collapse;
                text-align: center;
                padding: 5px;
                font-size: small;
            }
            h2{
                text-align: center;
            }
            #topic_title{
                justify-content: center; 
                align-items: center; 
                margin-bottom: 3%;
            }
            #head{
                border: none;
            }

            tr:nth-child(even) {
                background-color: #92f559;
                font-weight: bold;
              }
        </style>
        <div>
            <h2>Analystics Hub Subscription Info</h2>
        </div>
        <div id="topic_title">
            <table id="head">
                <tr id="head">
                    <th id="head">Subject Area   :</th>
                    <td id="head">DMS customer</td>
                </tr>
            </table>
            <br>
            <table id="head">
                <tr id="head">
                    <th id="head">Analytics Hub Source Dataset Name   :</th>
                    <td id="head">pgc_analytics_dms_customer</td>
                </tr>
            </table>
        </div>


        <div>
            <table>
                <tr>
                    <th>Name</th>
                    <td>Efforted_customer_tdmefcu</td>
                    <th>Description</th>
                    <td>efforted : efforted customer</td>
                    <th>PrimaryKey</th>
                    <td>cust_part_seq_no, cust_id, lob_cd, effort_id, effort_type_cd, effort_dt</td>
                </tr>
            </table>
            <table>
                <tr>
                    <th rowspan="3">1</th>
                </tr>

                  <tr>
                    <th>source system</th>
                    <th>SourceLanding</th>
                    <th>Frequency</th>
                    <th>RefershTime</th>
                    <th>AvgTime</th>
                    <th>AvgRecordVolume</th>
                    <th>AvgDataSize</th>
                    <th>DataRetention</th>
                    <th>PartitionColumn</th>
                    <th>ClussteringColumn</th>
                    <th>Support</th>
                    <th>Status</th>
                  </tr>
                  <tr>
                    <td>db2</td>
                    <td>hdl/sftp</td>
                    <td>daily/hourly</td>
                    <td>9am est Hours</td>
                    <td>5678</td>
                    <td>456.56</td>
                    <td>5yrs on effort_dt</td>
                    <td>effort_dt</td>
                    <td>cust_id</td>
                    <td>cust_id</td>
                    <td>Bigdata_support@pch.com</td>
                    <td>active</td>
                  </tr>
                
            </table>
                  
        </div>
        
    </body>
</html>
