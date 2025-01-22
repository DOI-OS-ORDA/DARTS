class DocumentVisibilityEngine:

    def call(self, user_role, case_ids = None, region_ids = None):
        match user_role:
            case 'superuser' | 'tech_support':
                return { 'public' : 'show' , 'private' : 'show' }
            case 'staff':
                return { 'public' : 'show' , 'private' : { 'case_ids': case_ids } }
            case 'regional_coordinator':
                return { 'public' : 'show' , 'private' : { 'region_ids': region_ids } }
            case _:
                return { 'public' : 'show' , 'private' : 'hide' }
