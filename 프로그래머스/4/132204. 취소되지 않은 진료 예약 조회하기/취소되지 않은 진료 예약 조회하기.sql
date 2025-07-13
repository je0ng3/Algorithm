with a as (
    select apnt_no, pt_no, mcdp_cd, apnt_ymd, mddr_id
    from appointment
    where mcdp_cd like "CS" and apnt_ymd like "2022-04-13%" and apnt_cncl_yn like "N"
)
select APNT_NO, (select PT_NAME
                from patient
                where a.pt_no = patient.pt_no) as PT_NAME,
                PT_NO, MCDP_CD, 
                (select DR_NAME
                from doctor
                 where mddr_id = dr_id
                ) as DR_NAME, 
                APNT_YMD
from a
order by APNT_YMD asc
