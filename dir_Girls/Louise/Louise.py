#------------------------
# :[ NAME ]:
#     fn_count
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_count( base: str, target: str ) -> int:
     return base.count( target )

#------------------------
# :[ NAME ]:
#     fn_copy
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_copy( base: str ) -> str:
     return base

#------------------------
# :[ NAME ]:
#     fn_replace
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_replace( base: str, target: str, replacement: str ) -> str:
     return base.replace( target, replacement )

#------------------------
# :[ NAME ]:
#     fn_split
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_split( base: str, splitter: str, position: int ) -> str:
     list = base.split( splitter )
     return list[position]

#------------------------
# :[ NAME ]:
#     fn_upper_all
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_upper_all( base: str ) -> str:
     return base.upper()

#------------------------
# :[ NAME ]:
#     fn_lower_all
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_lower_all( base: str ) -> str:
     return base.lower()

#------------------------
# :[ NAME ]:
#     fn_upper_first
#
# :[ CATEGORY ]:
#     Skill
#------------------------
def fn_upper_first( base: str ) -> str:
     base_upper: str = base.upper()[0]
     base_lower: str = base.lower()[1 : len(base)]

     return base_upper + base_lower
