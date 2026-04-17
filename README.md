# 📡 Broadcast Traffic Control using SDN (POX + Mininet)

---

## 📖 Overview

This project demonstrates how **Software Defined Networking (SDN)** can be used to monitor and control broadcast traffic in a network. Excessive broadcast traffic can lead to **broadcast storms**, degrading network performance.

Using a **POX controller** and **OpenFlow rules**, this system detects, limits, and controls broadcast packets dynamically.

---

## 🎯 Objectives

* Monitor network traffic using SDN controller
* Detect broadcast packets in real-time
* Limit broadcast traffic using threshold-based control
* Prevent broadcast storm scenarios
* Implement OpenFlow-based flow rules

---

## 🛠️ Technologies Used

* **Mininet** – Network emulation
* **POX Controller** – SDN controller
* **OpenFlow Protocol** – Flow rule management
* **Wireshark** – Packet analysis
* **iperf** – Network performance testing

---

## ⚙️ System Architecture

* Mininet creates a virtual network (hosts + switch)
* POX controller manages switch behavior
* Switch sends `PacketIn` events to controller
* Controller applies logic:

  * Allows ARP traffic
  * Detects broadcast packets
  * Counts packets per switch
  * Drops packets after threshold
  * Installs flow rules using OpenFlow

---

## 🚀 Features

* Handles `PacketIn` events dynamically
* Implements **match-action logic**
* Uses **OpenFlow flow rules (`ofp_flow_mod`)**
* Detects broadcast MAC (`ff:ff:ff:ff:ff:ff`)
* Applies broadcast threshold (**LIMIT = 20 packets**)
* Prevents network congestion

---

## ▶️ Setup Instructions

### 🔹 Step 1: Run POX Controller

```bash
cd ~/pox
./pox.py misc.broadcast_control
```

---

### 🔹 Step 2: Start Mininet

```bash
sudo mn --topo single,3 --controller remote
```

---

## 🧪 Test Scenarios

### ✅ Scenario 1: Normal Traffic

```bash
h1 ping h2
```

✔ Successful communication between hosts (0% packet loss)

---

### ✅ Scenario 2: ARP Broadcast Detection

```bash
h1 arping 10.0.0.2
```

✔ ARP packets allowed
✔ Broadcast packets detected by controller

---

### ✅ Scenario 3: Broadcast Limit Enforcement

```bash
h1 arping 10.0.0.2
```

✔ Broadcast packets counted
✔ After threshold → packets are restricted by controller

---

## 📊 Proof of Execution

### 🔹 Flow Table Verification

```bash
sh ovs-ofctl dump-flows s1
```

✔ Shows OpenFlow rules installed in switch

---

### 🔹 Wireshark Analysis

* ARP packets captured
* Broadcast MAC observed:

```
ff:ff:ff:ff:ff:ff
```

✔ Confirms Layer-2 broadcast traffic

---

### 🔹 iperf Testing

```bash
h2 iperf -s
h1 iperf -c h2
```

✔ Demonstrates network throughput and performance

---

## 📸 Screenshots

### 🔹 Network Connectivity

<img width="600" src="https://github.com/user-attachments/assets/7b39a6be-b8dc-4876-9c14-abc0022df2c7" />
<br>Successful ping between hosts with no packet loss.

---

### 🔹 ARP and Broadcast Detection

<img width="600" src="https://github.com/user-attachments/assets/66d4964e-3f5b-4643-b7f5-65170aa5fc2c" />
<br>Controller detects ARP and broadcast packets.

---

### 🔹 Controller Logs

<img width="600" src="https://github.com/user-attachments/assets/7161ec02-b868-40f9-a488-b9915c41b448" />
<br>Logs showing ARP allowed and broadcast packet count.

---

### 🔹 ARP Testing

<img width="600" src="https://github.com/user-attachments/assets/5cf9bb22-f6b0-431e-a390-ca5f4d390739" />
<br>ARP communication between hosts.

---

### 🔹 Broadcast Behavior

<img width="600" src="https://github.com/user-attachments/assets/270908a2-9aaf-495f-bb6e-ad248c31fde8" />
<br>Broadcast packets being generated and monitored.

---

### 🔹 Flow Table

<img width="600" src="https://github.com/user-attachments/assets/a72fe3f4-713c-4296-a7d3-53df649e23aa" />
<br>Installed OpenFlow rules inside the switch.

---

### 🔹 iperf Result

<img width="600" src="https://github.com/user-attachments/assets/77c5acc8-7663-426d-b863-eee417cd9527" />
<br>Bandwidth measurement between hosts.

---

### 🔹 Wireshark Capture

<img width="600" src="https://github.com/user-attachments/assets/87fcb049-f21c-486b-bf64-eb451b1cfb16" />
<br>Packet-level analysis showing broadcast MAC address.

---

## 📌 Expected Output

* Broadcast packets are detected and counted
* After threshold, packets are controlled/dropped
* Flow rules are installed in switch
* Network performance remains stable

---

## 🧠 Conclusion

This project demonstrates how SDN enables **centralized and intelligent control** over network behavior. By implementing broadcast traffic control using POX and OpenFlow, we successfully reduce unnecessary broadcast traffic and improve overall network efficiency.

---

## 👩‍💻 Author

**Khushi Patel**
