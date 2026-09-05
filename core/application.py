
import pickle
import json
import os
import shutil

from core.utils import error

class Application():
    def __init__(
            self,
            name: str = "new-project",
            author: str = "anonymous"
        ):

        self.name = name
        self.sanitized_name = ""

        self.author = author

        self.sanitize()

    def sanitize(self):
        self.sanitized_name = self.name.lower()
        self.sanitized_name = self.sanitized_name.replace(" ","-")

        for banned_char in "<>:;/\\|?*":
            self.sanitized_name = self.sanitized_name.replace(banned_char,"")
    
    def build(self):
        build_directory = os.path.join(
            "build",
            self.sanitized_name
        )

        if not ( self.sanitized_name in os.listdir("build") ):
            os.mkdir( build_directory )


        self.build_backend(build_directory)
        self.build_frontend(build_directory)

    def replace_template_content(self,file_path:str):
        value_links = {}
        complex_links = {}

        for key,value in self.__dict__.items():
            value_links[f"%PROJECT_{key.upper()}%"] = value
        
        template_content = open(file_path,"r").read()
        
        for key,value in value_links.items():
            template_content = template_content.replace(key,value)

        open(file_path,"w").write(template_content)

    def build_backend(self,build_directory:str):
        file_path = shutil.copy(
            os.path.join(
                "templates",
                "main.py"
            ),
            build_directory
        )

        self.replace_template_content(file_path)

    def build_frontend(self,build_directory:str):
        pass

    def store(self):

        ### Checks for creation ###

        project_directory = os.path.join(
            "projects",
            self.sanitized_name
        )

        if not ( self.sanitized_name in os.listdir("projects") ):
            os.mkdir( project_directory )
        
        if "project.json" in os.listdir( project_directory ):
            error("Existing project detected! Aboritng creation..."); return

        ### Creation occurs ###

        project_data_file = open(
            os.path.join(project_directory,"project.json"),
            "w"
        )

        project_descriptor_file = open(
            os.path.join(project_directory,"project-descriptor.pickle"),
            "wb"
        )

        json.dump(
            {
                "name":self.name,
                "author":self.author
            },
            project_data_file,
            indent=3
        )

        pickle.dump(self,project_descriptor_file)

        project_data_file.close()
        project_descriptor_file.close()

        ### Checks finishes ###

        return

    def load(project_directory) -> Application:
        project_descriptor_file = open(
            os.path.join(project_directory,"project-descriptor.pickle"),
            "rb"
        )

        app = pickle.load(project_descriptor_file)

        return app


