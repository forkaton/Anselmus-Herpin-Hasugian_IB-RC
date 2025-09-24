from algorithm import draw_ascii
from ucs import ucs
from ids import ids
from gbfs import gbfs
from astar import astar

graph = {
    "Cilegon": {"Tangerang": 81},
    "Tangerang": {"Cilegon": 81, "Jakarta": 29},
    "Jakarta": {"Tangerang": 29, "Depok": 22, "Bekasi": 25},
    "Depok": {"Jakarta": 22, "Bogor": 44},
    "Bogor": {"Depok": 44, "Sukabumi": 57},
    "Sukabumi": {"Bogor": 57, "Bandung": 93},
    "Bekasi": {"Jakarta": 25, "Subang": 95, "Indramayu": 185},
    "Indramayu": {"Bekasi": 185, "Cirebon": 56},
    "Subang": {"Bekasi": 95, "Cirebon": 103},
    "Cirebon": {"Subang": 103, "Indramayu": 56, "Tegal": 71, "Bandung": 106},
    "Bandung": {"Sukabumi": 93, "Cirebon": 106, "Tasikmalaya": 63},
    "Tasikmalaya": {"Bandung": 63, "Cilacap": 96, "Purwokerto": 113},
    "Cilacap": {"Tasikmalaya": 96, "Purwokerto": 42},
    "Purwokerto": {"Cilacap": 42, "Tasikmalaya": 113, "Kebumen": 57, "Tegal": 65},
    "Kebumen": {"Purwokerto": 57, "Yogyakarta": 81},
    "Tegal": {"Cirebon": 71, "Pekalongan": 70, "Purwokerto": 65},
    "Pekalongan": {"Tegal": 70, "Semarang": 83},
    "Semarang": {"Pekalongan": 83, "Kudus": 60, "Ambarawa": 37},
    "Kudus": {"Semarang": 60, "Rembang": 62},
    "Rembang": {"Kudus": 62, "Tuban": 93},
    "Tuban": {"Rembang": 93, "Bojonegoro": 95},
    "Bojonegoro": {"Tuban": 95, "Ngawi": 103, "Surabaya": 111},
    "Surabaya": {"Bojonegoro": 111, "Sidoarjo": 35},
    "Sidoarjo": {"Surabaya": 35, "Probolinggo": 66, "Nganjuk": 118},
    "Nganjuk": {},
    "Probolinggo": {"Sidoarjo": 66, "Situbondo": 100, "Lumajang": 75},
    "Situbondo": {"Probolinggo": 100, "Banyuwangi": 88},
    "Banyuwangi": {"Situbondo": 88, "Jember": 100},
    "Jember": {"Banyuwangi": 100, "Lumajang": 65},
    "Lumajang": {"Jember": 65, "Probolinggo": 75, "Kepanjen": 116},
    "Kepanjen": {"Lumajang": 116, "Trenggalek": 114},
    "Trenggalek": {"Kepanjen": 114, "Pacitan": 108, "Ngawi": 86},
    "Pacitan": {"Trenggalek": 108, "Yogyakarta": 107},
    "Yogyakarta": {"Pacitan": 107, "Kebumen": 81, "Magelang": 40},
    "Magelang": {"Yogyakarta": 40, "Ambarawa": 35},
    "Ambarawa": {"Magelang": 35, "Semarang": 37},
    "Ngawi": {"Trenggalek": 86, "Surakarta": 72, "Bojonegoro": 103},
    "Surakarta": {"Ngawi": 72, "Magelang": 75},
}


start = "Cilegon"
goal = "Banyuwangi"

# UCS

path_ucs, cost_ucs = ucs(graph, start, goal)
print("UCS:", path_ucs, "Cost:", cost_ucs)
draw_ascii(path_ucs, graph)

# IDS

path_ids, cost_ids = ids(graph, start, goal)
print("IDS:", path_ids, "Cost:", cost_ids)
draw_ascii(path_ids, graph)

# GBFS

path_gbfs, cost_gbfs = gbfs(graph, start, goal)
print("GBFS:", path_gbfs, "Cost:", cost_gbfs)
draw_ascii(path_gbfs, graph)

# A*

path_astar, cost_astar = astar(graph, start, goal)
print("A*:", path_astar, "Cost:", cost_astar)
draw_ascii(path_astar, graph)
