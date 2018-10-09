import argparse
import logging
from core.peer_dbs import Peer_DBS
from core.peer_ims import Peer_IMS

class Peer():
    
    def __init__(self):
        parser.add_argument("-l", "--chunks_before_leave", default=2000, type=int,
                            help="Number of chunk before leave the team")
        parser.add_argument("-s", "--set_of_rules", default="dbs",
                            help="set of rules")
        parser.add_argument("-a", "--splitter_address", default="127.0.1.1",
                            help="Splitter address")
        parser.add_argument("-p", "--splitter_port", default=4550, type=int,
                            help="Splitter port")
        parser.add_argument("-m", "--peer_port", default=0, type=int,
                            help="Peer port (default={})".format(Peer_DBS.peer_port))
        parser.add_argument("--loglevel", default=logging.ERROR, help="Log level")
        print(args)        
        logging.basicConfig(format="%(message)s - %(asctime)s - %(name)s - %(levelname)s")

    def instance(self, args):
        Peer_DBS.peer_port = args.peer_port
        Peer_DBS.splitter_address = args.splitter_address
        Peer_DBS.splitter_port = args.splitter_port
        if args.set_of_rules == "DBS":
            peer = Peer_DBS("P", "Peer_DBS", args.loglevel)
        elif args.set_of_rules == "IMS":
            peer = Peer_IMS("P", "Peer_IMS", args.loglevel)
        
    def run(self):
        peer.chunks_before_leave = args.chunks_before_leave
        peer.set_splitter((args.splitter_address, args.splitter_port))
        peer.connect_to_the_splitter(0)
        peer.receive_public_endpoint()
        peer.receive_buffer_size()
        peer.receive_the_number_of_peers()
        peer.listen_to_the_team()
        peer.receive_the_list_of_peers()
        peer.send_ready_for_receiving_chunks()
        peer.send_peer_type()   # Only for simulation purpose
        peer.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    peer = Peer(parser)
    args = parser.parse_args()
    peer.instance(args)
    peer.run(args)


 
