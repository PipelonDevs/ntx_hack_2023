import socket

def main():
    print("Unicorn Frequency Band UDP Receiver Example")
    print("-------------------------------------------")
    print()

    try:
        # Create a file to store data.
        DataFile = "immersiveDataChannels.csv";
        file = open("Datasets/"+DataFile, "wb")

        # Define an IP endpoint
        destination_port = 1000
        ip = "127.0.0.1"
        end_point = (ip, destination_port)
        print(f"Listening on port '{destination_port}'...")

        # Initialize UDP socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(end_point)
        receive_buffer_byte = bytearray(1024)

        # Acquisition loop
        while True:
            number_of_bytes_received, _ = udp_socket.recvfrom_into(receive_buffer_byte)
            if number_of_bytes_received > 0:
                message_byte = receive_buffer_byte[:number_of_bytes_received]
                message = message_byte.decode("ascii")
                file.write(message_byte)
                print(message, end="")
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        print("Press ENTER to terminate the application.")
        file.close()
        input()

if __name__ == "__main__":
    main()
