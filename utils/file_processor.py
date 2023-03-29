from analysis.models import Analysis


class FileProcessor:
    def __init__(self, form, user):
        self.form = form
        self.user = user
        self.read_lines()

    def read_lines(self):
        lines = self.form.cleaned_data['log_file']
        result_dict = ""

        for line in lines:

            decoded_line = line.decode()
            if len(decoded_line) != 0:
                if decoded_line[0:3] == '---' and decoded_line[:2] == '--':
                    record = self.create_instance()
                    marker = decoded_line.split("-")
                    sec = marker[6]
                    record.section = sec
                    record.log_id = marker[3]
                else:
                    result_dict += decoded_line

                record.description = result_dict

                record.save()

    def create_instance(self):
        new_record = Analysis()
        new_record.title = self.form.cleaned_data['title']
        new_record.log_file = self.form.cleaned_data['log_file']
        new_record.user = self.user

        return new_record
