from django.contrib import admin

# Register your models here.


import os
import json
import tempfile
import subprocess
from django.contrib import admin
from django.utils.text import slugify
from django.conf import settings
from .models import Ailment
from django.core.serializers.json import DjangoJSONEncoder


@admin.register(Ailment)
class AilmentAdmin(admin.ModelAdmin):
    actions = ["export_and_create_pr"]

    def export_ailment_data_dict(self, ailment):
        return {
            "id": ailment.id,
            "name": ailment.name,
            "description": ailment.description,
        }

    def export_and_create_pr(self, request, queryset):
        github_token = "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"
        repo_name = "aalishgadhiya/Django_learning"
        # base_branch = "develop"
        branch_name = "master"
        export_folder_rel = "ailment/fixtures/ailments"

        tmp_dir = tempfile.mkdtemp()
        repo_path = os.path.join(tmp_dir, "repo")

        subprocess.run([
            "git", "clone", f"https://{github_token}@github.com/{repo_name}.git", repo_path
        ], check=True)

        subprocess.run(["git", "checkout", branch_name], cwd=repo_path, check=True)

        export_folder = os.path.join(repo_path, export_folder_rel)
        os.makedirs(export_folder, exist_ok=True)

        for ailment in queryset:
            data = self.export_ailment_data_dict(ailment)
            filename = f"{slugify(ailment.name)}_{ailment.id}.json"
            file_path = os.path.join(export_folder, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, cls=DjangoJSONEncoder, indent=4)

        subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
        subprocess.run(["git", "commit", "-m", "Auto-export ailments data"], cwd=repo_path, check=True)
        subprocess.run(["git", "push", "origin", branch_name], cwd=repo_path, check=True)

        self.message_user(request, f"Exported and pushed branch: {branch_name}")
