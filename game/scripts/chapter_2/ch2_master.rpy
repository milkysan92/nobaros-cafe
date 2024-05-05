# Chapter 2 master script; the main situation logic belongs here; there should be no dialogue lines
label ch2_master:
    call cafe_intro from _call_cafe_intro
    call report_to_ingram from _call_report_to_ingram
    return