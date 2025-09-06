import datetime

#------------------------
# :[ NAME ]:
#     fn_get_date
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_get_date( format_string: str ) -> str:
     s = format_string.replace( "YYYY", "%Y" )
     s = s.replace( "MM", "%m" )
     s = s.replace( "DD", "%d" )

     return str( datetime.date.today().strftime( s ) )
