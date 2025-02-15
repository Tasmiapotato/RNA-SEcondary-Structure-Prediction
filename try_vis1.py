import Bio
import subprocess
import ViennaRNA

def parse_dot_bracket(dot_bracket):
    paired_bases = []
    unpaired_bases = []
    stack = []

    for i, symbol in enumerate(dot_bracket):
        if symbol == '(':
            stack.append(i)
        elif symbol == ')':
            if stack:
                start = stack.pop()
                paired_bases.append((start + 1, i + 1))
        elif symbol == '.':
            unpaired_bases.append(i + 1)

    return paired_bases, unpaired_bases

dot_bracket = "(((((((...............(((.(((((((((((((((....((((.((..(((.((((((....)))))))).).))))))......)))))))..))))))))))).((((((.(((((..(((((((.....))))))).(((((((..(((((.....))))).)))))))................))))))))))))))))))((.((((....)))).))...(((((((.(..(((((....)))))..((((.(.((.......)))))))((((....(((((((..((((....))))....)))))))....))))....((......))(((((...)))))......)))))))).."
paired, unpaired = parse_dot_bracket(dot_bracket)
print("Paired bases:", paired)
print("Unpaired bases:", unpaired)

import numpy as np

def generate_basepair_matrix(paired, unpaired, length):
    matrix = np.zeros((length, length))
    
    # Set probabilities for paired bases
    for start, end in paired:
        matrix[start - 1, end - 1] = 1.0  # Assign a value (e.g., 1.0) for paired bases
        matrix[end - 1, start - 1] = 1.0  # Assuming base pairing is symmetric
    
    # Set probabilities for unpaired bases (optional)
    for idx in unpaired:
        matrix[idx - 1, idx - 1] = 0.0  # Assign a value (e.g., 0.0) for unpaired bases
    
    return matrix

# Define the length of the sequence (adjust according to your sequence length)
seq_length = 374

paired =[(64, 69), (63, 70), (62, 71), (61, 72), (60, 73), (59, 74), (57, 75), (56, 76), (55, 78), (52, 80), (51, 81), (49, 82), (48, 83), (47, 84), (46, 85), (41, 92), (40, 93), (39, 94), (38, 95), (37, 96), (36, 97), (35, 98), (34, 101), (33, 102), (32, 103), (31, 104), (30, 105), (29, 106), (28, 107), (27, 108), (25, 109), (24, 110), (23, 111), (133, 139), (132, 140), (131, 141), (130, 142), (129, 143), (128, 144), (127, 145), (160, 166), (159, 167), (158, 168), (157, 169), (156, 170), (153, 172), (152, 173), (151, 174), (150, 175), (149, 176), (148, 177), (147, 178), (124, 195), (123, 196), (122, 197), (121, 198),(120, 199), (118, 200), (117, 201), (116, 202), (115, 203), (114, 204), (113, 205), (7, 206), (6, 207), (5, 208), (4, 209), (3, 210), (2, 211), (1, 212), (219, 224), (218, 225), (217, 226), (216, 227), (214, 229), (213, 230), (249, 254), (248, 255), (247, 256), (246, 257), (245, 258), (269, 277), (268, 278), (266,279), (264, 280), (263, 281), (262, 282), (261, 283), (304, 309), (303, 310), (302, 311), (301, 312), (298, 317), (297, 318), (296, 319), (295, 320), (294, 321), (293, 322), (292, 323), (287, 328), (286, 329), (285, 330), (284, 331), (337, 344), (336, 345), (350, 354), (349, 355), (348, 356), (347, 357), (346, 358), (242, 365), (240, 366), (239, 367), (238, 368), (237, 369), (236, 370), (235, 371), (234, 372)]
unpaired = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 26, 42, 43, 44, 45, 50, 53, 54, 58, 65, 66, 67, 68, 77, 79, 86, 87, 88, 89, 90, 91, 99, 100, 112, 119, 125, 126, 134, 135, 136, 137, 138, 146, 154, 155, 161, 162, 163, 164, 165, 171, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 215, 220, 221, 222, 223, 228, 231, 232, 233, 241, 243, 244, 250, 251, 252, 253, 259, 260, 265, 267, 270, 271, 272, 273, 274, 275, 276, 288, 289, 290, 291, 299, 300, 305, 306, 307, 308, 313, 314, 315, 316, 324, 325, 326, 327, 332, 333, 334, 335, 338, 339, 340, 341, 342, 343, 351, 352, 353, 359, 360, 361, 362, 363, 364, 373, 374]  
print(len(paired))
print(len(unpaired))

paired_adjusted = [(start - 1, end - 1) for start, end in paired]
unpaired_adjusted = [idx - 1 for idx in unpaired]
# Generate the base pair probability matrix
basepair_matrix = generate_basepair_matrix(paired_adjusted, unpaired_adjusted, seq_length)
print(basepair_matrix)


