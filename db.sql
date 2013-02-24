SQLite format 3   @     �                                                                        �    !����� �!!�ctableauth_groupauth_groupCREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
)3G! indexsqlite_autoindex_auth_group_1auth_group�99�Utableauth_group_permissionsauth_group_permissionsCREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
)K_9 indexsqlite_autoindex_auth_group_permissions_1auth_group_permissions�++�Stableauth_permissionauth_permissionCREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
)=Q+ indexsqlite_autoindex_auth_permiss            
   
   �    �^:����Z)���yW" � � � P                          / ;1Can change user profilechange_userprofile) 5+Can add user profileadd_userprofile9 E;Can delete fundraising groupdelete_fundraisinggroup9 E;Can change fundraising groupchange_fundraisinggroup3 ?5Can add fundraising groupadd_fundraisinggroup  +#Can delete sitedelete_site  +#Can change sitechange_site %Can add siteadd_site& 1)Can delete sessiondelete_session& 1)Can change sessionchange_session  +#Can add sessionadd_session/ ;1Can delete content typedelete_contenttype/ ;1Can change content typechange_contenttype)
 5+Can add content typeadd_contenttype 	 +#Can delete userdelete_user  +#Can change userchange_user %Can add useradd_user" -%Can delete groupdelete_group" -%Can change groupchange_group 'Can add groupadd_group, 7/Can delete permissiondelete_permission, 7/Can change permissionchange_permission& 1)Can add permissionadd_permi   
   � ������vdR<#
�������bD.�                                                                                                                                                                                                                                                                                                                                                                                                                                                                    1delete_userprofile1change_userprofile+add_userprofile;delete_fundraisinggroup;change_fundraisinggroup5add_fundraisinggroup#delete_site#change_siteadd_site)delete_session)change_session#add_session1delete_contenttype1change_contenttype+add_contenttype
#delete_user	#change_useradd_user%delete_group%change_groupadd_group/delete_permission/change_permission)add_permission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  �  ��$qr��!!�ctable�++�Stableauth_permissionauth_permissionCREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) N�++�Stableauth_permissionauth_permissionCREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
)=Q+ indexsqlite_autoindex_auth_permission_1auth_permission�99�Utableauth_group_permissionsauth_group_permissionsCREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
)K_9 indexsqlite_autoindex_auth_group_permissions_1auth_group_permissions�!!�ctableauth_groupauth_groupCREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
)    Cm��x H H                                                1E indexsqlite_autoindex_auth_user_1auth_user�z	--�'tableauth_user_groupsauth_user_groupsCREATE TABLE "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT 3G! indexsqlite_autoindex_auth_group_1auth_group�'AA�Ytableauth_user_user_permissionsauth_user_user_permissionsCREATE TABLE "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("user_id", "permission_id")
)SgA indexsqlite_autoindex_auth_user_user_permissions_1auth_user_user_permissions	�z	--�'tableauth_user_groupsauth_user_groupsCREATE TABLE "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id"),
    UNIQUE ("user_id", "group_id")
)?
S- indexsqlite_autoindex_auth_user_groups_1auth_user_groups                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 � W�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      � �'AAapbkdf2_sha256$10000$G8s5JJEYQKYg$pf8c0aqGnfyDnlD8GPM/pXZp1ii0azPgd2q2pgNADyk=  2013-02-24 07:23:46.0160002013-02-24 03:37:18.125000�& 3�'AAkzkz2182@columbia.edupbkdf2_sha256$10000$Ad0ngW06d85b$+qvLGFkErrmGUblEjSGyq9wsNeqP4knxUAaxZlG/Fuw=2013-02-24 03:37:00.3840002013-02-24 03:37:00.384000
   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       akz    �  �u��t & &                ;O) indexsqlite_autoindex_django_session_1django_session�33�Ctabledjango_content_typedjango_content_typeCREATE TABLE "d�J�ctableauth_userauth_userCREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "password" varchar(128) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "is_superuser" bool NOT NULL,
    "last_login" datetime NOT NULL,
    "date_joined" datetime NOT NULL
)1E indexsqlite_autoindex_auth_user_1auth_user�33�Ctabledjango_content_typedjango_content_typeCREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
)EY3 indexsqlite_autoindex_django_content_type_1django_content_type    ����r^-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              % %#user profileinternalsuserprofile/ /-fundraising groupinternalsfundraisinggroup sitesitessite sessionsessionssession( %%#content typecontenttypescontenttype userauthuser groupauthgroup !!permissionauthpermission
   U ����oU��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             #internalsuserprofile-internalsfundraisinggroupsitessitesessionssession%#contenttypescontenttypeauthuserauthgroup!authpermission    �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                M�Aae24e�vM�{Aae24e7dd55f192b9a79efd01bd277bb9YzQ5MWIyMDI2NGQ0ZmUxMzA4ODBjN2M5ZWI4NWZhNDE2MzE5MDk1NDqAAn1xAShVEl9hdXRoX3Vz
ZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED
VQ1fYXV0aF91c2VyX2lkcQRLAnUu
2013-03-10 07:23:46.031000
� � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          $Mae24e7dd55f192b9a79efd01bd277bb9   %6da9e76c3967d42bb7caf0e1221e9e42      �� � �                                                                                                                                                                    �JAA�tableinternals_fundraisinggroupinternals_fundraisinggroupCRE�D))�Ctabledjango_sessiondjango_sessionCREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);O) indexsqlite_autoindex_django_session_1django_session�,##�tabledjango_sitedjango_siteCREATE TABLE "django_site" (
    "id" integer NOT NULL PRIMARY KEY,
    "domain" varchar(100) NOT NULL,
    "name" varchar(50) NOT NULL
)�JAA�tableinternals_fundraisinggroupinternals_fundraisinggroupCREATE TABLE "internals_fundraisinggroup" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_name" varchar(50) NOT NULL,
    "fundraiser_name" varchar(50) NOT NULL,
    "current" integer NOT NULL,
    "goal" integer NOT NULL,
    "num_donations" integer NOT NULL
)   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ##example.comexample.com                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       �  ���W                                                                                                                                               �o77�}tableinternals_userprofileinternals_userprofileCREATE TABLE "internals_userprofile" (
    "user_id" integer NOT NULL PRIMARY KEY REFERENCES "auth_user" ("id"),
    "group_id" integer REFERENCES "internals_fundraisinggroup" ("id")
)�=+�-indexauth_permission_1bb8f392auth_permissionCREATE INDEX "auth_permission_1bb8f392" ON "auth_permission" ("content_type_id")�K9�;indexauth_group_permissions_425ae3c4auth_group_permissionsCREATE INDEX "auth_group_permissions_425ae3c4" ON "auth_group_permissions" ("group_id")�K9�Eindexauth_group_permissions_1e014c8fauth_group_permissionsCREATE INDEX "auth_group_permissions_1e014c8f" ON "auth_group_permissions" ("permission_id")�&QA�Gindexauth_user_user_permissions_403f60fauth_user_user_permissionsCREATE INDEX "auth_user_user_permissions_403f60f" ON "auth_user_user_permissions" ("user_id")    P ��|^:����Z)���yW" � � � P                          / ;1Can change user profilechange_userprofile) 5+Can add user profileadd_userprofile9 E;Can delete fundraising groupdelete_fundraisinggroup9 E;Can change fundraising groupchange_fundraisinggroup3 ?5Can add fundraising groupadd_fundraisinggroup  +#Can delete sitedelete_site  +#Can change sitechange_site %Can add siteadd_site& 1)Can delete sessiondelete_session& 1)Can change sessionchange_session  +#Can add sessionadd_session/ ;1Can delete content typedelete_contenttype/ ;1Can change content typechange_contenttype)
 5+Can add content typeadd_contenttype 	 +#Can delete userdelete_user  +#Can change userchange_user %Can add useradd_user" -%Can delete groupdelete_group" -%Can change groupchange_group 'Can add groupadd_group, 7/Can delete permissiondelete_permission, 7/Can change permissionchange_permission& 1)Can add permissionadd_permission   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     / ;1Can delete user profiledelete_userprofile
   p ���������������������|vp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
	
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 5 5�f�h �                                                                                                               |;)�!indexdjango_session_3da3d3d8django_session$CREATE INDEX "django_session_3da3d3d8" ON "django_session" ("expire_date")�?-�#indexauth_user_groups_425ae3c4auth_user_gr�.SA�Uindexauth_user_user_permissions_1e014c8fauth_user_user_permissions CREATE INDEX "auth_user_user_permissions_1e014c8f" ON "auth_user_user_permissions" ("permission_id")~=-�indexauth_user_groups_403f60fauth_user_groups"CREATE INDEX "auth_user_groups_403f60f" ON "auth_user_groups" ("user_id")�?-�#indexauth_user_groups_425ae3c4auth_user_groups#CREATE INDEX "auth_user_groups_425ae3c4" ON "auth_user_groups" ("group_id")|;)�!indexdjango_session_3da3d3d8django_session$CREATE INDEX "django_session_3da3d3d8" ON "django_session" ("expire_date")�I7�7indexinternals_userprofile_425ae3c4internals_userprofile%CREATE INDEX "internals_userprofile_425ae3c4" ON "internals_userprofile" ("group_id")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         >2013-03-10 07:23:45.946000A2013-03-10 07:23:46.031000
   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  