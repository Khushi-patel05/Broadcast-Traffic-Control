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
<img width="358" height="132" alt="Screenshot 2026-04-16 205104" src="https://github.com/user-attachments/assets/7b39a6be-b8dc-4876-9c14-abc0022df2c7" />


### 🔹 ARP and Broadcast Detection
<img width="580" height="254" alt="Screenshot 2026-04-16 205133" src="https://github.com/user-attachments/assets/66d4964e-3f5b-4643-b7f5-65170aa5fc2c" />


### 🔹 Controller Logs
<img width="637" height="327" alt="Screenshot 2026-04-16 205150" src="https://github.com/user-attachments/assets/7161ec02-b868-40f9-a488-b9915c41b448" />


### 🔹 ARP Testing
<img width="686" height="237" alt="Screenshot 2026-04-16 205224" src="https://github.com/user-attachments/assets/5cf9bb22-f6b0-431e-a390-ca5f4d390739" />


### 🔹 Broadcast Behavior
<img width="714" height="201" alt="Screenshot 2026-04-16 205432" src="https://github.com/user-attachments/assets/270908a2-9aaf-495f-bb6e-ad248c31fde8" />


### 🔹 Flow Table
<img width="730" height="94" alt="Screenshot 2026-04-16 205508" src="https://github.com/user-attachments/assets/a72fe3f4-713c-4296-a7d3-53df649e23aa" />


### 🔹 iperf Result
<img width="546" height="75" alt="Screenshot 2026-04-16 205544" src="https://github.com/user-attachments/assets/77c5acc8-7663-426d-b863-eee417cd9527" />


### 🔹 Wireshark Capture
<img width="963" height="651" alt="Screenshot 2026-04-16 205735" src="https://github.com/user-attachments/assets/87fcb049-f21c-486b-bf64-eb451b1cfb16" />


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
