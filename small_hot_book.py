from urllib import parse
from functools import reduce
from operator import add

__apk_version__ = '6.68.1'


def bytes_to_int32(t):
    return [int.from_bytes(t[i * 4:(i + 1) * 4], byteorder='little') for i in range(len(t) // 4)]


def int32_to_bytes(t):
    return reduce(add, [bytearray((t % 2 ** 32).to_bytes(4, byteorder='little')) for t in t])


def byte_n(t, n):
    return bytearray(t.to_bytes(4, byteorder='little'))[n]


def read_int16(t):
    return int.from_bytes(t[:2], byteorder='little')


def read_int32(t):
    return int.from_bytes(t[:4], byteorder='little')


data_a798 = bytearray('0123456789abcdef', encoding='utf-8')


def make_ctx():
    return [
        bytearray(
            [210, 114, 133, 81, 135, 119, 113, 117, 218, 172, 249, 219, 5, 227, 99, 34, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 164, 106, 215,
             86, 183, 199, 232, 219, 112, 32, 36, 238, 206, 189, 193, 175, 15, 124, 245, 42, 198, 135, 71, 19, 70, 48,
             168, 1, 149, 70, 253, 216, 152, 128, 105, 175, 247, 68, 139, 177, 91, 255, 255, 190, 215, 92, 137, 34, 17,
             144, 107, 147, 113, 152, 253, 142, 67, 121, 166, 33, 8, 180, 73, 98, 37, 30, 246, 64, 179, 64, 192, 81, 90,
             94, 38, 170, 199, 182, 233, 93, 16, 47, 214, 83, 20, 68, 2, 129, 230, 161, 216, 200, 251, 211, 231, 230,
             205, 225, 33, 214, 7, 55, 195, 135, 13, 213, 244, 237, 20, 90, 69, 5, 233, 227, 169, 248, 163, 239, 252,
             217, 2, 111, 103, 138, 76, 42, 141, 66, 57, 250, 255, 129, 246, 113, 135, 34, 97, 157, 109, 12, 56, 229,
             253, 68, 234, 190, 164, 169, 207, 222, 75, 96, 75, 187, 246, 112, 188, 191, 190, 198, 126, 155, 40, 250,
             39, 161, 234, 133, 48, 239, 212, 5, 29, 136, 4, 57, 208, 212, 217, 229, 153, 219, 230, 248, 124, 162, 31,
             101, 86, 172, 196, 68, 34, 41, 244, 151, 255, 42, 67, 167, 35, 148, 171, 57, 160, 147, 252, 195, 89, 91,
             101, 146, 204, 12, 143, 125, 244, 239, 255, 209, 93, 132, 133, 79, 126, 168, 111, 224, 230, 44, 254, 20,
             67, 1, 163, 161, 17, 8, 78, 130, 126, 83, 247, 53, 242, 58, 189, 187, 210, 215, 42, 145, 211, 134, 235, 0,
             0, 0, 0]),
        bytearray(
            [210, 114, 133, 81, 135, 119, 113, 117, 218, 172, 249, 219, 5, 227, 99, 34, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 164, 106, 215,
             86, 183, 199, 232, 219, 112, 32, 36, 238, 206, 189, 193, 175, 15, 124, 245, 42, 198, 135, 71, 19, 70, 48,
             168, 1, 149, 70, 253, 216, 152, 128, 105, 175, 247, 68, 139, 177, 91, 255, 255, 190, 215, 92, 137, 34, 17,
             144, 107, 147, 113, 152, 253, 142, 67, 121, 166, 33, 8, 180, 73, 98, 37, 30, 246, 64, 179, 64, 192, 81, 90,
             94, 38, 170, 199, 182, 233, 93, 16, 47, 214, 83, 20, 68, 2, 129, 230, 161, 216, 200, 251, 211, 231, 230,
             205, 225, 33, 214, 7, 55, 195, 135, 13, 213, 244, 237, 20, 90, 69, 5, 233, 227, 169, 248, 163, 239, 252,
             217, 2, 111, 103, 138, 76, 42, 141, 66, 57, 250, 255, 129, 246, 113, 135, 34, 97, 157, 109, 12, 56, 229,
             253, 68, 234, 190, 164, 169, 207, 222, 75, 96, 75, 187, 246, 112, 188, 191, 190, 198, 126, 155, 40, 250,
             39, 161, 234, 133, 48, 239, 212, 5, 29, 136, 4, 57, 208, 212, 217, 229, 153, 219, 230, 248, 124, 162, 31,
             101, 86, 172, 196, 68, 34, 41, 244, 151, 255, 42, 67, 167, 35, 148, 171, 57, 160, 147, 252, 195, 89, 91,
             101, 146, 204, 12, 143, 125, 244, 239, 255, 209, 93, 132, 133, 79, 126, 168, 111, 224, 230, 44, 254, 20,
             67, 1, 163, 161, 17, 8, 78, 130, 126, 83, 247, 53, 242, 58, 189, 187, 210, 215, 42, 145, 211, 134, 235, 0,
             0, 0, 0]),
        bytearray(
            [38, 166, 106, 172, 243, 217, 172, 116, 161, 74, 188, 42, 118, 102, 91, 161, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 164, 106,
             215, 86, 183, 199, 232, 219, 112, 32, 36, 238, 206, 189, 193, 175, 15, 124, 245, 42, 198, 135, 71, 19, 70,
             48, 168, 1, 149, 70, 253, 216, 152, 128, 105, 175, 247, 68, 139, 177, 91, 255, 255, 190, 215, 92, 137, 34,
             17, 144, 107, 147, 113, 152, 253, 142, 67, 121, 166, 33, 8, 180, 73, 98, 37, 30, 246, 64, 179, 64, 192, 81,
             90, 94, 38, 170, 199, 182, 233, 93, 16, 47, 214, 83, 20, 68, 2, 129, 230, 161, 216, 200, 251, 211, 231,
             230, 205, 225, 33, 214, 7, 55, 195, 135, 13, 213, 244, 237, 20, 90, 69, 5, 233, 227, 169, 248, 163, 239,
             252, 217, 2, 111, 103, 138, 76, 42, 141, 66, 57, 250, 255, 129, 246, 113, 135, 34, 97, 157, 109, 12, 56,
             229, 253, 68, 234, 190, 164, 169, 207, 222, 75, 96, 75, 187, 246, 112, 188, 191, 190, 198, 126, 155, 40,
             250, 39, 161, 234, 133, 48, 239, 212, 5, 29, 136, 4, 57, 208, 212, 217, 229, 153, 219, 230, 248, 124, 162,
             31, 101, 86, 172, 196, 68, 34, 41, 244, 151, 255, 42, 67, 167, 35, 148, 171, 57, 160, 147, 252, 195, 89,
             91, 101, 146, 204, 12, 143, 125, 244, 239, 255, 209, 93, 132, 133, 79, 126, 168, 111, 224, 230, 44, 254,
             20, 67, 1, 163, 161, 17, 8, 78, 130, 126, 83, 247, 53, 242, 58, 189, 187, 210, 215, 42, 145, 211, 134, 235,
             0, 0, 0, 0])
    ]


def sub_604db(a1):
    for i in range(4):
        a1[8 + i] = 0xFF


def sub_a6e8(a1, a2, a3):
    v3, v5, v6, v8 = a1, a2, 0, 0

    while True:
        v8 = v5[v6]
        if int.from_bytes(v3[8:12], 'little', signed=False) > 0:
            sub_604db(a1)

        v3[12 + 2 * v6] = data_a798[v8 >> 4]

        v10 = v5[v6]

        if int.from_bytes(v3[8:12], 'little', signed=False) > 0:
            sub_604db(a1)

        v3[12 + 2 * v6 + 1] = data_a798[v10 & 0xF]

        v6 += 1
        if v6 >= a3:
            break


def sub_abb8():
    v15 = bytearray(45)
    v17 = bytearray([187, 197, 152, 57, 144, 47, 56, 83, 99, 121, 252, 203, 124, 139, 35, 19])

    v15[0] = 0x20
    v15[4] = 0x20
    v15[8] = 0x00

    for i in range(32):
        v15[12 + i] = 0x20

    v15[44] = 0x00

    sub_a6e8(v15, v17, 0x10)

    return v15


def __ror4__(value, count):
    nbits = 32
    value %= 2 ** nbits
    low = value << (nbits - count)
    value >>= count
    value |= low
    return value


def sub_2cda0(a1, a2, a3):
    a1 = bytes_to_int32(a1)

    v205 = a1
    v204 = a3
    v203 = 0
    v202 = a1[0]
    v201 = a1[1]
    v200 = a1[2]

    i = a1[3]
    while True:
        r = v204
        v204 -= 1
        if not r:
            break
        a2_2 = a2
        v4 = v203
        v5 = v203 + 1
        v6 = a2[v4]
        v7 = v5
        v5 += 1
        v8 = v6 | (a2_2[v7] << 8)
        v9 = v5
        v5 += 1
        v10 = v8 | (a2_2[v9] << 16)
        v11 = v5
        v5 += 1
        v12 = v10 | (a2_2[v11] << 24)
        v13 = v5
        v5 += 1
        v14 = a2_2[v13]
        v15 = v5
        v5 += 1
        v16 = v14 | (a2_2[v15] << 8)
        v17 = v5
        v5 += 1
        v18 = v16 | (a2_2[v17] << 16)
        v19 = v5
        v5 += 1
        v20 = v18 | (a2_2[v19] << 24)
        v21 = v201 + __ror4__(v12 + v205[23] + ((v200 ^ i) & v201 ^ i) + v202, 26)
        v22 = v5
        v5 += 1
        v23 = a2_2[v22]
        v24 = v5
        v5 += 1
        v25 = v23 | (a2_2[v24] << 8)
        v26 = v5
        v5 += 1
        v27 = v25 | (a2_2[v26] << 16)
        v28 = v5
        v5 += 1
        v29 = v27 | (a2_2[v28] << 24)
        v30 = v21 + __ror4__(v20 + v205[24] + ((v201 ^ v200) & v21 ^ v200) + i, 19)
        v31 = v5
        v5 += 1
        v32 = a2_2[v31]
        v33 = v5
        v5 += 1
        v34 = v32 | (a2_2[v33] << 8)
        v35 = v5
        v5 += 1
        v36 = v34 | (a2_2[v35] << 16)
        v37 = v5
        v5 += 1
        v38 = v36 | (a2_2[v37] << 24)
        v39 = v30 + __ror4__(v29 + v205[25] + ((v21 ^ v201) & v30 ^ v201) + v200, 15)
        v40 = v5
        v5 += 1
        v41 = a2_2[v40]
        v42 = v5
        v5 += 1
        v43 = v41 | (a2_2[v42] << 8)
        v44 = v5
        v5 += 1
        v45 = v43 | (a2_2[v44] << 16)
        v46 = v5
        v5 += 1
        v47 = v45 | (a2_2[v46] << 24)
        v48 = v39 + __ror4__(v38 + v205[26] + ((v30 ^ v21) & v39 ^ v21) + v201, 11)
        v49 = v5
        v5 += 1
        v50 = a2_2[v49]
        v51 = v5
        v5 += 1
        v52 = v50 | (a2_2[v51] << 8)
        v53 = v5
        v5 += 1
        v54 = v52 | (a2_2[v53] << 16)
        v55 = v5
        v5 += 1
        v56 = v54 | (a2_2[v55] << 24)
        v57 = v48 + __ror4__(v47 + v205[27] + ((v39 ^ v30) & v48 ^ v30) + v21, 25)
        v58 = v5
        v5 += 1
        v59 = a2_2[v58]
        v60 = v5
        v5 += 1
        v61 = v59 | (a2_2[v60] << 8)
        v62 = v5
        v5 += 1
        v63 = v61 | (a2_2[v62] << 16)
        v64 = v5
        v5 += 1
        v65 = v63 | (a2_2[v64] << 24)
        v66 = v57 + __ror4__(v56 + v205[28] + ((v48 ^ v39) & v57 ^ v39) + v30, 20)
        v67 = v5
        v5 += 1
        v68 = a2_2[v67]
        v69 = v5
        v5 += 1
        v70 = v68 | (a2_2[v69] << 8)
        v71 = v5
        v5 += 1
        v72 = v70 | (a2_2[v71] << 16)
        v73 = v5
        v5 += 1
        v74 = v72 | (a2_2[v73] << 24)
        v75 = v66 + __ror4__(v65 + v205[29] + ((v57 ^ v48) & v66 ^ v48) + v39, 15)
        v76 = v5
        v5 += 1
        v77 = a2_2[v76]
        v78 = v5
        v5 += 1
        v79 = v77 | (a2_2[v78] << 8)
        v80 = v5
        v5 += 1
        v81 = v79 | (a2_2[v80] << 16)
        v82 = v5
        v5 += 1
        v83 = v81 | (a2_2[v82] << 24)
        v84 = v75 + __ror4__(v74 + v205[30] + ((v66 ^ v57) & v75 ^ v57) + v48, 12)
        v85 = v5
        v5 += 1
        v86 = a2_2[v85]
        v87 = v5
        v5 += 1
        v88 = v86 | (a2_2[v87] << 8)
        v89 = v5
        v5 += 1
        v90 = v88 | (a2_2[v89] << 16)
        v91 = v5
        v5 += 1
        v92 = v90 | (a2_2[v91] << 24)
        v93 = v84 + __ror4__(v83 + v205[31] + ((v75 ^ v66) & v84 ^ v66) + v57, 25)
        v94 = v5
        v5 += 1
        v95 = a2_2[v94]
        v96 = v5
        v5 += 1
        v97 = v95 | (a2_2[v96] << 8)
        v98 = v5
        v5 += 1
        v99 = v97 | (a2_2[v98] << 16)
        v100 = v5
        v5 += 1
        v101 = v99 | (a2_2[v100] << 24)
        v102 = v93 + __ror4__(v92 + v205[32] + ((v84 ^ v75) & v93 ^ v75) + v66, 20)
        v103 = v5
        v5 += 1
        v104 = a2_2[v103]
        v105 = v5
        v5 += 1
        v106 = v104 | (a2_2[v105] << 8)
        v107 = v5
        v5 += 1
        v108 = v106 | (a2_2[v107] << 16)
        v109 = v5
        v5 += 1
        v110 = v108 | (a2_2[v109] << 24)
        v111 = v102 + __ror4__(v101 + v205[33] + ((v93 ^ v84) & v102 ^ v84) + v75, 16)
        v112 = v5
        v5 += 1
        v113 = a2_2[v112]
        v114 = v5
        v5 += 1
        v115 = v113 | (a2_2[v114] << 8)
        v116 = v5
        v5 += 1
        v117 = v115 | (a2_2[v116] << 16)
        v118 = v5
        v5 += 1
        v119 = v117 | (a2_2[v118] << 24)
        v120 = v111 + __ror4__(v110 + v205[34] + ((v102 ^ v93) & v111 ^ v93) + v84, 10)
        v121 = v5
        v5 += 1
        v122 = a2_2[v121]
        v123 = v5
        v5 += 1
        v124 = v122 | (a2_2[v123] << 8)
        v125 = v5
        v5 += 1
        v126 = v124 | (a2_2[v125] << 16)
        v127 = v5
        v5 += 1
        v128 = v126 | (a2_2[v127] << 24)
        v129 = v120 + __ror4__(v119 + v205[35] + ((v111 ^ v102) & v120 ^ v102) + v93, 25)
        v130 = v5
        v5 += 1
        v131 = a2_2[v130]
        v132 = v5
        v5 += 1
        v133 = v131 | (a2_2[v132] << 8)
        v134 = v5
        v5 += 1
        v135 = v133 | (a2_2[v134] << 16)
        v136 = v5
        v5 += 1
        v137 = v135 | (a2_2[v136] << 24)
        v138 = v129 + __ror4__(v128 + v205[36] + ((v120 ^ v111) & v129 ^ v111) + v102, 19)
        v139 = v5
        v5 += 1
        v140 = a2_2[v139]
        v141 = v5
        v5 += 1
        v142 = v140 | (a2_2[v141] << 8) | (a2_2[v5] << 16)
        v143 = v5 + 1
        v203 = v5 + 2
        v144 = v142 | (a2_2[v143] << 24)
        v145 = v138 + __ror4__(v137 + v205[37] + ((v129 ^ v120) & v138 ^ v120) + v111, 15)
        v146 = v145 + __ror4__(v144 + v205[38] + ((v138 ^ v129) & v145 ^ v129) + v120, 10)
        v147 = v146 + __ror4__(v20 + (v205[39] & 0xFF00FF00) + ((v146 ^ v145) & v138 ^ v145) + v129, 27)
        v148 = v147 + __ror4__(v65 + v205[40] + ((v147 ^ v146) & v145 ^ v146) + v138, 23)
        v149 = v148 + __ror4__(v110 + v205[41] + ((v148 ^ v147) & v146 ^ v147) + v145, 18)
        v150 = v149 + __ror4__(v12 + (v205[42] & 0xFF0011FF) + ((v149 ^ v148) & v147 ^ v148) + v146, 12)
        v151 = v150 + __ror4__(v56 + v205[43] + ((v150 ^ v149) & v148 ^ v149) + v147, 27)
        v152 = v151 + __ror4__(v101 + v205[44] + ((v151 ^ v150) & v149 ^ v150) + v148, 23)
        v153 = v152 + __ror4__(v144 + v205[45] + ((v152 ^ v151) & v150 ^ v151) + v149, 18)
        v154 = v153 + __ror4__(v47 + v205[46] + ((v153 ^ v152) & v151 ^ v152) + v150, 12)
        v155 = v154 + __ror4__(v92 + v205[47] + ((v154 ^ v153) & v152 ^ v153) + v151, 27)
        v156 = v155 + __ror4__(v137 + v205[48] + ((v155 ^ v154) & v153 ^ v154) + v152, 23)
        v157 = v156 + __ror4__(v38 + v205[49] + ((v156 ^ v155) & v154 ^ v155) + v153, 18)
        v158 = v157 + __ror4__(v83 + v205[50] + ((v157 ^ v156) & v155 ^ v156) + v154, 12)
        v159 = v158 + __ror4__(v128 + v205[51] + ((v158 ^ v157) & v156 ^ v157) + v155, 27)
        v160 = v159 + __ror4__(v29 + (v205[52] & 0xFF110011) + ((v159 ^ v158) & v157 ^ v158) + v156, 23)
        v161 = v160 + __ror4__(v74 + v205[53] + ((v160 ^ v159) & v158 ^ v159) + v157, 18)
        v162 = v161 + __ror4__(v119 + v205[54] + ((v161 ^ v160) & v159 ^ v160) + v158, 12)
        v163 = v162 + __ror4__(v56 + v205[55] + (v162 ^ v161 ^ v160) + v159, 28)
        v164 = v163 + __ror4__(v83 + v205[56] + (v163 ^ v162 ^ v161) + v160, 21)
        v165 = v164 + __ror4__(v110 + v205[57] + (v164 ^ v163 ^ v162) + v161, 16)
        v166 = v165 + __ror4__(v137 + v205[58] + (v165 ^ v164 ^ v163) + v162, 9)
        v167 = v166 + __ror4__(v20 + v205[59] + (v166 ^ v165 ^ v164) + v163, 28)
        v168 = v167 + __ror4__(v47 + v205[60] + (v167 ^ v166 ^ v165) + v164, 21)
        v169 = v168 + __ror4__(v74 + v205[61] + (v168 ^ v167 ^ v166) + v165, 16)
        v170 = v166 + __ror4__(v128 + v205[63] + (v166 ^ v169 ^ v168) + v167, 28)
        v171 = v169 + __ror4__(v101 + v205[62] + (v169 ^ v168 ^ v170) + v166, 9)
        v172 = v168 + __ror4__(v38 + v205[65] + (v168 ^ v170 ^ v171) + v169, 16)
        v173 = v170 + __ror4__(v12 + v205[64] + (v170 ^ v171 ^ v172) + v168, 21)
        v174 = v172 + __ror4__(v65 + v205[66] + (v172 ^ v173 ^ v170) + v171, 9)
        v175 = v174 + __ror4__(v92 + v205[67] + (v174 ^ v172 ^ v173) + v170, 28)
        v176 = v175 + __ror4__(v119 + v205[68] + (v175 ^ v174 ^ v172) + v173, 21)
        v177 = v176 + __ror4__(v144 + v205[69] + (v176 ^ v175 ^ v174) + v172, 16)
        v178 = v177 + __ror4__(v29 + v205[70] + (v177 ^ v176 ^ v175) + v174, 9)
        v179 = v178 + __ror4__(v12 + v205[71] + ((v178 | ~v176) ^ v177) + v175, 26)
        v180 = v179 + __ror4__(v74 + v205[72] + ((v179 | ~v177) ^ v178) + v176, 22)
        v181 = v180 + __ror4__(v137 + v205[73] + ((v180 | ~v178) ^ v179) + v177, 17)
        v182 = v181 + __ror4__(v56 + v205[74] + ((v181 | ~v179) ^ v180) + v178, 11)
        v183 = v182 + __ror4__(v119 + v205[75] + ((v182 | ~v180) ^ v181) + v179, 26)
        v184 = v183 + __ror4__(v38 + v205[76] + ((v183 | ~v181) ^ v182) + v180, 22)
        v185 = v184 + __ror4__(v101 + v205[77] + ((v184 | ~v182) ^ v183) + v181, 17)
        v186 = v185 + __ror4__(v20 + v205[78] + ((v185 | ~v183) ^ v184) + v182, 11)
        v187 = v186 + __ror4__(v83 + v205[79] + ((v186 | ~v184) ^ v185) + v183, 26)
        v188 = v187 + __ror4__(v144 + v205[80] + ((v187 | ~v185) ^ v186) + v184, 22)
        v189 = v188 + __ror4__(v65 + v205[81] + ((v188 | ~v186) ^ v187) + v185, 17)
        v190 = v189 + __ror4__(v128 + v205[82] + ((v189 | ~v187) ^ v188) + v186, 11)
        v191 = v190 + __ror4__(v47 + v205[83] + ((v190 | ~v188) ^ v189) + v187, 26)
        v192 = v191 + __ror4__(v110 + v205[84] + ((v191 | ~v189) ^ v190) + v188, 22)
        v193 = v192 + __ror4__(v29 + v205[85] + ((v192 | ~v190) ^ v191) + v189, 17)
        v194 = v193 + __ror4__(v92 + v205[86] + ((v193 | ~v191) ^ v192) + v190, 11)
        v195 = v191 + v205[0]
        v205[0] = v195
        v202 = v195
        v196 = v194 + v205[1]
        v205[1] = v196
        v201 = v196
        v197 = v193 + v205[2]
        v205[2] = v197
        v200 = v197
        v198 = v192 + v205[3]
        v205[3] = v198
        i = v198

    return int32_to_bytes(a1)


def sub_2cc42(a1, a2, a3):
    a1 = bytes_to_int32(a1)

    v8 = a1[4] + 8 * a3
    if v8 < a1[4]:
        a1[5] += 1
    a1[5] += a3 >> 29
    a1[4] = v8
    v6 = a1[22]
    if v6:
        v9 = 6
        a1 = int32_to_bytes(a1)
        for i in range(64 - v6):
            a1[v9 * 4 + v6 + i] = a2[i]
        a1 = sub_2cda0(a1, a1[v9 * 4:], 1)
        a1 = bytes_to_int32(a1)
        v3 = 64 - v6
        a2 = a2[v3:]
        a3 -= v3
        a1[22] = 0
        for i in range(64):
            a1[v9 + i] = 0
    v7 = a3 >> 6
    if v7:
        a1 = int32_to_bytes(a1)
        a1 = sub_2cda0(a1, a2, v7)
        a1 = bytes_to_int32(a1)
        v4 = v7 << 6
        a2 = a2[v4:]
        a3 -= v4
    if a3:
        a1[22] = a3
        a1 = int32_to_bytes(a1)
        for i in range(a3):
            a1[24 + i] = a2[i]
        a1 = bytes_to_int32(a1)

    return int32_to_bytes(a1)


def sub_2dd88(a1, a2):
    v32 = 0
    v31 = 0
    v30 = 24
    a2 = bytes_to_int32(a2)
    v2 = a2[22]
    a2 = int32_to_bytes(a2)
    a2[v30 + v2] = 128
    v29 = v2 + 1
    if v29 >= 0x39:
        for i in range(64 - v29):
            a2[v30 + v29 + i] = 0
        v29 = 0
        a2 = sub_2cda0(a2, a2[24:], 1)
    for i in range(56 - v29):
        a2[v30 + v29 + i] = 0
    v3 = v30 + 56
    v4 = v3
    v3 += 1
    a2[v4] = read_int32(a2[v31 + 16:]) % 2 ** 8
    v5 = v3
    v3 += 1
    a2[v5] = (read_int16(a2[v31 + 16:]) >> 8) % 2 ** 8
    v6 = v3
    v3 += 1
    a2[v6] = read_int16(a2[v31 + 18:]) % 2 ** 8
    v7 = v3
    v3 += 1
    a2[v7] = a2[v31 + 19]
    v8 = v3
    v3 += 1
    a2[v8] = read_int32(a2[v31 + 20:]) % 2 ** 8
    v9 = v3
    v3 += 1
    a2[v9] = (read_int16(a2[v31 + 20:]) >> 8) % 2 ** 8
    v10 = v3
    v3 += 1
    a2[v10] = read_int16(a2[v31 + 22:]) % 2 ** 8
    a2[v3] = a2[v31 + 23]
    v3 -= 63
    a2 = sub_2cda0(a2[v31:], a2[v3:], 1)
    a2 = bytes_to_int32(a2)
    a2[(v31 + 88) // 4] = 0
    a2 = int32_to_bytes(a2)
    for i in range(64):
        a2[v3 + i] = 0
    v11 = read_int32(a2[v31:])
    v12 = v32
    v13 = v32 + 1
    a1[v12] = read_int32(a2[v31:]) % 2 ** 8
    v14 = v13
    v13 += 1
    a1[v14] = byte_n(v11, 1)
    v15 = v13
    v13 += 1
    a1[v15] = byte_n(v11, 2)
    v16 = v13
    v13 += 1
    a1[v16] = byte_n(v11, -1)
    v17 = read_int32(a2[v31 + 4:])
    v18 = v13
    v13 += 1
    a1[v18] = v17 % 2 ** 8
    v19 = v13
    v13 += 1
    a1[v19] = byte_n(v17, 1)
    v20 = v13
    v13 += 1
    a1[v20] = byte_n(v17, 2)
    v21 = v13
    v13 += 1
    a1[v21] = byte_n(v17, -1)
    v22 = read_int32(a2[v31 + 8:])
    v23 = v13
    v13 += 1
    a1[v23] = v22 % 2 ** 8
    v24 = v13
    v13 += 1
    a1[v24] = byte_n(v22, 1)
    v25 = v13
    v13 += 1
    a1[v25] = byte_n(v22, 2)
    a1[v13] = byte_n(v22, -1)
    v26 = read_int32(a2[v31 + 12:])
    a1[v13 + 1] = v26 % 2 ** 8
    a1[v13 + 2] = byte_n(v26, 1)
    a1[v13 + 3] = byte_n(v26, -2)
    a1[v13 + 4] = byte_n(v26, -1)

    return a1, a2


def get_sign(path='', params='', xy_common_params='', xy_platform_info='', data=''):
    """
    ????????????
    """
    content = bytearray(''.join([path, params, xy_common_params, xy_platform_info, data]), encoding='utf-8')
    ctx = make_ctx()
    t1 = bytearray(16)
    t2 = bytearray(44)

    ctx[0] = sub_2cc42(ctx[0], content, len(content))
    t1, ctx[0] = sub_2dd88(t1, ctx[0])
    ctx[0] = ctx[2].copy()
    ctx[0] = sub_2cc42(ctx[0], t1, 16)
    t1, ctx[0] = sub_2dd88(t1, ctx[0])
    sub_a6e8(t2, t1, 16)

    sign = bytes(t2[12:]).decode('utf-8')
    return sign

#  ????????????????????????
# ??????????????????url?????????header??????xy-common-params???xy-platform-info????????????data????????????
path = '/api/sns/v4/note/user/posted'

params = parse.urlencode({'user_id': '5eeb209d000000000101d84a'})

xy_common_params = parse.urlencode({})

xy_platform_info = parse.urlencode({})

data = parse.urlencode({})

# ????????????
sign = get_sign(
    path=path, 
    params=params, 
    xy_common_params=xy_common_params, 
    xy_platform_info=xy_platform_info,
    data=data
)
print(sign)
