import data_handler as dat

dataset = dat.open_data()
t850, z850 = dat.extract_data(dataset,850.0)

values = [] * 92

for i in range(92):
    print(i)
    time_frame = dat.get_time(dataset, i)
    values[i] = dat.integrate(time_frame)

print(values)