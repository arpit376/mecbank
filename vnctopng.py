import pyvnc2swf

# Initialize VncDecoder
decoder = pyvnc2swf.VncDecoder()

# Open a PCAP file containing VNC packets
decoder.open_pcap('vnc_packets.pcap')

# Iterate through packets and decode screen updates
for packet in decoder.packet_generator():
    if packet.has_screen():
        # Render the screen updates and save as an image
        image = packet.get_screen().make_image()
        image.save(f'vnc_image_{packet.timestamp}.png')

# Close the PCAP file
decoder.close_pcap()

