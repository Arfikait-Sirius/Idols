LABEL_GIRLS_NAME = "[GIRLS-NAME]: "
LABEL_TARGET = "[    TARGET]: "
LABEL_JUDGE = "[     JUDGE]: "
LABEL_PRINT = "[     PRINT]: "
LABEL_RESULT = "[    RESULT]: "

#------------------------
# :[ NAME ]:
#     fn_set_girl_name
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_set_girl_name( name: str ) -> None:

     print( f"{LABEL_GIRLS_NAME}{name}" )

     return

#------------------------
# :[ NAME ]:
#     fn_set_skill_name
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_set_skill_name( target: str ) -> None:

     print( f"{LABEL_TARGET}{target}()" )

     return

#------------------------
# :[ NAME ]:
#     fn_judge
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_judge( judgement: bool ) -> None:

     if( judgement ):
          print( f"{LABEL_JUDGE}OK" )
     else:
          print( f"{LABEL_TARGET}NG - Please check this source." )

     return

#------------------------
# :[ NAME ]:
#     fn_disp_result
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_disp_result( result: bool ) -> None:

     if( result ):
          print( f"{LABEL_RESULT}{girl_name} = OK." )
     else:
          print( f"{LABEL_RESULT}{girl_name} = NG." )

     return

#------------------------
# :[ NAME ]:
#     fn_print
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_print( result: str ) -> None:

     print( f"{LABEL_PRINT}{result}" )

     return
