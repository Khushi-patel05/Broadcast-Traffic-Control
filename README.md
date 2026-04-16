# 📡 Broadcast Traffic Control using SDN (POX + Mininet)

## 📖 Overview

This project demonstrates how Software Defined Networking (SDN) can be used to monitor and control broadcast traffic in a network. Excessive broadcast traffic can lead to broadcast storms, degrading network performance. Using a POX controller and OpenFlow rules, this system detects, limits, and drops excessive broadcast packets.

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
  * Drops packets after threshold
  * Installs flow rules using OpenFlow

---

## 🚀 Features

* Handles `PacketIn` events dynamically
* Implements **match-action logic**
* Uses **OpenFlow flow rules (ofp_flow_mod)**
* Detects broadcast MAC (`ff:ff:ff:ff:ff:ff`)
* Applies **broadcast threshold limit**
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

✔ Expected: Successful communication between hosts

---

### ✅ Scenario 2: ARP Broadcast Detection

```bash
h1 arping 10.0.0.2
```

✔ Expected:

* ARP packets allowed
* Broadcast detected

---

### ✅ Scenario 3: Broadcast Limit Enforcement

```bash
h1 arping 10.0.0.2
```

✔ Expected:

* Broadcast packets counted
* After threshold → packets dropped

---

## 📊 Proof of Execution

### 🔹 Flow Table

```bash
sh ovs-ofctl dump-flows s1
```

✔ Shows installed OpenFlow rules

---

### 🔹 Wireshark Analysis

* ARP packets captured
* Broadcast MAC address detected:

```
ff:ff:ff:ff:ff:ff
```

---

### 🔹 iperf Testing

```bash
h2 iperf -s
h1 iperf -c h2
```

✔ Demonstrates network throughput

---

## 📸 Screenshots

### 🔹 Network Connectivity
![Ping](asset/Screenshot%202026-04-16%20205104.png)

### 🔹 ARP and Broadcast Detection
![ARP](asset/Screenshot%202026-04-16%20205133.png)

### 🔹 Controller Logs
![Logs](asset/Screenshot%202026-04-16%20205150.png)

### 🔹 ARP Testing
![ARP Test](asset/Screenshot%202026-04-16%20205224.png)

### 🔹 Broadcast Behavior
![Broadcast](asset/Screenshot%202026-04-16%20205432.png)

### 🔹 Flow Table
![Flow](asset/Screenshot%202026-04-16%20205508.png)

### 🔹 iperf Result
![iperf](asset/Screenshot%202026-04-16%20205544.png)

### 🔹 Wireshark Capture
![Wireshark](asset/Screenshot%202026-04-16%20205735.png)

---

## 📌 Expected Output

* Broadcast packets are detected and counted
* Excess packets are dropped after threshold
* Flow rules are installed in switch
* Network remains stable

---

## 🧠 Conclusion

This project shows how SDN enables centralized control over network behavior. By implementing broadcast traffic control using POX and OpenFlow, we successfully prevent broadcast storms and improve network efficiency.

---

## 👩‍💻 Author

* Khushi Patel
