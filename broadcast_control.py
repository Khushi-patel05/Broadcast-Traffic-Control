from pox.core import core
import pox.openflow.libopenflow_01 as of
log=core.getLogger()
BROADCAST="ff:ff:ff:ff:ff:ff"
LIMIT=20
broadcast_count={}
def _handle_PacketIn(event):
    packet=event.parsed
    dpid=event.dpid
    if not packet.parsed:
       return
    src=str(packet.src)
    dst=str(packet.dst)
    if dpid not in broadcast_count:
       broadcast_count[dpid]=0
    if packet.find('arp'):
       log.info(f"[Switch {dpid}] ARP packet allowed")
       if str(packet.dst)==BROADCAST:
          broadcast_count[dpid]+=1
          log.info(f"[Switch {dpid}] Broadcast packet detected ({broadcast_count[dpid]})")
          if broadcast_count[dpid] > LIMIT:
             log.warning(f"[Switch {dpid}] Broadcast limit exceeded.Dropping Packeeeet.")
             return
       install_flow(event,packet)
       flood(event)
       return 
    if dst==BROADCAST:
       broadcast_count[dpid]+=1
       log.info(f"[Switch {dpid}] Broadcast packet detected ({broadcast_count[dpid]})")
       if broadcast_count[dpid]>LIMIT:
          log.warning(f"[Switch {dpid}] Broadcast limit exceeded.Dropping PAcket.")
          return
    install_flow(event,packet)
    flood(event)
def flood(event): 
    msg=of.ofp_packet_out()
    msg.data=event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)
def install_flow(event,packet):
    msg=of.ofp_flow_mod()
    msg.match=of.ofp_match.from_packet(packet)
    msg.idle_timeout=30
    msg.hard_timeout=60
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)
def launch():
    core.openflow.addListenerByName("PacketIn",_handle_PacketIn)
    log.info("Broadcast Traffic Control Controller Started")
