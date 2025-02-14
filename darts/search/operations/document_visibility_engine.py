class DocumentVisibilityEngine:

    def call(self, user_role, case_ids = None, region_ids = None):
        match user_role:
            case 'superuser' | 'tech':
                return 'show'
            case 'staff':
                return { 'case_ids': case_ids }
            case 'regional':
                return { 'region_ids': region_ids }
            case _:
                return 'hide'
