# -*- coding: utf-8 -*-
import socket
import struct


# IP报文解析器
class IPParser(object):
    IP_HEADER_LENGTH = 20

    @classmethod
    def parse_ip_header(cls, ip_header):
        """
        IP 报文格式
        1. 4位IP-Version  4位IP头长度  8位服务类型  16位总长度
        2. 16位标识符  3位标记位  3位片偏移
        3. 8位TTL  8位协议  16位IP头部校验和
        4. 32位源IP地址
        5. 32位目的IP地址
        """
        # 第一行
        line1 = struct.unpack('>BBH', ip_header[:4])
        # eg: 11110000 => 1111
        ip_version = line1[0] >> 4
        # eg: 11111111 & 00001111 => 00001111
        iph_length = line1[0] & 15 * 4
        packet_length = line1[2]
        # 第三行
        line3 = struct.unpack('>BBH', ip_header[8:12])
        ttl = line3[0]
        protocol = line3[1]
        iph_checksum = line3[2]
        # 第四行
        line4 = struct.unpack('>4s', ip_header[12:16])
        src_ip = socket.inet_ntoa(line4[0])
        # 第五行
        line5 = struct.unpack('>4s', ip_header[16:20])
        dst_ip = socket.inet_ntoa(line5[0])
        return {
            "ip_version": ip_version,
            "iph_length": iph_length,
            "packet_length": packet_length,
            "TTL": ttl,
            "protocol": protocol,
            "iph_checksum": iph_checksum,
            "src_ip": src_ip,
            "dst_ip": dst_ip,
        }

    @classmethod
    def parse(cls, packet):
        ip_header = packet[:cls.IP_HEADER_LENGTH]
        return cls.parse_ip_header(ip_header)
