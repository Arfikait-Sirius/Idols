LABEL_GIRLS_NAME = "[GIRLS-NAME]: "
LABEL_TARGET = "[    TARGET]: "
LABEL_JUDGE = "[     JUDGE]: "
LABEL_PRINT = "[     PRINT]: "

skill_name = ""

#------------------------
# :[ NAME ]:
#     fn_set_girl_name
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_set_girl_name( girl_name: str ) -> None:
     print( f"{LABEL_GIRLS_NAME}{girl_name}" )

     return

#------------------------
# :[ NAME ]:
#     fn_set_skill_name
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_set_skill_name( target: str ) -> None:
     skill_name = target
     print( f"{LABEL_TARGET}{skill_name}()" )

     return

#------------------------
# :[ NAME ]:
#     fn_judge
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_judge( judgement: bool ) -> None:

     if ( judgement ):
          print( f"{LABEL_JUDGE}OK" )
     else:
          print( f"{LABEL_TARGET}NG - Please check {skill_name}" )

     return