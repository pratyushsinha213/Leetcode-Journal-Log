class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(" ")
        months = {
            "Jan": '01', 
            "Feb": '02',
            "Mar": '03', 
            "Apr": '04', 
            "May": '05', 
            "Jun": '06', 
            "Jul": '07', 
            "Aug": '08', 
            "Sep": '09', 
            "Oct": '10', 
            "Nov": '11', 
            "Dec": '12'
        }
        num_date = ""
        for num in day:
            if num.isnumeric():
                num_date += num
        if int(num_date) < 10:
            num_date = '0'+ num_date
        
        builder = f"{year}-{months[month]}-{num_date}"

        return builder