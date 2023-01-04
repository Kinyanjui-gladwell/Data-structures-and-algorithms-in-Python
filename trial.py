column_names = ['member_no', 'start_date', 'end_date']
default_fields = {'member_no':None, 'start_date':None, 'end_date':None}
# column_names[0]=default_fields['member_no']
# print(column_names)
column_names = [None if (i=='member_no') | (i=='start_date') | (i=='end_date') else i for i in column_names]
print(column_names)