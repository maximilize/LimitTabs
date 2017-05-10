import sublime
import sublime_plugin
import os
import time


class LimitTabsCommand(sublime_plugin.WindowCommand):

    def run(self):
        default_settings = sublime.load_settings("LimitTabs.sublime-settings")
        settings = self.window.active_view().settings()

        def get_setting(key, default):
            value = default_settings.get(key)
            if not value:
                value = default
            return settings.get(key, value)

        modified_duration = get_setting('limittabs_modified_duration', 1800)
        accessed_duration = get_setting('limittabs_accessed_duration', 60)
        threshold = get_setting('limittabs_threshold', 0)
        keep_open = get_setting('limittabs_keep_open', 0)

        now = time.time()
        active = self.window.active_view();
        candidates = []

        for x in range(0, self.window.num_groups()):

            windows_in_group = self.window.views_in_group(x)

            if len(windows_in_group) < threshold:
                continue

            to_close = len(windows_in_group) - keep_open
            if to_close <= 0:
                continue

            active_in_group = self.window.active_view_in_group(x)

            for file in windows_in_group:

                path = file.file_name()

                if file == active_in_group:
                    continue
                if not path:
                    continue
                if not os.path.exists(path):
                    continue

                mtime = os.path.getmtime(path)
                if now - mtime < modified_duration:
                    continue

                atime = os.path.getatime(path)
                if now - atime < accessed_duration:
                    continue

                if file.is_dirty():
                    continue
                if file.is_scratch():
                    continue

                candidates.append((max(atime, mtime), file))

            candidates = list(sorted(candidates, key=lambda x: x[0]))
            for i in range(min(len(candidates), to_close)):
                self.window.focus_view(candidates[i][1])
                self.window.run_command('close_file')

            self.window.focus_view(active)


class LimitTabsListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        run_on_post_save = sublime.load_settings("LimitTabs.sublime-settings").get('limittabs_run_on_post_save')
        if not run_on_post_save:
            return
        view.window().run_command("limit_tabs")
