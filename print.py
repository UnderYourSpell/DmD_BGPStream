import pybgpstream

# Set the start and end times for your stream
start_time = "2023-10-14 21:03:00 UTC"
end_time = "2023-10-14 21:10:00 UTC"

stream = pybgpstream.BGPStream(
    from_time=start_time,
    until_time=end_time,
    collectors=["route-views.sg", "route-views.eqix"],
    record_type="updates",
    filter="peer 11666 and prefix more 210.180.0.0/16"
)

for elem in stream:
    # record fields can be accessed directly from elem
    # e.g. elem.time
    # or via elem.record
    # e.g. elem.record.time
    print(elem)
