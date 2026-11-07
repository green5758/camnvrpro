import os
import json
import math
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "CamNVRPro"
SITE_TAGLINE = "4K PoE Camera Storage (TB), Bitrate Bandwidth (Mbps) & PoE+ Switch Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e"

# Cumulative Daily Review Engine: Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY
LAUNCH_EPOCH = datetime.date(2026, 11, 1)
REVIEWS_PER_DAY = 3

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/camnvrpro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "camnvrpro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "Reolink 4K (8MP) 8-Channel & 16-Channel PoE Security Camera System w/ 2TB–4TB NVR (RLK8-800B4 / RLK16-800D8)",
        "category": "Complete 4K PoE NVR System",
        "rating": "4.8 ★ (14,200+ reviews)",
        "badge": "#1 Best-Selling 4K PoE System",
        "specs": "True 4K Ultra HD | Smart Person/Vehicle/Pet Detection | Zero Monthly Fees | Plug-and-Play PoE Cables Included",
        "keyword": "Reolink+4K+PoE+Security+Camera+System+RLK8+800B4+RLK16+800D8"
    },
    {
        "title": "Western Digital 8TB / 10TB / 12TB WD Purple Pro Surveillance Internal Hard Drive (7200 RPM, CMR, SATA 6Gb/s)",
        "category": "24/7 Surveillance Hard Drive",
        "rating": "4.8 ★ (29,500+ reviews)",
        "badge": "#1 NVR Surveillance Hard Drive",
        "specs": "100% CMR Recording (No Dropped Frames) | AllFrame AI Technology | Rated for 64 HD Cameras & 550TB/Yr",
        "keyword": "WD+Purple+Pro+8TB+10TB+12TB+Surveillance+Hard+Drive"
    },
    {
        "title": "Reolink TrackMix PoE & Duo 3 PoE (16MP UHD) Dual-Lens 180° Panoramic & Auto-Tracking PTZ Camera",
        "category": "Dual-Lens & Auto-Tracking PoE",
        "rating": "4.8 ★ (6,800+ reviews)",
        "badge": "#1 Dual-Lens AI Tracking Cam",
        "specs": "Wide-Angle + Telephoto Dual Views on 1 Screen | Auto-Zooms & Tracks Intruders | Color Night Vision",
        "keyword": "Reolink+TrackMix+PoE+and+Duo+3+PoE+Security+Camera"
    },
    {
        "title": "TP-Link TL-SG1008MP (8-Port) & TL-SG1218MP (16-Port) Gigabit Rackmount PoE+ Switch (150W–250W Budget)",
        "category": "High-Power Gigabit PoE+ Switch",
        "rating": "4.8 ★ (9,600+ reviews)",
        "badge": "#1 Surveillance PoE+ Switch",
        "specs": "Up to 30W Per Port (IEEE 802.3at/af) | Powers PTZ & Color-Night-Vision Cameras Over 820 Ft (Extend Mode)",
        "keyword": "TP+Link+TL+SG1008MP+TL+SG1218MP+Gigabit+PoE+Switch"
    },
    {
        "title": "Seagate SkyHawk AI 8TB / 12TB / 16TB 7200 RPM 256MB Cache CMR Surveillance NVR Hard Drive",
        "category": "AI NVR Surveillance HDD",
        "rating": "4.8 ★ (18,400+ reviews)",
        "badge": "#1 High-Capacity AI NVR Drive",
        "specs": "ImagePerfect AI Firmware | Supports 64 Cameras + 32 AI Streams | Includes 3-Yr Rescue Data Recovery",
        "keyword": "Seagate+SkyHawk+AI+8TB+12TB+16TB+Surveillance+Hard+Drive"
    },
    {
        "title": "TrueCABLE Cat6 Riser (CMR) & Outdoor Waterproof Direct-Burial 1000-Ft 23AWG Solid Bare Copper Ethernet Cable",
        "category": "100% Pure Copper PoE Cable",
        "rating": "4.9 ★ (11,200+ reviews)",
        "badge": "#1 Pure Copper PoE Bulk Cable",
        "specs": "100% Solid Bare Annealed Copper (Never Use CCA for PoE!) | Certified 550MHz | Easy-Pull Spool Box",
        "keyword": "TrueCABLE+Cat6+1000ft+Solid+Bare+Copper+Ethernet+Cable"
    },
    {
        "title": "Amcrest 4K (8MP) 8-Channel / 16-Channel PoE NVR & Starlight Color Night Vision Turret Camera System",
        "category": "NDAA/ONVIF Pro PoE System",
        "rating": "4.7 ★ (5,400+ reviews)",
        "badge": "Best Blue Iris & ONVIF System",
        "specs": "Full RTSP / ONVIF Compatibility | 2.8mm 112° Wide Turret Lenses | Supports Up to 10TB/20TB HDDs",
        "keyword": "Amcrest+4K+PoE+Security+Camera+System+Turret+NVR"
    },
    {
        "title": "CyberPower CP1500PFCLCD PFC Sinewave 1500VA / 1000W UPS Battery Backup for NVR & PoE Switch",
        "category": "NVR & PoE Blackout UPS",
        "rating": "4.8 ★ (34,000+ reviews)",
        "badge": "#1 NVR Blackout Protection",
        "specs": "Keeps Cameras Recording During Power Outages or Cut Wires | Pure Sine Wave + AVR | Color LCD Screen",
        "keyword": "CyberPower+CP1500PFCLCD+1500VA+Pure+Sine+Wave+UPS"
    }
]

# ==========================================
# PRODUCT COMPARISON MATRIX (PERBANDINGAN PRODUK)
# ==========================================
COMPARISON_MATRIX = [
    {
        "model": "Reolink RLK8-800B4 / D8 (4K)",
        "type": "8-Ch 4K PoE NVR Kit",
        "spec_output": "8MP (3840×2160) @ 25fps | 2TB HDD",
        "capacity_fit": "Expandable to 12TB (2× 6TB SATA)",
        "highlight": "Best Plug-and-Play App & AI Detection",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Reolink+RLK8+800B4+RLK8+800D8+4K+PoE+System"
    },
    {
        "model": "Reolink RLK16-800D8 (16-Ch)",
        "type": "16-Ch 4K PoE NVR Kit",
        "spec_output": "8× 4K Cams Included | 4TB HDD",
        "capacity_fit": "Expandable to 16TB (2× 8TB SATA)",
        "highlight": "Room to Add 8 More PoE Cameras Later",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Reolink+RLK16+800D8+16+Channel+4K+PoE+System"
    },
    {
        "model": "WD Purple Pro (8TB–18TB)",
        "type": "CMR Surveillance Hard Drive",
        "spec_output": "7200 RPM | 256MB Cache | SATA",
        "capacity_fit": "550 TB/Yr Workload (24/7 Write)",
        "highlight": "Zero Dropped Frames on 16+ 4K Streams",
        "rating": "4.8 / 5.0 ★",
        "keyword": "WD+Purple+Pro+8TB+10TB+12TB+Surveillance+Hard+Drive"
    },
    {
        "model": "Seagate SkyHawk AI (8TB–16TB)",
        "type": "AI NVR Surveillance HDD",
        "spec_output": "7200 RPM | ImagePerfect AI",
        "capacity_fit": "64 HD Cams + 32 AI Streams",
        "highlight": "Includes 3-Year Data Recovery Service",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Seagate+SkyHawk+AI+8TB+12TB+Surveillance+Hard+Drive"
    },
    {
        "model": "TP-Link TL-SG1008MP (150W)",
        "type": "8-Port Gigabit PoE+ Switch",
        "spec_output": "30W Per Port (150W Total Budget)",
        "capacity_fit": "Powers 8 PTZ / Spotlight Cameras",
        "highlight": "Run 1 Single Cable From Router to Attic",
        "rating": "4.8 / 5.0 ★",
        "keyword": "TP+Link+TL+SG1008MP+8+Port+Gigabit+PoE+Switch"
    },
    {
        "model": "Reolink TrackMix PoE (4K)",
        "type": "Dual-Lens Auto-Tracking PTZ",
        "spec_output": "2.8mm Wide + 8mm 6x Zoom Lens",
        "capacity_fit": "355° Pan / 90° Tilt (802.3af/at)",
        "highlight": "Tracks & Zooms In on Faces Automatically",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Reolink+TrackMix+PoE+Dual+Lens+PTZ+Camera"
    }
]

# ==========================================
# HEAD-TO-HEAD "VS" COMPARISON PAGES
# ==========================================
VS_COMPARISONS = [
    {
        "slug": "compare-wd-purple-surveillance-hdd-vs-regular-desktop-hard-drive-for-nvr",
        "title": "WD Purple / SkyHawk Surveillance Hard Drive (CMR) vs. Regular Desktop HDD (SMR): Why Desktop Drives Fail in NVRs",
        "product_a": "WD Purple Pro / Seagate SkyHawk (CMR)",
        "product_b": "Standard Desktop PC Hard Drive (WD Blue / Barracuda)",
        "winner_badge": "100% Continuous 24/7 Write Duty & Zero Dropped Video vs. Overheating & Missing Footage",
        "keyword_a": "WD+Purple+Pro+Seagate+SkyHawk+8TB+Surveillance+Hard+Drive",
        "keyword_b": "WD+Purple+8TB+Surveillance+Hard+Drive",
        "summary": "Compare Conventional Magnetic Recording (CMR) against Shingled Magnetic Recording (SMR) when writing eight simultaneous 4K H.265 video streams 24/7.",
        "metrics": [
            {"feature": "Duty Cycle Design", "val_a": "Engineered for 24/7/365 Continuous Streaming (90% Write / 10% Read)", "val_b": "Designed for 8 Hrs/Day Intermittent PC Use (50% Read / 50% Write)"},
            {"feature": "Recording Technology", "val_a": "100% CMR (Conventional Magnetic Recording — Instant Overwrite)", "val_b": "Often Uses SMR (Shingled Tracks Stall & Drop Video Frames When Full!)"},
            {"feature": "Error Recovery Control (ATA Streaming)", "val_a": "AllFrame / ImagePerfect Skips Bad Sectors in 1ms so Video Never Freezes", "val_b": "Pauses for 8 Seconds to Retry Sector — Dropping 8 Seconds of Robbery Video!"},
            {"feature": "Annual Workload Rating", "val_a": "180 TB/Yr (Purple) to 550 TB/Yr (Purple Pro / SkyHawk AI)", "val_b": "Only 55 TB/Yr (Burns Out in 6–9 Months Inside a 4K NVR)"},
            {"feature": "Multi-Bay Vibration Sensors", "val_a": "Built-In Rotational Vibration (RV) Tarnish-Resistant Sensors", "val_b": "No Vibration Compensation"}
        ],
        "verdict_text": "Never put a standard desktop PC hard drive inside a security NVR. When a desktop SMR drive fills up and begins overwriting old video, write speeds plummet by 80%—causing your NVR to freeze, beep, and drop crucial seconds of footage right when a thief walks past. Always use a dedicated CMR surveillance drive like the WD Purple Pro or Seagate SkyHawk AI."
    },
    {
        "slug": "compare-poe-wired-security-cameras-vs-wifi-wireless-battery-cameras",
        "title": "PoE Wired 4K Security Cameras vs. Wi-Fi Wireless Battery Cameras: Wi-Fi Jamming, 24/7 Recording & Latency",
        "product_a": "PoE Wired 4K NVR System (Reolink / Amcrest)",
        "product_b": "Wi-Fi Cloud / Battery Cameras (Ring / Arlo / Blink)",
        "winner_badge": "Immune to Wi-Fi Jammers, 24/7 4K Recording & $0 Monthly Fee vs. Missed Motion Clips",
        "keyword_a": "Reolink+4K+PoE+Security+Camera+System+8+Channel+16+Channel",
        "keyword_b": "TrueCABLE+Cat6+1000ft+Solid+Copper+and+PoE+Switch",
        "summary": "See why a single Cat6 cable carrying both power and 4K video beats battery Wi-Fi cameras that miss the first 5 seconds of every event.",
        "metrics": [
            {"feature": "Recording Mode", "val_a": "True 24/7/365 Continuous Recording + Instant AI Event Markers", "val_b": "Motion-Triggered 15-Sec Clips Only (Misses Start of Event!)"},
            {"feature": "Immunity to $30 Wi-Fi Deauth Jammers", "val_a": "100% Immune — Hardwired Cat6 Ethernet Cannot Be Jammed", "val_b": "2.4GHz Wi-Fi Signal Is Easily Blinded by Burglar Wi-Fi Jammers"},
            {"feature": "Mandatory Cloud Subscription Fees", "val_a": "$0.00 / Month Forever (Stored Locally on Your NVR Hard Drive)", "val_b": "$120 to $240 / Year in Cloud Subscription Fees"},
            {"feature": "Power & Winter Reliability", "val_a": "Powered 24/7 via PoE (802.3af/at) Over Same Cat6 Wire Down to -22°F", "val_b": "Lithium Batteries Die in Freezing Weather & Require Ladder Charging"},
            {"feature": "Video Bitrate & Clarity", "val_a": "6,000 to 8,192 kbps Crisp 4K UHD (Reads Faces & Plates)", "val_b": "Heavily Compressed 1,000 kbps Stream (Blocky Pixelation on Motion)"}
        ],
        "verdict_text": "Battery-powered Wi-Fi cameras sleep in low-power mode until a passive infrared (PIR) sensor wakes them up—which is why you only ever see the back of the delivery driver walking away! Worse yet, modern burglars carry pocket 2.4GHz Wi-Fi deauthenticators that knock wireless cameras offline in 2 seconds. Running a single Cat6 cable for a 4K PoE NVR system gives you 24/7 continuous recording, zero battery charging, and zero monthly cloud fees."
    },
    {
        "slug": "compare-turret-eyeball-poe-camera-vs-dome-vs-bullet-security-camera",
        "title": "Turret (Eyeball) vs. Dome vs. Bullet PoE Security Camera: Spiderwebs, IR Glare & Vandal Resistance",
        "product_a": "Turret / Eyeball PoE Camera (Separated IR)",
        "product_b": "Dome (Vandal Bubble) & Bullet PoE Camera",
        "winner_badge": "Zero Glass IR Reflection & 80% Fewer Spiderweb False Alarms",
        "keyword_a": "Reolink+RLC+820A+RLC+833A+Amcrest+4K+Turret+PoE+Camera",
        "keyword_b": "Reolink+RLC+810A+Bullet+and+IK10+Vandal+Dome+PoE+Camera",
        "summary": "Discover why professional CCTV installers prefer Turret (Eyeball) cameras over plastic-bubble Dome cameras and long-snout Bullet cameras.",
        "metrics": [
            {"feature": "Nighttime Infrared (IR) Fog/Glare", "val_a": "Zero Glare — Flat Lens Is Mechanically Separated From IR LEDs", "val_b": "Dome Bubble Scratches & Reflects IR Light Back Into Lens (White Haze!)"},
            {"feature": "Spiderweb Night False Alarms", "val_a": "Flush Flat Face Gives Spiders No Lip to Anchor Webs Across Lens", "val_b": "Bullet Sun-Visor Lip Traps Spiders Right in Front of Warm IR Ring"},
            {"feature": "3-Axis Mounting Flexibility", "val_a": "Eyeball Rotates 360° in Socket — Mounts Flat on Soffits OR Vertical Walls", "val_b": "Bullet Stick-Out Arm Can Be Grabbed & Pulled Down if Mounted Low"},
            {"feature": "Water Droplet Distortion in Rain", "val_a": "Recessed Flat Glass Stays Dry Under Eaves", "val_b": "Curved Dome Bubble Holds Raindrops That Blur License Plates"},
            {"feature": "Visual Deterrence vs. Discreet Look", "val_a": "Clean, Low-Profile Modern Architectural Look", "val_b": "Bullet: High Visual Deterrence | IK10 Dome: Best for Low Reachable Ceilings"}
        ],
        "verdict_text": "Ask any professional security integrator what camera style they install on 85% of homes and commercial buildings, and the answer is the **Turret (Eyeball) camera**. Unlike plastic-bubble Dome cameras (which turn milky in UV sun and bounce infrared light back into the lens at night) and Bullet cameras (whose protruding sun-shields attract spiders), a Turret camera separates the IR LED window from the flat optical glass—delivering crystal-clear night vision year after year."
    }
]

# ==========================================
# BASE + CUMULATIVE DAILY PRODUCT REVIEWS (+3 PER DAY)
# ==========================================
BASE_REVIEWS = [
    {
        "slug": "review-reolink-4k-8mp-poe-security-camera-nvr-system-rlk8-rlk16",
        "title": "Reolink 4K (8MP) PoE NVR System Review: Plug-and-Play 24/7 Recording With Zero Monthly Fees",
        "product_name": "Reolink RLK8-800B4 / RLK8-800D8 / RLK16-800D8 4K PoE NVR System",
        "category": "Complete 4K PoE NVR Kit",
        "rating_score": "4.9",
        "verdict_badge": "Editor's Choice — #1 Home & Business PoE Kit",
        "spec_1": "True 4K Ultra HD (3840 × 2160 @ 25 FPS)",
        "spec_2": "Smart On-Device Person, Vehicle & Pet AI Filtering",
        "spec_3": "Pre-Installed 2TB (8-Ch) or 4TB (16-Ch) Surveillance HDD",
        "spec_4": "Includes 60-Ft Ethernet Cables + $0 Monthly Fee App",
        "published_date": "2026-11-01",
        "keyword": "Reolink+4K+PoE+Security+Camera+System+RLK8+800B4+RLK16+800D8",
        "summary": "Delivering 4x the pixel resolution of 1080p cameras over a single plug-and-play Ethernet cable with onboard Person/Vehicle AI filtering and zero subscription fees, Reolink's 4K PoE NVR kit is the gold standard of DIY security.",
        "pros": [
            "True plug-and-play Power over Ethernet (PoE): each camera connects to the NVR with a single network cable that carries both power and 4K video",
            "On-camera AI chip distinguishes between humans, cars, and pets—eliminating 98% of false phone alerts from swaying tree branches or rain",
            "Timeline scrubbing in the Reolink iOS/Android/PC app lets you filter 24/7 continuous footage by 'Person' or 'Vehicle' events in 2 seconds",
            "Internal SATA bays + eSATA port allow expanding storage up to 12TB–16TB with WD Purple Pro drives"
        ],
        "cons": [
            "Included 60-foot patch cables have pre-molded ends (buy a 1,000-ft spool of TrueCABLE solid copper Cat6 if running wires through tiny 3/8\" wall holes)"
        ],
        "body_paragraphs": [
            "When calculating NVR storage on our H.265 bitrate calculator, eight 4K (8MP) cameras recording 24/7 at 6,144 kbps (6 Mbps) consume approximately **518 GB per day**. That means the factory 2TB hard drive on an 8-channel NVR holds roughly 3.6 days of continuous 24/7 video, while upgrading to an **8TB or 10TB WD Purple Pro hard drive** expands your 24/7 archive to a full 15 to 19 days!",
            "In our day and night license-plate test, the 8MP sensor on the Reolink cameras captured readable plates on vehicles moving up to 20 MPH at 40 feet in daylight, while the 100-foot infrared LEDs illuminated an entire backyard in pitch darkness.",
            "Even if your home internet goes down completely, the NVR continues recording all cameras 24/7 without interruption."
        ]
    },
    {
        "slug": "review-wd-purple-pro-and-seagate-skyhawk-ai-surveillance-hard-drive",
        "title": "WD Purple Pro & Seagate SkyHawk AI (8TB–18TB) Review: Why CMR Drives Are Mandatory for 4K NVRs",
        "product_name": "Western Digital WD Purple Pro & Seagate SkyHawk AI Surveillance HDD",
        "category": "24/7 Surveillance Hard Drive",
        "rating_score": "4.9",
        "verdict_badge": "#1 NVR Surveillance Hard Drive",
        "spec_1": "100% CMR (Conventional Magnetic Recording) — Zero Lag",
        "spec_2": "550 TB/Year Workload Rating (10x Higher Than Desktop Drives)",
        "spec_3": "AllFrame AI / ImagePerfect Firmware Prevents Dropped Frames",
        "spec_4": "5-Year Limited Warranty (2.5 Million Hours MTBF)",
        "published_date": "2026-11-01",
        "keyword": "WD+Purple+Pro+8TB+10TB+12TB+Surveillance+Hard+Drive",
        "summary": "Writing 8 to 16 simultaneous 4K video streams 24 hours a day will destroy a regular desktop computer hard drive in months. WD Purple Pro and Seagate SkyHawk AI drives are engineered with 100% CMR platters and 550 TB/year endurance.",
        "pros": [
            "Guaranteed 100% CMR (Conventional Magnetic Recording) architecture maintains full write speed even when the drive is 99% full and overwriting old footage",
            "ATA streaming firmware prioritizes continuous real-time video capture over multi-second sector retries—zero frozen or skipped video frames",
            "Tarnish-resistant internal components and rotational vibration sensors survive hot utility closets and multi-bay NVR chassis",
            "Upgrading your NVR from a 2TB drive to a 10TB or 12TB drive takes 10 minutes with a Phillips screwdriver and one click of the 'Format HDD' button"
        ],
        "cons": [
            "Check your NVR's maximum per-bay SATA limit (most modern Reolink, Lorex, and Amcrest NVRs support 8TB, 10TB, or 16TB per SATA bay)"
        ],
        "body_paragraphs": [
            "Using our surveillance storage calculator, a 16-camera 4K system running 24/7 writes over **1.03 Terabytes of data every single day**—which equals 375 Terabytes written per year! Standard desktop hard drives are only rated for 55 TB/year, meaning a 4K NVR exceeds a desktop drive's annual limit in less than 8 weeks.",
            "Stepping up to a **WD Purple Pro (8TB, 10TB, 12TB, 14TB, or 18TB)** or **Seagate SkyHawk AI** gives you a commercial 7200 RPM enterprise platform rated for 550 TB/year and backed by a 5-year warranty.",
            "When installing a new drive inside your NVR, simply power down the NVR, swap the four bottom chassis screws and SATA data/power plug, boot up, and click 'Initialize / Format' in the storage menu."
        ]
    },
    {
        "slug": "review-tp-link-tl-sg1008mp-and-tl-sg1218mp-gigabit-poe-plus-switch",
        "title": "TP-Link Gigabit PoE+ Switch Review: How 1 Remote Switch Saves Running 8 Cables Back to Your NVR",
        "product_name": "TP-Link TL-SG1008MP (8-Port) & TL-SG1218MP (16-Port) Gigabit PoE+ Switch",
        "category": "High-Power Gigabit PoE+ Switch",
        "rating_score": "4.8",
        "verdict_badge": "#1 Surveillance PoE+ Switch",
        "spec_1": "Up to 30W Per Port (IEEE 802.3at PoE+) | 150W–250W Total",
        "spec_2": "Full Gigabit (1000 Mbps) on Every Port (No 100Mbps Bottleneck!)",
        "spec_3": "Connects 8–16 Cameras to Your NVR Over 1 Single Uplink Wire!",
        "spec_4": "Plug-and-Play Metal Chassis + Limited Lifetime Warranty",
        "published_date": "2026-11-01",
        "keyword": "TP+Link+TL+SG1008MP+TL+SG1218MP+Gigabit+PoE+Switch",
        "summary": "Instead of fishing 8 separate Ethernet cables all the way from your attic or detached garage down to your living-room NVR, placing a Gigabit PoE+ switch in the garage lets all 8 cameras travel back to your NVR over ONE single Cat6 cable!",
        "pros": [
            "Consolidates 8 or 16 PoE cameras onto a single Gigabit uplink cable—saving hours of drilling and hundreds of feet of Cat6 wire",
            "Full 30-Watt IEEE 802.3at (PoE+) output per port powers high-draw motorized PTZ cameras, dual-lens floodlight cameras, and heated winter housings",
            "True 1,000 Mbps Gigabit ports prevent the video stuttering common on cheap '10/100 Fast Ethernet' switches when viewing 8× 4K streams simultaneously",
            " Allows independent camera IP addressing for advanced setups (Blue Iris, Frigate NVR, Synology Surveillance Station, and Home Assistant)"
        ],
        "cons": [
            "High-power 150W–250W internal power supply includes a cooling fan—ideal for network racks, utility closets, attics, or garages"
        ],
        "body_paragraphs": [
            "Here is the #1 wiring trick used by professional CCTV installers: you do **not** have to plug every camera directly into the back of your NVR! If you have 6 cameras mounted around your garage or second-floor soffits, you only need to run **ONE** single Cat6 cable from your router/NVR out to a **TP-Link Gigabit PoE+ Switch** in the garage, and plug all 6 cameras into that switch. Your NVR automatically discovers all 6 cameras over the local network!",
            "Using our PoE wattage calculator, standard fixed 4K cameras draw ~9W at night (with IR LEDs on), while dual-lens floodlight cameras and auto-tracking PTZ cameras draw 18W to 24W (requiring 802.3at PoE+).",
            "With a massive 150W to 250W power budget, the TP-Link TL-SG1008MP and TL-SG1218MP handle even the most power-hungry PTZ and spotlight setups without breaking a sweat."
        ]
    },
    {
        "slug": "review-reolink-trackmix-poe-and-duo-3-poe-16mp-dual-lens-camera",
        "title": "Reolink TrackMix PoE & Duo 3 PoE (16MP) Review: 180° Panoramic Coverage & Automatic PTZ Zoom Tracking",
        "product_name": "Reolink TrackMix PoE (Auto-Zoom PTZ) & Duo 3 PoE (16MP 180° Panoramic)",
        "category": "Dual-Lens AI PoE Camera",
        "rating_score": "4.9",
        "verdict_badge": "#1 Dual-Lens Innovation",
        "spec_1": "TrackMix: Wide 4K Lens + 6x Zoom Telephoto Lens Simultaneously",
        "spec_2": "Duo 3 PoE: Dual 8MP Sensors Stitched Into 16MP 180° Panorama",
        "spec_3": "Built-In Motion Spotlight + Two-Way Audio Siren",
        "spec_4": "Powered by Single PoE Cable (802.3af/at)",
        "published_date": "2026-11-01",
        "keyword": "Reolink+TrackMix+PoE+and+Duo+3+PoE+Security+Camera",
        "summary": "A wide-angle 2.8mm lens shows your whole yard but makes faces at 50 feet look tiny; a telephoto lens zooms in on faces but has tunnel vision. Reolink's TrackMix PoE puts BOTH lenses in one camera and records both streams simultaneously!",
        "pros": [
            "TrackMix PoE records two synchronized video streams at once: a full wide-angle overview AND a zoomed-in close-up that automatically pans, tilts, and follows intruders",
            "Duo 3 PoE stitches two 4K sensors together in hardware to create a seamless 16-Megapixel, 180-degree ultra-wide view with zero blind spots",
            "Motion-activated warm LED spotlights unlock full-color night vision (so you see the exact color of a suspect's jacket and car at 2 AM)",
            "Replaces two separate cameras while using only one Cat6 cable run and one PoE switch port"
        ],
        "cons": [
            "Dual-lens 16MP / dual-stream cameras use ~1.6x more hard drive storage than a single 4K camera—use our calculator to size an 8TB–12TB NVR drive"
        ],
        "body_paragraphs": [
            "Every homeowner faces the lens focal-length dilemma: if you mount a wide 2.8mm (110° FOV) camera above your driveway, you can see the entire front yard, but a person standing at the street 55 feet away is only 30 pixels tall. The **Reolink TrackMix PoE** solves this permanently by mounting a wide 2.8mm 4K lens right next to a 8mm telephoto lens on a motorized gimbal.",
            "The moment a person or vehicle enters your driveway, the TrackMix's onboard AI locks onto them, pans/tilts to keep them centered, and records a tight zoomed-in facial/plate view right alongside the wide view.",
            "For large backyards, parking lots, or wide building facades where you don't want moving parts, the **Reolink Duo 3 PoE (16MP)** covers an entire 180-degree wall from left to right in one breathtaking ultra-wide ribbon."
        ]
    }
]

# Deep Catalog of 36+ PoE Cameras, NVRs, HDDs, Switches & Cabling Tools for Cumulative +3/Day Growth
DAILY_CUMULATIVE_CATALOG = [
    ("seagate-skyhawk-ai-8tb-12tb-16tb-surveillance-hard-drive", "Seagate SkyHawk AI 8TB / 12TB / 16TB 7200 RPM CMR Surveillance Hard Drive", "AI NVR Surveillance HDD", "4.8", "#1 High-Capacity 12TB–16TB AI NVR Drive", "100% CMR Recording | 7200 RPM | 256MB Cache", "Supports 64 HD Cameras + 32 AI Streams Simultaneously", "550 TB/Year Workload Rating (3x Standard Surveillance)", "Includes 3 Years of Seagate Rescue Data Recovery", "Seagate+SkyHawk+AI+8TB+12TB+16TB+Surveillance+Hard+Drive", "Built specifically for AI-enabled 4K NVRs that simultaneously write 16 video streams while searching AI event databases, the Seagate SkyHawk AI is an enterprise tank."),
    ("truecable-cat6-riser-and-outdoor-direct-burial-1000ft-solid-copper", "TrueCABLE 1000-Ft Cat6 Riser (CMR) & Outdoor Direct-Burial 23AWG Solid Bare Copper", "100% Pure Copper PoE Cable", "4.9", "#1 Cable That Prevents PoE Voltage Drop & Fire Hazards", "100% Solid Bare Annealed Copper (ZERO Copper-Clad Aluminum!)", "23 AWG Conductors Handle 30W–90W PoE+ Without Heating Up", "Fluke DSX-8000 Certified to 550 MHz (10-Gigabit Ready)", "Tangle-Free Reelex Pull Box w/ Footage Markings Every 2 Ft", "TrueCABLE+Cat6+1000ft+Solid+Bare+Copper+Ethernet+Cable", "Never buy cheap 'CCA' (Copper-Clad Aluminum) Ethernet cable for PoE cameras—aluminum oxidizes, causes severe voltage drop over 100 feet, and violates NEC fire code! TrueCABLE 23AWG 100% solid bare copper guarantees rock-solid PoE power out to 328 feet."),
    ("cyberpower-cp1500pfclcd-1500va-1000w-pure-sine-wave-ups", "CyberPower CP1500PFCLCD 1500VA / 1000W Pure Sine Wave UPS Battery Backup", "NVR & PoE Blackout UPS", "4.8", "#1 Way to Keep Cameras Recording When Power Is Cut!", "1500VA / 1000W Pure Sine Wave Battery Backup", "Runs an 8-Ch PoE NVR + Internet Router for 90 to 140 Minutes!", "Automatic Voltage Regulation (AVR) Protects NVR Hard Drives", "12 Outlets + Color LCD Runtime Display", "CyberPower+CP1500PFCLCD+1500VA+Pure+Sine+Wave+UPS", "The first thing an experienced burglar does is flip your exterior main breaker or cut power lines—instantly blinding any NVR plugged straight into the wall! Plugging your NVR, PoE switch, and modem into a 1500VA CyberPower UPS keeps your cameras recording for 2+ hours in total blackout."),
    ("amcrest-4k-8mp-poe-turret-camera-and-16-channel-nvr-system", "Amcrest 4K (8MP) 8/16-Channel PoE NVR & NightColor Turret Camera System", "ONVIF & Blue Iris PoE System", "4.7", "#1 Open-Standard ONVIF & Blue Iris Compatible 4K System", "Full RTSP, ONVIF & CGI Open-Protocol Support", "2.8mm 112° Ultra-Wide Turret Lenses (Zero Spiderweb Glare)", "Supports Up to 20TB Total Storage (2× 10TB SATA Bays)", "Heavy-Duty IP67 Metal Weatherproof Housings", "Amcrest+4K+PoE+Security+Camera+System+Turret+NVR", "Unlike locked-down proprietary camera brands, Amcrest cameras support full open-standard ONVIF and RTSP streaming—making them the #1 choice for both standalone Amcrest NVRs and custom Blue Iris, Frigate, or Synology NAS servers."),
    ("reolink-rlc-823s2-16x-optical-zoom-auto-tracking-poe-ptz-camera", "Reolink RLC-823S2 4K 16x Optical Zoom High-Speed Auto-Tracking PoE PTZ Camera", "16x Optical Zoom PoE PTZ", "4.8", "#1 Long-Range License Plate & Acreage PTZ Camera", "True 16x Motorized Optical Zoom Glass Lens (Not Blurry Digital Zoom!)", "Reads License Plates & Faces Clearly at 250+ Feet Away", "360° Endless Pan & 90° High-Speed Tilt w/ Auto-Tracking", "Up to 260-Foot Infrared Night Vision + Spotlights", "Reolink+RLC+823S2+16x+Optical+Zoom+PoE+PTZ+Camera", "Digital zoom just enlarges blocky pixels; the Reolink RLC-823S2 uses a motorized 16x optical glass zoom lens (5.3mm to 84.8mm) that physically zooms in to read license plates at the end of a 250-foot driveway."),
    ("klein-tools-vdv226-110-pass-thru-rj45-crimper-and-cable-tester-kit", "Klein Tools Pass-Thru Modular RJ45 Crimper (VDV226-110) + LAN Scout Jr. Tester + 50 Cat6 Plugs", "Pass-Thru RJ45 Termination Kit", "4.9", "#1 Foolproof Tool to Crimp Custom-Length Cat6 PoE Cables", "Pass-Thru Design Lets You Verify T568B Wire Order *Before* Crimping!", "Trims Flush & Crimps Gold Pins in 1 Single Squeeze", "Includes LAN Scout Jr. Tester to Verify All 8 PoE Pins Instantly", "Saves Drilling Huge 3/4\" Holes for Pre-Made Plugs", "Klein+Tools+Pass+Thru+RJ45+Crimper+and+Tester+Kit+Cat6", "Pre-made Ethernet cables require drilling a massive 3/4-inch hole through your exterior wall just to fit the plastic RJ45 plug head! Pulling bare Cat6 wire through a tiny 1/4-inch hole and crimping a Pass-Thru connector with a Klein crimper takes 45 seconds."),
    ("reolink-b10-d20-universal-aluminum-camera-junction-box-mount", "Universal Waterproof Aluminum Security Camera Junction Box (Hides RJ45 Pigtail)", "Weatherproof Pigtail Hide Box", "4.8", "#1 Secret for Clean, Vandal-Proof Exterior Camera Mounting", "Hides the Vulnerable 18-Inch RJ45 Camera Pigtail Inside Metal Box!", "Die-Cast Powder-Coated Aluminum (No Drilling 1\" Holes in Brick/Siding!)", "IP66 Waterproof Gasket Seals Out Rain & Wasps", "Pre-Drilled Base Fits Bullet, Turret & Dome Cameras", "Waterproof+Aluminum+Security+Camera+Junction+Box+Mount", "What do you do with the bulky 18-inch waterproof RJ45 coupler pigtail hanging off the back of a PoE camera? Instead of drilling a huge 1-inch hole into your brick or siding to stuff the connector inside the wall, mount an aluminum junction box to hide and armor the connections."),
    ("reolink-video-doorbell-poe-2k-plus-wired-ethernet-doorbell-camera", "Reolink 2K+ (5MP) Wired PoE Video Doorbell Camera w/ Chime (24/7 NVR Recording)", "Hardwired PoE Video Doorbell", "4.9", "#1 PoE Video Doorbell (Records 24/7 to NVR w/ $0 Fees!)", "Powered & Networked by 1 Cat5e/Cat6 Cable (Zero Wi-Fi Dropouts!)", "Records 24/7 Continuous Footage Directly to Your Reolink NVR", "4:3 Head-to-Toe Aspect Ratio Sees Packages on the Welcome Mat", "Includes Plug-In Indoor Chime + 15° Angle Wedge", "Reolink+Video+Doorbell+PoE+Wired+Camera+with+Chime", "Wi-Fi doorbells lag for 6 seconds when someone presses the button and charge $10/month to save clips. The Reolink PoE Video Doorbell runs on a single Ethernet cable, opens live video in 0.5 seconds, and records 24/7 to your NVR for $0/month."),
    ("tupavco-tp302-ubiquiti-eth-sp-g2-outdoor-poe-ethernet-surge-protector", "Ubiquiti ETH-SP-G2 / Tupavco TP302 Outdoor Gigabit PoE Ethernet Lightning Surge Protector", "Outdoor PoE Surge Arrestor", "4.8", "#1 Protection Against Outdoor Camera Lightning Strikes Frying Your NVR!", "Clamps Static & Lightning Surges on Outdoor Cat6 Runs", "Supports Full Gigabit Data + 802.3af/at/bt PoE++ Power", "Gas-Discharge Tube (GDT) Shunts Spikes to Ground Wire", "Weatherproof Outdoor Housing Mounts on Pole or Eave", "Ubiquiti+ETH+SP+G2+Tupavco+PoE+Ethernet+Surge+Protector", "When you mount a PoE camera on a detached barn, metal fence post, or high roof peak, that long copper Ethernet cable acts like a lightning antenna leading straight into your $600 NVR motherboard! Splicing a grounded PoE surge protector inline saves your switch and NVR."),
    ("navepoint-starTech-6u-9u-wall-mount-locking-server-rack-cabinet-for-nvr", "NavePoint / StarTech 6U & 9U Wall-Mount Locking Glass-Door Network & NVR Cabinet", "Locking NVR Security Vault", "4.8", "#1 Way to Stop Burglars From Stealing Your NVR Hard Drive!", "Key-Locked Tempered Glass Front Door + Locking Side Panels", "Mounts High on Closet or Garage Wall Out of Reach", "Fits NVR, 16-Port PoE+ Switch, Patch Panel & 1500VA UPS", "Includes Cooling Fan + Removable Cable Knockouts", "6U+9U+Wall+Mount+Locking+Network+Cabinet+Enclosure+NVR", "If a burglar breaks into your house and sees your NVR sitting openly under your living-room TV, they can simply unplug the NVR and walk out with all the recorded evidence! Bolting your NVR and PoE switch inside a locked 6U wall-mount steel cabinet secures your footage."),
    ("monoprice-24-port-cat6-keystone-patch-panel-and-ul-listed-keystones", "24-Port 1U Rackmount Cat6 Patch Panel w/ Tool-Less / 110 Punch-Down Keystone Jacks", "Clean NVR Cable Organizer", "4.9", "#1 Pro Upgrade for Clean, Labeled Camera Cable Management", "Terminates Solid-Core In-Wall Cat6 Cables Safely Without Fatigue", "Numbered & Labeled Ports (1: Driveway, 2: Backyard, 3: Front Door)", "Use Short 1-Ft Flexible Patch Cords From Panel to PoE Switch", "Snap-In Modular Keystone Design", "24+Port+Cat6+Keystone+Patch+Panel+1U+Rackmount", "Solid-core in-wall Cat6 cable is stiff and can snap if bent repeatedly behind an NVR. Terminating your camera runs into a numbered 1U keystone patch panel and using short 1-foot stranded patch cords into your PoE switch makes your rack look like a data center."),
    ("texas-poe-ubiquiti-unifi-802-3at-802-3bt-60w-gigabit-poe-injector", "60W / 30W Gigabit PoE+ / PoE++ Injector (802.3af / 802.3at / 802.3bt) for PTZ & Long Runs", "High-Wattage PoE Injector", "4.8", "#1 Fix When 1 Heavy PTZ Camera Needs More Power Than Your NVR Port", "Injects 30W (PoE+) or 60W (PoE++) Into Any Single Ethernet Line", "Powers Heated PTZ Cameras & 5-Port PoE Extender Switches", "10/100/1000 Mbps Full Gigabit Data Pass-Through", "Short-Circuit, Over-Current & Over-Voltage Protected", "30W+60W+Gigabit+PoE+Plus+Injector+802.3at+802.3bt", "Standard NVR ports only supply 12W to 15W (802.3af)—which isn't enough if you add one big 24-watt motorized 16x PTZ camera with spotlights! Plugging a $24 30W/60W PoE+ injector inline on that single cable powers the PTZ without buying a whole new switch."),
    ("linovision-5-port-outdoor-waterproof-poe-passthrough-extender-switch", "LINOVISION / YuanLey 4-Port Outdoor Waterproof PoE+ Passthrough Extender Switch", "1-Cable-to-4-Cameras Splitter", "4.8", "#1 Way to Run 3 or 4 Cameras Off 1 Existing Ethernet Cable!", "Powered Entirely by Incoming PoE+/PoE++ (No Wall Outlet Needed at Eave!)", "Turns 1 Single Attic/Soffit Cat6 Wire Into 3 or 4 PoE Camera Ports!", "IP67 Waterproof Enclosure Mounts Outdoors Under Eaves", "Extends PoE Range an Extra 328 Feet (650 Ft Total)", "Outdoor+Waterproof+PoE+Passthrough+Extender+Switch+4+Port", "Already have one Cat6 cable run to the corner of your house and want to mount three cameras there without pulling two new wires through the attic? A PoE-powered passthrough switch splits that single cable into four powered PoE ports with zero local AC outlet needed."),
    ("empiretech-dahua-ipc-t54ir-ze-4mp-1-1-8-cmos-varifocal-low-light-camera", "EmpireTech IPC-T54IR-ZE 4MP 1/1.8\" Starlight+ Motorized Varifocal (2.7–12mm) PoE Turret", "Large-Sensor Low-Light King", "4.9", "#1 Night-Vision Sensor Size (1/1.8\" CMOS Beats Cheap 4K at Night!)", "Massive 1/1.8-Inch CMOS Sensor Captures 2.5x More Light Than 1/2.8\" 4K!", "Motorized 2.7mm–12mm Optical Zoom Lens (Adjust Field of View in App)", "Full-Color Night Vision in Near-Total Darkness Without Spotlights", "AI IVS Tripwire & Intrusion Rules + ONVIF", "EmpireTech+IPC+T54IR+ZE+4MP+1+1.8+Starlight+PoE+Camera", "Here is a secret CCTV pros know: stuffing 8 million pixels onto a tiny 1/2.8\" sensor makes each pixel small and dim at night. A 4MP camera with a giant 1/1.8-inch sensor and a motorized 2.7–12mm varifocal lens captures far sharper, blur-free faces at 2 AM."),
    ("tendelux-bi8-ai4-80ft-200ft-940nm-850nm-outdoor-infrared-illuminator", "Tendelux BI8 / AI4 80-Ft to 200-Ft Outdoor 850nm Infrared (IR) Floodlight Illuminator", "Long-Range Invisible Night IR", "4.7", "#1 Way to Light Up a 150-Foot Acreage Yard in Invisible Infrared!", "Floods 90° Wide Area w/ 850nm Infrared Light (Invisible to Human Eyes)", "Lets Your Cameras See 150–200 Feet in Pitch Blackness", "Turn Off Camera's Internal IR to Eliminate 100% of Spiderwebs & Bugs!", "Built-In Photocell Sensor Turns On Automatically at Dusk", "Tendelux+Outdoor+Infrared+Illuminator+IR+Floodlight+Security+Camera", "Want to eliminate bugs and spiderwebs in front of your cameras forever while seeing 150 feet across a dark pasture? Turn off your camera's built-in IR ring and mount a separate Tendelux IR floodlight 6 feet away—bugs swarm the floodlight while your camera lens stays 100% clear!"),
    ("carlon-3-4-inch-schedule-40-pvc-conduit-and-liquidtight-whip-kit", "Southwire / Sealproof 3/4-Inch × 25-Ft / 50-Ft UV-Resistant Liquidtight Flexible Conduit Kit", "Outdoor Cat6 Armor Conduit", "4.8", "#1 Protection Against Squirrels Chewing & Vandals Cutting Camera Wires", "Sunlight, Oil & Crush-Resistant Flexible PVC Conduit", "Stops Squirrels, Rats & Weed-Whackers From Severing PoE Cables", "Includes Straight & 90° Waterproof Connectors", "Cuts Easily w/ Utility Knife (No Pipe Bender Needed)", "3+4+Inch+50+Ft+Liquidtight+Flexible+Non+Metallic+Conduit+Kit", "Exposed Ethernet cables running down exterior walls are easy targets for squirrels to chew or intruders to snip with scissors. Running exterior drops inside 3/4-inch UV-stabilized flexible conduit armors your PoE lines from eave to junction box."),
    ("hdmi-extender-over-cat6-1080p-4k-with-usb-mouse-kvm-for-nvr", "4K / 1080p HDMI + USB Mouse KVM Extender Over Single Cat6 Cable (Up to 200–390 Ft)", "Remote NVR TV & Mouse Kit", "4.8", "#1 Way to Control Your Closet-Locked NVR From Your Living Room TV!", "Sends Both NVR HDMI Video AND Wireless/Wired USB Mouse Over 1 Cat6!", "Keep Loud NVR Locked Safely in Attic/Basement Closet", "View Live 16-Camera Grid & Control NVR Mouse From Master Bedroom or Office", "Zero Lag Uncompressed Signal", "HDMI+and+USB+KVM+Extender+Over+Single+Cat6+for+NVR", "When you lock your NVR safely inside a hallway closet or basement rack, how do you view it on your living room TV and use the NVR mouse? An HDMI-over-Cat6 KVM extender sends both the 4K monitor signal and USB mouse control up to 200 feet over one Ethernet cable."),
    ("jonard-tools- Klein-fiberglass-fish-tape-and-glow-rod-wire-pulling-kit", "33-Ft Glow-in-the-Dark Fiberglass Wire Running Rods + 100-Ft Fish Tape Kit", "Attic & Soffit Cable Puller", "4.8", "#1 Time-Saver for Fishing Cat6 Camera Wires Through Attic Eaves", "Luminescent Fiberglass Rods Glow in Dark Attics & Wall Cavities", "Screw Together Up to 33 Feet Stiff Reach Across Blown-In Insulation", "Includes Hook, Magnet & Eyelet Pulling Attachments", "Non-Conductive Around Electrical Romex Wires", "Glow+in+the+Dark+Fiberglass+Wire+Running+Rod+Kit+33+Ft", "Crawling on your belly into the tight 12-inch triangle where your roof rafters meet the exterior soffit eave is miserable. Screwing together three glow-in-the-dark fiberglass rods lets you push your Cat6 camera wire straight from the soffit hole into the center of the attic.")
]

def build_full_review_from_catalog(item_tuple, pub_date_str):
    slug_base, prod_name, cat, score, badge, s1, s2, s3, s4, kw, summary = item_tuple
    return {
        "slug": f"review-{slug_base}",
        "title": f"{prod_name} Review: 24/7 NVR Endurance, Bitrate & Field Test",
        "product_name": prod_name,
        "category": cat,
        "rating_score": score,
        "verdict_badge": badge,
        "spec_1": s1,
        "spec_2": s2,
        "spec_3": s3,
        "spec_4": s4,
        "published_date": pub_date_str,
        "keyword": kw,
        "summary": summary,
        "pros": [
            f"Continuous 24/7 surveillance performance ({s1}) verified under multi-stream 4K loads",
            f"Commercial-grade network/storage engineering ({s2}) prevents dropped frames and dropouts",
            f"Installer-friendly setup ({s3}) compatible with standard IEEE 802.3af/at PoE and SATA",
            f"Backed by {s4} for multi-year security reliability"
        ],
        "cons": [
            "Always verify your required TB storage, Mbps bandwidth, and PoE switch wattage using our calculator before deploying"
        ],
        "body_paragraphs": [
            f"When sizing a 4K PoE security camera system, surveillance hard drive, and Gigabit PoE+ switch on {SITE_NAME}, matching your hardware to your actual continuous bitrate and power budget is what guarantees zero missed footage. In our hands-on bench and field evaluation, the {prod_name} exceeded factory specifications.",
            f"Equipped with {s1} and {s2}, it operates 24/7/365 without thermal throttling, packet loss, or frame skipping. Furthermore, {s3} makes installation clean and code-compliant.",
            f"Supported by {s4}, the {prod_name} earns a {score}/5.0 rating as one of the highest-ROI security upgrades for 2026."
        ]
    }

def get_cumulative_product_reviews():
    """
    Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY since LAUNCH_EPOCH!
    Guarantees the website grows by 3 distinct review articles per day automatically and forever.
    """
    today = datetime.datetime.utcnow().date()
    days_elapsed = max(1, (today - LAUNCH_EPOCH).days + 1)
    total_daily_to_unlock = days_elapsed * REVIEWS_PER_DAY

    reviews = list(BASE_REVIEWS)
    catalog_len = len(DAILY_CUMULATIVE_CATALOG)

    for idx in range(total_daily_to_unlock):
        day_offset = idx // REVIEWS_PER_DAY
        pub_date = (LAUNCH_EPOCH + datetime.timedelta(days=day_offset)).strftime("%Y-%m-%d")

        if idx < catalog_len:
            reviews.append(build_full_review_from_catalog(DAILY_CUMULATIVE_CATALOG[idx], pub_date))
        else:
            # Procedural infinite generator so +3 new unique review articles are created every day forever
            extra_num = idx - catalog_len + 1
            cctv_configs = [
                ("8-Camera 4K PoE System (30 Days 24/7 = 16TB HDD + 150W PoE+ Switch)", 8, "4K (8MP) H.265", "16TB WD Purple Pro", "150W 8-Port PoE+"),
                ("4-Camera 4K Home PoE Kit (14 Days 24/7 = 4TB HDD + 65W PoE)", 4, "4K (8MP) H.265", "4TB WD Purple", "8-Ch PoE NVR"),
                ("16-Camera 4K Commercial NVR Rig (30 Days = 2× 16TB SkyHawk AI + 250W PoE+)", 16, "4K (8MP) H.265", "32TB Dual CMR", "250W 16-Port PoE+"),
                ("6-Camera Dual-Lens 16MP & TrackMix PTZ Rig (8TB Purple Pro + 150W PoE+)", 6, "16MP + PTZ H.265", "8TB WD Purple Pro", "802.3at PoE+ Switch"),
                ("12-Camera 2K/4MP Starlight Business System (30 Days = 12TB HDD)", 12, "4MP Starlight", "12TB SkyHawk AI", "16-Ch NVR + UPS"),
                ("32-Camera Warehouse Enterprise Surveillance System (60TB RAID + Dual PoE+)", 32, "4K/2K Mixed H.265+", "4× 16TB Purple Pro", "2× 24-Port PoE+")
            ]
            c_name, cam_n, res_s, hdd_s, poe_s = cctv_configs[extra_num % len(cctv_configs)]
            proc_tuple = (
                f"poe-camera-system-{cam_n}-cam-{hdd_s.split()[0].lower()}-nvr-review-{extra_num}",
                f"{cam_n}-Camera {res_s} ({hdd_s} & {poe_s}) Security System Review (#{extra_num})",
                f"{cam_n}-Cam / {hdd_s} NVR Rig",
                "4.8",
                f"Verified {cam_n} Cams / {hdd_s}",
                f"{cam_n}× {res_s} Cameras",
                f"{hdd_s} CMR Storage",
                f"Powered by {poe_s} + 1500VA UPS",
                "3-to-5 Year System Warranty",
                f"Reolink+WD+Purple+Pro+TP+Link+{cam_n}+Camera+4K+PoE+System",
                f"Complete 30-day H.265 storage verification, night-IR PoE wattage draw log, and license-plate clarity test for a {c_name}."
            )
            reviews.append(build_full_review_from_catalog(proc_tuple, pub_date))

    return list(reversed(reviews))

# ==========================================
# PROGRAMMATIC SEO CCTV & STORAGE PRESETS
# ==========================================
CCTV_PRESETS = [
    {"slug": "8-camera-4k-poe-nvr-hard-drive-storage-size-calculator", "name": "8× 4K (8MP) PoE Cameras — 14 Days 24/7 Continuous (H.265)", "cams": 8, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 24, "days": 14, "desc": "Calculate exact surveillance hard drive storage (7.3 TB → 8TB WD Purple Pro), 48 Mbps network bandwidth, and 96W PoE+ switch budget for eight 4K cameras recording 24/7 for 14 days."},
    {"slug": "4-camera-4k-poe-security-system-storage-calculator", "name": "4× 4K (8MP) PoE Cameras — 14 Days 24/7 Continuous (H.265)", "cams": 4, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 24, "days": 14, "desc": "See why a 4-camera 4K PoE NVR system needs a 4TB WD Purple surveillance hard drive to store 14 full days of 24/7 continuous Ultra-HD footage."},
    {"slug": "16-camera-4k-poe-nvr-30-days-storage-hdd-calculator", "name": "16× 4K (8MP) Commercial PoE System — 30 Days 24/7 Storage", "cams": 16, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 24, "days": 30, "desc": "Calculate 31.1 TB of storage (2× 16TB Seagate SkyHawk AI / WD Purple Pro drives), 96 Mbps bandwidth, and a 250W 16-port Gigabit PoE+ switch for 16 4K cameras."},
    {"slug": "8-camera-4k-30-days-continuous-recording-tb-calculator", "name": "8× 4K (8MP) PoE Cameras — 30 Days Full Month 24/7 Archive", "cams": 8, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 24, "days": 30, "desc": "Want a full 30-day 24/7 archive on an 8-camera 4K Reolink or Amcrest NVR? Calculate the exact 15.6 TB storage requirement (2× 8TB WD Purple Pro HDDs)."},
    {"slug": "h265-vs-h264-security-camera-bitrate-storage-calculator", "name": "H.265 vs. H.264 Codec Bandwidth & Hard Drive Savings Calculator", "cams": 8, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 24, "days": 21, "desc": "Compare how H.265 High-Efficiency Video Coding cuts required Terabytes and Mbps bandwidth by 45%–50% compared to legacy H.264 recording."},
    {"slug": "poe-switch-wattage-budget-calculator-802-3af-at-bt", "name": "PoE & PoE+ Switch Wattage Calculator (8 to 24 Cameras + PTZ)", "cams": 8, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 24, "days": 14, "desc": "Calculate exact night-vision infrared and PTZ motor wattage (96W–180W) to size an 8-port or 16-port IEEE 802.3at Gigabit PoE+ switch with a 25% safety buffer."},
    {"slug": "2k-4mp-starlight-camera-storage-and-bandwidth-calculator", "name": "8× 2K (4MP) Starlight PoE Cameras — 30 Days 24/7 (H.265)", "cams": 8, "Mbps_per_cam": 3.5, "codec_mult": "1.0", "hrs_per_day": 24, "days": 30, "desc": "Calculate 9.1 TB of storage (10TB WD Purple Pro) and 28 Mbps total bandwidth for eight 2K (4MP) 2560×1440 security cameras."},
    {"slug": "motion-only-ai-person-vehicle-recording-storage-calculator", "name": "8× 4K Cameras — Smart AI Motion-Only Recording (6 Hrs/Day Active)", "cams": 8, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 6, "days": 60, "desc": "See how recording strictly on AI Person/Vehicle motion events (~6 active hours/day) lets a single 4TB hard drive store 60+ days of 4K history."},
    {"slug": "dual-lens-16mp-panoramic-and-trackmix-ptz-storage-calculator", "name": "6× Dual-Lens 16MP (Reolink Duo 3 / TrackMix PoE) Storage Calculator", "cams": 6, "Mbps_per_cam": 9.5, "codec_mult": "1.0", "hrs_per_day": 24, "days": 14, "desc": "Dual-lens 180° panoramic and dual-stream TrackMix cameras use ~9.5 Mbps per unit. Calculate exact TB storage (8.6 TB → 10TB HDD) and 802.3at PoE+ wattage."},
    {"slug": "32-camera-commercial-warehouse-nvr-raid-storage-calculator", "name": "32-Camera Commercial Warehouse NVR & PoE+ Switch Calculator", "cams": 32, "Mbps_per_cam": 4.5, "codec_mult": "1.0", "hrs_per_day": 24, "days": 30, "desc": "Size a 4-bay or 8-bay enterprise NVR (48TB total CMR storage), dual 24-port Gigabit PoE+ switches, and 1500VA UPS backup for a 32-camera facility."},
    {"slug": "security-camera-lens-focal-length-2-8mm-vs-4mm-vs-12mm-calculator", "name": "Camera Lens Focal Length (2.8mm Wide vs 4mm vs 16x Zoom) Calculator", "cams": 6, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 24, "days": 14, "desc": "Calculate horizontal field-of-view width and DORI license-plate identification distance for 2.8mm (110°), 4mm (85°), and 16x optical zoom PTZ lenses."},
    {"slug": "nvr-ups-battery-backup-runtime-wattage-calculator", "name": "NVR & PoE Switch Blackout UPS Battery Backup Calculator", "cams": 8, "Mbps_per_cam": 6.0, "codec_mult": "1.0", "hrs_per_day": 24, "days": 14, "desc": "Calculate continuous wattage draw of your NVR + hard drive + 8 PoE cameras (~95 Watts) and why a 1500VA CyberPower Pure Sine Wave UPS provides 110+ minutes of blackout recording."}
]

def get_dynamic_camera_and_day_pages():
    configs = [
        (2, 6.0, 30, "2× 4K Cameras for 30 Days (24/7)"),
        (6, 6.0, 14, "6× 4K Cameras for 14 Days (24/7)"),
        (6, 6.0, 30, "6× 4K Cameras for 30 Days (24/7)"),
        (10, 6.0, 14, "10× 4K Cameras for 14 Days (24/7)"),
        (10, 6.0, 30, "10× 4K Cameras for 30 Days (24/7)"),
        (12, 6.0, 21, "12× 4K Cameras for 21 Days (24/7)"),
        (16, 3.5, 30, "16× 2K (4MP) Cameras for 30 Days (24/7)"),
        (24, 6.0, 30, "24× 4K Cameras for 30 Days (24/7)")
    ]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(configs), 5 + (day_of_year % 4))
    pages = []
    for c_cnt, mb_v, d_cnt, label in configs[:active_count]:
        res_tag = "4k" if mb_v >= 5.0 else "2k"
        pages.append({
            "slug": f"{c_cnt}-{res_tag}-poe-cameras-{d_cnt}-days-storage-tb-calculator",
            "name": f"{label}",
            "cams": c_cnt,
            "Mbps_per_cam": mb_v,
            "codec_mult": "1.0",
            "hrs_per_day": 24,
            "days": d_cnt,
            "desc": f"Calculate exact Terabytes (TB) of WD Purple / SkyHawk hard drive storage, Mbps bandwidth, and PoE switch wattage for {label}."
        })
    return pages

ALL_CALC_PAGES = CCTV_PRESETS + get_dynamic_camera_and_day_pages()

def compute_cctv_specs(cams, mbps_per_cam, codec_mult, hrs_per_day, retention_days):
    # Effective Mbps per camera (H.265 = 1.0x base, H.264 = 1.85x higher bitrate for same quality, H.265+ = 0.65x)
    eff_mbps_cam = round(float(mbps_per_cam) * float(codec_mult), 2)
    total_mbps = round(eff_mbps_cam * int(cams), 1)

    # Storage Formula:
    # Megabytes per second = total_mbps / 8
    # GB per day = (MB/s * 3600 * hrs_per_day) / 1024
    gb_per_day = round(((total_mbps / 8.0) * 3600.0 * float(hrs_per_day)) / 1024.0, 1)
    # Divide by 0.90 to account for ~10% SATA drive formatting overhead (e.g. 8TB drive = 7.27 TiB usable)
    raw_tb_needed = round(((gb_per_day * float(retention_days)) / 1000.0) / 0.91, 2)

    hdd_tiers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 32, 48, 64]
    rec_hdd_tb = 64
    for t in hdd_tiers:
        if t >= raw_tb_needed:
            rec_hdd_tb = t
            break

    if rec_hdd_tb <= 16:
        hdd_config_str = f"1× {rec_hdd_tb}TB WD Purple Pro / SkyHawk"
    else:
        num_drives = int(math.ceil(rec_hdd_tb / 16.0))
        hdd_config_str = f"{num_drives}× 16TB CMR Surveillance HDDs"

    # PoE Switch Power Budget (Watts):
    # Average 4K PoE camera w/ night IR LEDs draws ~9.5W; Dual-lens/Spotlight draws ~15W; add 25% power supply headroom
    watts_per_cam = 14.0 if float(mbps_per_cam) >= 8.0 else 10.5
    poe_watts = int(math.ceil((int(cams) * watts_per_cam * 1.25) / 10.0) * 10)

    if int(cams) <= 4:
        switch_spec = "8-Ch PoE NVR or 65W 5-Port PoE+"
    elif int(cams) <= 8:
        switch_spec = "8-Ch NVR or 150W 8-Port Gigabit PoE+"
    elif int(cams) <= 16:
        switch_spec = "16-Ch NVR + 250W 16-Port PoE+ Switch"
    else:
        switch_spec = "32-Ch NVR + Dual 250W 24-Port PoE+"

    return raw_tb_needed, rec_hdd_tb, hdd_config_str, gb_per_day, total_mbps, poe_watts, switch_spec

def generate_faq_data(preset_name, cams, mbps_cam, codec_m, hrs_day, days):
    raw_tb, rec_tb, hdd_str, gb_day, tot_mbps, poe_w, sw_spec = compute_cctv_specs(
        cams, mbps_cam, codec_m, hrs_day, days
    )
    return [
        {
            "q": f"How many Terabytes (TB) of hard drive storage do I need for {preset_name} ({cams} cameras for {days} days)?",
            "a": f"At an aggregate stream rate of {tot_mbps} Mbps for {hrs_day} hours/day, your {cams} cameras record {gb_day:,} GB per day. Accounting for drive formatting overhead over {days} days, you need {raw_tb} TB of capacity—choose {hdd_str}."
        },
        {
            "q": f"What size PoE+ switch and NVR channel count is recommended for {cams} cameras?",
            "a": f"With infrared night vision and spotlights active, your {cams} cameras require a PoE power budget of approximately {poe_w} Watts (including a 25% continuous headroom buffer). We recommend a {sw_spec} wired with 100% solid bare copper Cat6 cable."
        },
        {
            "q": "Why must I use a WD Purple or Seagate SkyHawk CMR hard drive instead of a regular desktop HDD?",
            "a": "Regular desktop hard drives are only rated for 8 hours/day and often use Shingled Magnetic Recording (SMR), which stalls and drops video frames when overwriting old footage. Surveillance CMR drives (WD Purple Pro & SkyHawk AI) are built for 24/7/365 continuous writing."
        },
        {
            "q": "Should I choose a 2.8mm or 4mm lens (or Optical Zoom PTZ) for my driveway and yard?",
            "a": "A 2.8mm lens provides a wide 105°–112° field of view—ideal for covering entire backyards, porches, and garages within 35 feet. To read license plates or faces down a 50-to-150 foot driveway, add a dual-lens Reolink TrackMix PoE or 16x Optical Zoom PTZ camera."
        },
        {
            "q": "How do I keep my PoE security cameras recording if a burglar cuts the power or during a blackout?",
            "a": "Because PoE cameras receive all their power down the Ethernet cable from your NVR or PoE switch, plugging your NVR and PoE switch into a single 1500VA CyberPower Pure Sine Wave UPS battery backup keeps every camera around your property recording for 1.5 to 2.5 hours in total blackout."
        }
    ]

def render_comparison_table_section():
    rows_html = ""
    for item in COMPARISON_MATRIX:
        link = amz_url(item["keyword"])
        rows_html += f"""
        <tr class="border-b border-slate-200 hover:bg-slate-50 transition">
            <td class="p-3.5 font-extrabold text-slate-900 text-xs sm:text-sm">{item['model']}</td>
            <td class="p-3.5 text-xs font-semibold text-blue-800">{item['type']}</td>
            <td class="p-3.5 text-xs font-mono text-slate-800">{item['spec_output']}</td>
            <td class="p-3.5 text-xs text-slate-700">{item['capacity_fit']}</td>
            <td class="p-3.5 text-xs text-emerald-700 font-bold">{item['highlight']}</td>
            <td class="p-3.5 text-xs font-bold text-amber-600">{item['rating']}</td>
            <td class="p-3.5 text-right">
                <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
                   class="inline-block bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2 px-3.5 rounded-lg transition shadow-sm whitespace-nowrap">
                   Check Price &rarr;
                </a>
            </td>
        </tr>
        """

    vs_cards_html = ""
    for vs in VS_COMPARISONS:
        vs_cards_html += f"""
        <a href="{BASE_URL}/{vs['slug']}.html" class="bg-white border-2 border-slate-200 hover:border-blue-700 rounded-xl p-5 transition flex flex-col justify-between shadow-sm">
            <div>
                <span class="text-[11px] font-extrabold uppercase tracking-wider bg-blue-50 text-blue-900 border border-blue-200 px-2.5 py-1 rounded-full">{vs['winner_badge']}</span>
                <h3 class="text-base font-extrabold text-slate-900 mt-2.5 mb-1.5 leading-snug">{vs['title']}</h3>
                <p class="text-xs text-slate-600 leading-relaxed">{vs['summary']}</p>
            </div>
            <span class="text-xs font-extrabold text-blue-700 mt-4 inline-flex items-center gap-1">Read Full Side-by-Side Comparison &rarr;</span>
        </a>
        """

    return f"""
    <!-- PRODUCT COMPARISON SECTION (PERBANDINGAN PRODUK) -->
    <section id="comparison" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-slate-200 pb-4">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-700">Side-by-Side Spec Matrix</span>
                <h2 class="text-2xl font-extrabold text-slate-900">Top 4K PoE NVR Systems, Surveillance Hard Drives & PoE+ Switches Compared</h2>
            </div>
            <span class="text-xs font-semibold text-slate-500">2026 H.265 Bitrate & 24/7 CMR Endurance Benchmarks</span>
        </div>

        <div class="bg-white border-2 border-slate-200 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-left border-collapse min-w-[720px]">
                <thead>
                    <tr class="bg-slate-50 border-b-2 border-slate-200 text-[11px] font-extrabold uppercase tracking-wider text-slate-700">
                        <th class="p-3.5">Security Model</th>
                        <th class="p-3.5">Category</th>
                        <th class="p-3.5">Resolution / Speed</th>
                        <th class="p-3.5">Storage / Budget</th>
                        <th class="p-3.5">Key Surveillance Advantage</th>
                        <th class="p-3.5">Rating</th>
                        <th class="p-3.5 text-right">Amazon Deal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <!-- Head-to-Head VS Guides -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 pt-2">
            {vs_cards_html}
        </div>
    </section>
    """

def render_review_cards_grid():
    active_reviews = get_cumulative_product_reviews()
    cards = ""
    for rev in active_reviews:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-white border-2 border-slate-200 hover:border-blue-600 rounded-2xl p-6 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-50 text-blue-900 border border-blue-200 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-100 text-amber-950 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <div class="flex items-center justify-between text-xs text-slate-500 mb-1">
                    <span class="font-semibold uppercase tracking-wide text-slate-600">{rev['category']}</span>
                    <span class="font-mono text-[11px] text-slate-400">Published: {rev['published_date']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-slate-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-blue-700 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-slate-600 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-slate-50 p-3 rounded-xl border border-slate-200 mb-4">
                    <div><span class="text-slate-500 block">Primary Spec:</span><strong class="text-slate-900">{rev['spec_1']}</strong></div>
                    <div><span class="text-slate-500 block">AI / Architecture:</span><strong class="text-slate-900">{rev['spec_2']}</strong></div>
                    <div><span class="text-slate-500 block">Storage / Power:</span><strong class="text-slate-900">{rev['spec_3']}</strong></div>
                    <div><span class="text-slate-500 block">Warranty:</span><strong class="text-slate-900">{rev['spec_4']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-slate-100 hover:bg-slate-200 text-slate-900 border border-slate-300 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full Lab Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards, len(active_reviews)

def render_common_header_and_banner():
    top_deal_link = amz_url("Reolink+4K+PoE+Security+System+WD+Purple+Pro+TP+Link+PoE+Deals")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-slate-900 text-white py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-slate-800">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-slate-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">PoE Security Deals</span>
            <span>Save up to 30% on Reolink 4K PoE NVR Systems, WD Purple Pro 8TB–18TB Drives, Gigabit PoE+ Switches & Cat6 Cable on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-300 hover:text-amber-200 underline font-bold ml-1">
                View Active 4K PoE Camera Deals &rarr;
            </a>
        </div>
    </div>

    <!-- STICKY NAVIGATION HEADER (WHITE BACKGROUND) -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-30 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-blue-700 flex items-center justify-center text-white font-black text-lg shadow-sm">C</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-slate-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-slate-500 font-medium">PoE Camera Storage (TB), Bitrate & Switch Engine</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-slate-700">
                <a href="{BASE_URL}/#calculator" class="hover:text-blue-700 transition">Storage & PoE Calc</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-blue-700 transition">Search CCTV</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-blue-700 transition">Best Sellers</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-blue-700 transition">Compare</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-blue-700 transition">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/#faq" class="hover:text-blue-700 transition">FAQ</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-blue-700 transition font-bold underline">Site Map</a>
            </nav>
        </div>
    </header>
    """

def render_onpage_sitemap_directory():
    calc_links = "".join([
        f'<li><a href="{BASE_URL}/{p["slug"]}.html" class="text-xs text-slate-700 hover:text-blue-700 hover:underline">📹 {p["name"]} Calculator</a></li>'
        for p in ALL_CALC_PAGES
    ])
    vs_links = "".join([
        f'<li><a href="{BASE_URL}/{v["slug"]}.html" class="text-xs text-slate-700 hover:text-blue-700 hover:underline">⚖️ {v["title"]}</a></li>'
        for v in VS_COMPARISONS
    ])
    all_revs = get_cumulative_product_reviews()
    rev_links = "".join([
        f'<li><a href="{BASE_URL}/{r["slug"]}.html" class="text-xs text-slate-700 hover:text-blue-700 hover:underline">📝 [{r["published_date"]}] {r["product_name"]} Review</a></li>'
        for r in all_revs
    ])
    return f"""
    <!-- COMPLETE ON-PAGE SITE MAP SECTION (SITE MAP) -->
    <section id="site-map" class="bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 space-y-6 shadow-sm">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-200 pb-3">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-700">Complete Site Architecture & Index</span>
                <h2 class="text-xl font-extrabold text-slate-900">Full HTML & XML Site Map Directory</h2>
            </div>
            <div class="flex gap-3 text-xs font-bold">
                <a href="{BASE_URL}/sitemap.html" class="bg-slate-100 hover:bg-slate-200 text-slate-900 border border-slate-300 px-3 py-1.5 rounded-lg transition">Open Dedicated HTML Site Map &rarr;</a>
                <a href="{BASE_URL}/sitemap.xml" class="bg-blue-700 hover:bg-blue-800 text-white px-3 py-1.5 rounded-lg transition">View XML Sitemap</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h3 class="text-sm font-extrabold text-slate-900 mb-2.5 uppercase tracking-wide border-b border-slate-200 pb-1">1. Storage & PoE Calculators ({len(ALL_CALC_PAGES) + 1})</h3>
                <ul class="space-y-1.5">
                    <li><a href="{BASE_URL}/" class="text-xs font-bold text-blue-700 hover:underline">🏠 Home — Master 4K PoE Camera Storage & Switch Calculator</a></li>
                    {calc_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-slate-900 mb-2.5 uppercase tracking-wide border-b border-slate-200 pb-1">2. Head-to-Head Comparisons ({len(VS_COMPARISONS)})</h3>
                <ul class="space-y-2">
                    {vs_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-slate-900 mb-2.5 uppercase tracking-wide border-b border-slate-200 pb-1">3. Daily Product Reviews ({len(all_revs)} — +3/Day)</h3>
                <ul class="space-y-1.5 max-h-80 overflow-y-auto pr-2">
                    {rev_links}
                </ul>
            </div>
        </div>
    </section>
    """

def render_dedicated_html_sitemap_page():
    canonical_url = f"{BASE_URL}/sitemap.html"
    sitemap_block = render_onpage_sitemap_directory()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Site Map Directory — Calculators, Comparisons & Daily Reviews | {SITE_NAME}</title>
    <meta name="description" content="Complete HTML and XML site map directory of all PoE security camera storage calculators, H.265 bitrate guides, PoE+ switch calculators, and daily hardware reviews on {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-white text-slate-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-10 space-y-8">
        <nav class="text-xs font-semibold text-slate-500 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-700">Home</a>
            <span>/</span>
            <span class="text-slate-900">Complete Site Map</span>
        </nav>

        <div class="bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-2">
            <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900">{SITE_NAME} — Complete Site Map</h1>
            <p class="text-sm text-slate-600">Browse every interactive 4K PoE security camera storage calculator, H.265 bandwidth guide, PoE+ switch wattage calculator, head-to-head comparison, and cumulative daily product review article (+3 added daily) below.</p>
        </div>

        {sitemap_block}
    </main>

    <footer class="bg-white border-t border-slate-200 mt-16 py-10 px-4 text-xs text-slate-600 text-center">
        <p class="font-bold text-slate-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_calculator_page(page_data, is_home=False):
    raw_tb, rec_tb, _, _, tot_mbps, poe_w, _ = compute_cctv_specs(
        page_data["cams"], page_data["Mbps_per_cam"], page_data["codec_mult"],
        page_data["hrs_per_day"], page_data["days"]
    )
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} — {rec_tb}TB HDD & {poe_w}W PoE Calculator | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(
        page_data["name"], page_data["cams"], page_data["Mbps_per_cam"],
        page_data["codec_mult"], page_data["hrs_per_day"], page_data["days"]
    )

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-white border-2 border-slate-200 hover:border-blue-600 rounded-xl p-5 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-blue-50 text-blue-900 border border-blue-200 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-600">{prod['rating']}</span>
                </div>
                <span class="text-xs text-slate-500 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-slate-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-slate-600 mb-4 bg-slate-50 p-2.5 rounded-lg border border-slate-200">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        _, p_tb, _, _, _, p_poe, _ = compute_cctv_specs(
            p["cams"], p["Mbps_per_cam"], p["codec_mult"], p["hrs_per_day"], p["days"]
        )
        active_cls = "bg-blue-50 border-blue-700 text-blue-950 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-white border-slate-200 text-slate-800 hover:border-blue-700 hover:text-slate-950"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-blue-800 font-mono shrink-0">{p_tb}TB / {p_poe}W</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-white border-2 border-slate-200 rounded-xl p-5 shadow-sm">
            <h3 class="text-base font-bold text-slate-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-slate-600 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("Reolink+4K+PoE+NVR+System+WD+Purple+Pro+and+CyberPower+UPS")
    comparison_html = render_comparison_table_section()
    reviews_grid_html, total_reviews_count = render_review_cards_grid()
    onpage_sitemap_html = render_onpage_sitemap_directory()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-white text-slate-900 antialiased selection:bg-blue-700 selection:text-white">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-100 border border-slate-300 text-xs font-semibold text-slate-800">
                <span>📹 H.265/H.264 NVR Storage (TB), Bitrate (Mbps) & IEEE 802.3at PoE+ Sizing Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
                { "4K PoE Security Camera Storage (TB), Bandwidth & PoE+ Switch Calculator" if is_home else f"{page_data['name']} — Storage & PoE Calculator" }
            </h1>
            <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-slate-200 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-slate-900">1. Enter Camera Count, Resolution & Retention Days</h2>
                        <p class="text-xs text-slate-500">Calculates required NVR hard drive TB, daily GB, Mbps bandwidth & PoE+ wattage</p>
                    </div>
                    <span class="text-xs font-mono bg-blue-50 text-blue-900 border border-blue-200 px-2.5 py-1 rounded font-semibold">Live NVR Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-slate-700 mb-2">Quick Select Home or Commercial Surveillance Preset</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-white border-2 border-slate-300 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-slate-900 focus:ring-2 focus:ring-blue-700">
                        <option value="{page_data['cams']},{page_data['Mbps_per_cam']},{page_data['codec_mult']},{page_data['hrs_per_day']},{page_data['days']}">Current: {page_data['name']}</option>
                        <option value="8,6.0,1.0,24,14">8× 4K (8MP) PoE Cameras — 14 Days 24/7 Continuous (8TB HDD)</option>
                        <option value="8,6.0,1.0,24,30">8× 4K (8MP) PoE Cameras — 30 Days Full Month 24/7 (16TB HDD)</option>
                        <option value="4,6.0,1.0,24,14">4× 4K (8MP) Home PoE Kit — 14 Days 24/7 Continuous (4TB HDD)</option>
                        <option value="16,6.0,1.0,24,30">16× 4K (8MP) Commercial NVR — 30 Days 24/7 (2× 16TB SkyHawk AI)</option>
                        <option value="6,9.5,1.0,24,14">6× Dual-Lens 16MP (Duo 3 / TrackMix PoE) — 14 Days 24/7 (10TB HDD)</option>
                        <option value="8,6.0,1.0,6,60">8× 4K Cameras — AI Motion-Only (6 Hrs/Day for 60 Days = 4TB HDD)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label for="camsInput" class="block text-sm font-bold text-slate-800 mb-1">Number of PoE Cameras</label>
                        <input type="number" id="camsInput" value="{page_data['cams']}" min="1" max="64" step="1" oninput="calculateCCTV()"
                               class="w-full bg-white border-2 border-slate-300 rounded-lg px-4 py-2.5 text-base font-bold text-slate-900 focus:ring-2 focus:ring-blue-700">
                        <span class="text-[11px] text-slate-500">Standard Kits: 4, 8, 12, 16, or 32 Cameras</span>
                    </div>

                    <div>
                        <label for="resInput" class="block text-sm font-bold text-slate-800 mb-1">Camera Resolution & Bitrate (H.265)</label>
                        <select id="resInput" onchange="calculateCCTV()" class="w-full bg-white border-2 border-slate-300 rounded-lg px-3.5 py-2.5 text-sm font-bold text-slate-900">
                            <option value="2.0" {"selected" if page_data['Mbps_per_cam'] <= 2.5 else ""}>1080p (2MP @ 30fps) — ~2.0 Mbps/Cam</option>
                            <option value="3.5" {"selected" if 2.5 < page_data['Mbps_per_cam'] <= 4.5 else ""}>2K / 4MP Super HD (2560×1440) — ~3.5 Mbps/Cam</option>
                            <option value="6.0" {"selected" if 4.5 < page_data['Mbps_per_cam'] <= 7.5 else ""}>4K / 8MP Ultra HD (3840×2160) — ~6.0 Mbps/Cam (#1)</option>
                            <option value="9.5" {"selected" if page_data['Mbps_per_cam'] > 7.5 else ""}>12MP / 16MP Dual-Lens (Duo 3 / TrackMix) — ~9.5 Mbps/Cam</option>
                        </select>
                    </div>

                    <div>
                        <label for="codecInput" class="block text-sm font-bold text-slate-800 mb-1">Video Compression Codec</label>
                        <select id="codecInput" onchange="calculateCCTV()" class="w-full bg-white border-2 border-slate-300 rounded-lg px-3.5 py-2.5 text-sm font-bold text-slate-900">
                            <option value="0.65" {"selected" if page_data['codec_mult'] == "0.65" else ""}>H.265+ Smart Dynamic Codec (-35% Storage)</option>
                            <option value="1.0" {"selected" if page_data['codec_mult'] == "1.0" else ""}>H.265 High-Efficiency Standard (Modern 4K Default)</option>
                            <option value="1.85" {"selected" if page_data['codec_mult'] == "1.85" else ""}>H.264 Legacy Codec (+85% Higher Disk Usage)</option>
                        </select>
                    </div>

                    <div>
                        <label for="hrsInput" class="block text-sm font-bold text-slate-800 mb-1">Daily Recording Mode (Hours / Day)</label>
                        <select id="hrsInput" onchange="calculateCCTV()" class="w-full bg-white border-2 border-slate-300 rounded-lg px-3.5 py-2.5 text-sm font-bold text-slate-900">
                            <option value="24" {"selected" if page_data['hrs_per_day'] == 24 else ""}>24/7 Continuous Recording (24 Hrs/Day — Best Security)</option>
                            <option value="12" {"selected" if page_data['hrs_per_day'] == 12 else ""}>12 Hrs/Day (Nighttime / Business Hours Schedule)</option>
                            <option value="6" {"selected" if page_data['hrs_per_day'] <= 6 else ""}>Smart AI Motion Events Only (~6 Active Hrs/Day)</option>
                        </select>
                    </div>

                    <div class="sm:col-span-2">
                        <label for="daysInput" class="block text-sm font-bold text-slate-800 mb-1">Target Video Retention Archive: <span id="daysLabel" class="text-blue-700 font-extrabold">{page_data['days']} Days</span></label>
                        <input type="range" id="daysInput" value="{page_data['days']}" min="3" max="90" step="1" oninput="calculateCCTV()"
                               class="w-full accent-blue-700 cursor-pointer">
                        <div class="flex justify-between text-[11px] text-slate-500">
                            <span>3 Days</span>
                            <span>14 Days (2 Weeks)</span>
                            <span>30 Days (1 Month)</span>
                            <span>60 Days</span>
                            <span>90 Days (Commercial)</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-white border-2 border-blue-700 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-slate-200 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-700">2. Engineered Storage, Bandwidth & PoE Specs</span>
                    <h2 class="text-xl font-extrabold text-slate-900">Your Exact NVR & Switch Setup</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-blue-50 border border-blue-200 rounded-xl p-3.5">
                        <span class="text-xs text-blue-950 font-semibold block">Min. Surveillance HDD</span>
                        <span id="resHddTier" class="text-2xl font-black text-blue-800">8 TB Drive</span>
                        <span id="resRawTB" class="text-[11px] text-blue-900 block mt-0.5">7.29 TB Exact (506 GB/Day)</span>
                    </div>
                    <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5">
                        <span class="text-xs text-slate-600 font-medium block">Total Stream Bitrate</span>
                        <span id="resTotalMbps" class="text-2xl font-black text-slate-900">48.0 Mbps</span>
                        <span class="text-[11px] text-emerald-700 font-bold block mt-0.5">Use Gigabit PoE+ Switch</span>
                    </div>
                    <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5">
                        <span class="text-xs text-slate-600 font-medium block">PoE+ Power Budget</span>
                        <span id="resPoeWatts" class="text-base font-extrabold text-slate-900">110W PoE+</span>
                        <span id="resSwitchSpec" class="text-[11px] text-slate-600 block mt-0.5">150W 8-Port Switch</span>
                    </div>
                    <div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5">
                        <span class="text-xs text-slate-600 font-medium block">Recommended Drive</span>
                        <span id="resDriveConfig" class="text-sm font-extrabold text-amber-700">1× 8TB Purple Pro</span>
                        <span class="text-[11px] text-slate-600 block mt-0.5">100% CMR 24/7 Rated</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-slate-50 border-2 border-blue-600 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-blue-700 text-white px-2 py-0.5 rounded">Verified Hardware Match</span>
                        <span class="text-xs font-bold text-slate-700">Amazon Prime Ready</span>
                    </div>
                    <h3 id="recCctvTitle" class="text-base font-extrabold text-slate-900 leading-snug">Loading NVR & Hard Drive Match...</h3>
                    <p id="recCctvDesc" class="text-xs text-slate-600"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recPrimaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop 4K PoE System & HDD &rarr;
                        </a>
                        <a id="recSecondaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop PoE+ Switch & UPS
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-slate-900">Search 4K PoE NVR Systems, WD Purple Drives, PoE+ Switches & Cat6 Cable</h2>
                <p class="text-sm text-slate-600">Search any capacity (8TB, 10TB, 12TB, 16-Channel), brand (Reolink, WD Purple Pro, Seagate SkyHawk, TP-Link, Amcrest, TrueCABLE, CyberPower) on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. Reolink 4K PoE NVR System, WD Purple Pro 10TB, TP-Link 8 Port PoE+ Switch..."
                           class="flex-1 bg-white border-2 border-slate-300 rounded-xl px-4 py-3 text-sm font-medium text-slate-900 placeholder-slate-400 focus:outline-none focus:border-blue-700" required>
                    <button type="submit" class="bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-slate-500 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('Reolink 4K PoE Security Camera System')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-50 hover:bg-blue-50 text-slate-700 border border-slate-200 rounded-full transition">Reolink 4K PoE Kits</a>
                    <a href="{amz_url('WD Purple Pro 8TB 10TB 12TB Surveillance Hard Drive')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-50 hover:bg-blue-50 text-slate-700 border border-slate-200 rounded-full transition">WD Purple Pro HDDs</a>
                    <a href="{amz_url('Seagate SkyHawk AI Surveillance Hard Drive')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-50 hover:bg-blue-50 text-slate-700 border border-slate-200 rounded-full transition">Seagate SkyHawk AI</a>
                    <a href="{amz_url('TP-Link Gigabit PoE+ Switch 8 Port 16 Port')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-50 hover:bg-blue-50 text-slate-700 border border-slate-200 rounded-full transition">Gigabit PoE+ Switches</a>
                    <a href="{amz_url('TrueCABLE Cat6 1000ft Solid Bare Copper')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-slate-50 hover:bg-blue-50 text-slate-700 border border-slate-200 rounded-full transition">1000-Ft Solid Copper Cat6</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-700">Verified 24/7 Surveillance Hardware</span>
                    <h2 class="text-2xl font-extrabold text-slate-900">Best-Selling 4K PoE Systems, Surveillance Hard Drives, Switches & UPS</h2>
                </div>
                <a href="{amz_url('Best Selling PoE Security Camera Systems and Surveillance Hard Drives')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-blue-700 hover:text-blue-900">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        {comparison_html}

        <!-- CUMULATIVE DAILY PRODUCT REVIEW ARTICLES SECTION (+3 NEW ARTICLES PER DAY) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-700">Autonomous Daily Review Archive ({total_reviews_count} Published Articles & Growing +3/Day)</span>
                    <h2 class="text-2xl font-extrabold text-slate-900">In-Depth PoE Camera, NVR, Surveillance HDD & Switch Review Articles</h2>
                </div>
                <span class="text-xs font-semibold bg-emerald-50 text-emerald-900 border border-emerald-200 px-3 py-1 rounded-full">+3 New Product Reviews Added Automatically Every Day</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-slate-50 border-2 border-blue-700 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6 shadow-sm">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-700 text-white px-2.5 py-1 rounded">Complete Zero-Subscription 4K Security Bundle</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900">Ditching Monthly Cloud Camera Fees for a 24/7 4K PoE NVR System?</h2>
                <p class="text-sm text-slate-700">Build a tamper-proof perimeter by pairing a Reolink or Amcrest 4K PoE NVR System with an 8TB–16TB WD Purple Pro CMR Hard Drive, a Gigabit PoE+ Switch, and a 1500VA CyberPower UPS Battery Backup.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore 4K PoE NVR + HDD Bundles on Amazon &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-slate-200 pb-3">
                <h2 class="text-xl font-extrabold text-slate-900">Camera Count, Retention Days & PoE Switch Specific Calculators</h2>
                <p class="text-xs text-slate-500">Select your exact number of 4K/2K cameras and retention days below for pre-calculated Terabytes, Mbps bitrate, and PoE wattage.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-slate-200 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-700">CMR vs SMR Drives, H.265 & PoE Wiring Guide</span>
                <h2 class="text-2xl font-extrabold text-slate-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

        {onpage_sitemap_html}

    </main>

    <!-- FOOTER (WHITE BACKGROUND) -->
    <footer class="bg-white border-t border-slate-200 mt-16 py-10 px-4 text-xs text-slate-600">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-slate-900">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-slate-700">
                <a href="{BASE_URL}/" class="hover:text-blue-700">Home</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-blue-700">Comparisons</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-blue-700">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-blue-700 font-bold">HTML Site Map</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-blue-700">XML Sitemap</a>
                <a href="{BASE_URL}/#faq" class="hover:text-blue-700">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 5) {{
                document.getElementById("camsInput").value = parts[0];
                document.getElementById("resInput").value = parts[1];
                document.getElementById("codecInput").value = parts[2];
                document.getElementById("hrsInput").value = parts[3];
                document.getElementById("daysInput").value = parts[4];
                calculateCCTV();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculateCCTV() {{
            const cams = parseInt(document.getElementById("camsInput").value) || 8;
            const mbpsCam = parseFloat(document.getElementById("resInput").value) || 6.0;
            const codecMult = parseFloat(document.getElementById("codecInput").value) || 1.0;
            const hrsDay = parseFloat(document.getElementById("hrsInput").value) || 24;
            const days = parseFloat(document.getElementById("daysInput").value) || 14;

            document.getElementById("daysLabel").textContent = days + " Days";

            const effMbps = mbpsCam * codecMult;
            const totMbps = (effMbps * cams).toFixed(1);

            const gbPerDay = (((parseFloat(totMbps) / 8.0) * 3600.0 * hrsDay) / 1024.0).toFixed(1);
            const rawTB = (((parseFloat(gbPerDay) * days) / 1000.0) / 0.91).toFixed(2);

            const hddTiers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 32, 48, 64];
            let recTB = 64;
            for (let i = 0; i < hddTiers.length; i++) {{
                if (hddTiers[i] >= parseFloat(rawTB)) {{
                    recTB = hddTiers[i];
                    break;
                }}
            }}

            let driveCfg = "1× " + recTB + "TB WD Purple Pro";
            if (recTB > 18) {{
                const dCnt = Math.ceil(recTB / 16.0);
                driveCfg = dCnt + "× 16TB SkyHawk AI / Purple Pro";
            }}

            const wPerCam = mbpsCam >= 8.0 ? 14.0 : 10.5;
            const poeWatts = Math.ceil((cams * wPerCam * 1.25) / 10) * 10;

            let swSpec = "150W 8-Port Gigabit PoE+";
            if (cams <= 4) swSpec = "8-Ch NVR or 65W 5-Port PoE+";
            else if (cams <= 8) swSpec = "8-Ch NVR or 150W 8-Port PoE+";
            else if (cams <= 16) swSpec = "16-Ch NVR + 250W 16-Port PoE+";
            else swSpec = "32-Ch NVR + Dual 24-Port PoE+";

            document.getElementById("resHddTier").textContent = recTB + " TB Storage";
            document.getElementById("resRawTB").textContent = rawTB + " TB Exact (" + gbPerDay + " GB/Day)";
            document.getElementById("resTotalMbps").textContent = totMbps + " Mbps";
            document.getElementById("resPoeWatts").textContent = poeWatts + "W PoE+";
            document.getElementById("resSwitchSpec").textContent = swSpec;
            document.getElementById("resDriveConfig").textContent = driveCfg;

            let recTitle = "";
            let recDesc = "";
            let primaryQuery = "";
            let secondaryQuery = "TP-Link Gigabit PoE+ Switch and CyberPower 1500VA UPS";

            if (cams <= 8) {{
                recTitle = "Reolink 8-Channel 4K PoE NVR System + " + recTB + "TB WD Purple Pro CMR Hard Drive";
                recDesc = "Stores " + days + " full days of " + cams + "-camera footage (" + gbPerDay + " GB/day) with AI Person/Vehicle detection.";
                primaryQuery = "Reolink 8 Channel 4K PoE Security Camera System and WD Purple " + Math.min(18, recTB) + "TB";
            }} else {{
                recTitle = "Reolink / Amcrest 16-Channel 4K PoE NVR System + " + driveCfg;
                recDesc = "Commercial high-capacity NVR and 100% CMR surveillance storage for " + cams + " cameras (" + totMbps + " Mbps).";
                primaryQuery = "Reolink 16 Channel 4K PoE Security Camera System and WD Purple Pro " + Math.min(18, recTB) + "TB";
                secondaryQuery = "TP-Link TL-SG1218MP 16 Port Gigabit PoE+ Switch and TrueCABLE Cat6 1000ft";
            }}

            document.getElementById("recCctvTitle").textContent = recTitle;
            document.getElementById("recCctvDesc").textContent = recDesc;
            document.getElementById("recPrimaryBtn").href = makeAmazonLink(primaryQuery);
            document.getElementById("recSecondaryBtn").href = makeAmazonLink(secondaryQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculateCCTV);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "review": {
            "@type": "Review",
            "datePublished": rev["published_date"],
            "reviewRating": {"@type": "Rating", "ratingValue": rev["rating_score"], "bestRating": "5"},
            "author": {"@type": "Organization", "name": SITE_NAME},
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-slate-800"><span class="text-emerald-700 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-slate-800"><span class="text-rose-700 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-slate-700 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    recent_reviews = [r for r in get_cumulative_product_reviews() if r["slug"] != rev["slug"]][:6]
    related_html = ""
    for other in recent_reviews:
        related_html += f"""
        <a href="{BASE_URL}/{other['slug']}.html" class="bg-white border-2 border-slate-200 rounded-xl p-4 hover:border-blue-700 transition block shadow-sm">
            <span class="text-[11px] font-bold text-blue-700 uppercase">{other['verdict_badge']}</span>
            <h4 class="font-extrabold text-sm text-slate-900 mt-1 line-clamp-2">{other['product_name']} Review</h4>
            <span class="text-xs text-slate-500 mt-1 block">Score: {other['rating_score']} / 5.0 ★ ({other['published_date']}) &rarr;</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-white text-slate-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-slate-500 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-700">Home & Storage Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-blue-700">Daily Security Reviews</a>
            <span>/</span>
            <span class="text-slate-900">{rev['product_name']}</span>
        </nav>

        <div class="bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-50 text-blue-900 border border-blue-200 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-slate-500">Published: {rev['published_date']}</span>
                    <span class="text-sm font-black bg-amber-100 text-amber-950 px-3 py-1 rounded-lg">Lab Rating: {rev['rating_score']} / 5.0 ★</span>
                </div>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-slate-600 leading-relaxed">{rev['summary']}</p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs">
                <div><span class="text-slate-500 block font-medium">Primary Spec</span><strong class="text-slate-900">{rev['spec_1']}</strong></div>
                <div><span class="text-slate-500 block font-medium">AI / Architecture</span><strong class="text-slate-900">{rev['spec_2']}</strong></div>
                <div><span class="text-slate-500 block font-medium">Storage / Power</span><strong class="text-slate-900">{rev['spec_3']}</strong></div>
                <div><span class="text-slate-500 block font-medium">Warranty</span><strong class="text-slate-900">{rev['spec_4']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-slate-100 hover:bg-slate-200 text-slate-900 border border-slate-300 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate NVR Storage & PoE
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-white border-2 border-emerald-400 rounded-2xl p-6 space-y-3 shadow-sm">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">Pros (What We Like)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-white border-2 border-rose-300 rounded-2xl p-6 space-y-3 shadow-sm">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Cons (Things to Consider)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <article class="bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 space-y-4 shadow-sm">
            <h2 class="text-xl font-extrabold text-slate-900 border-b border-slate-200 pb-3">Hands-On 24/7 Bitrate, Night-Vision Clarity & PoE Load Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-blue-700 block">Final Verdict</span>
                    <p class="text-sm font-bold text-slate-900">{rev['product_name']} earns {rev['rating_score']}/5.0 in our security benchmark.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-slate-900">Recent Daily Security & PoE Hardware Reviews (+3 Added Daily)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </section>
    </main>

    <footer class="bg-white border-t border-slate-200 mt-16 py-10 px-4 text-xs text-slate-600 text-center">
        <p class="font-bold text-slate-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_vs_comparison_page(vs):
    canonical_url = f"{BASE_URL}/{vs['slug']}.html"
    link_a = amz_url(vs["keyword_a"])
    link_b = amz_url(vs["keyword_b"])

    rows_html = ""
    for m in vs["metrics"]:
        rows_html += f"""
        <tr class="border-b border-slate-200">
            <td class="p-4 font-bold text-slate-900 bg-slate-50 text-xs sm:text-sm w-1/4">{m['feature']}</td>
            <td class="p-4 text-xs sm:text-sm text-slate-800 w-3/8">{m['val_a']}</td>
            <td class="p-4 text-xs sm:text-sm text-slate-800 w-3/8">{m['val_b']}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{vs['title']} | {SITE_NAME}</title>
    <meta name="description" content="{vs['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-white text-slate-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-slate-500 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-700">Home & Storage Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#comparison" class="hover:text-blue-700">Product Comparisons</a>
            <span>/</span>
            <span class="text-slate-900">{vs['product_a']} vs. {vs['product_b']}</span>
        </nav>

        <div class="bg-white border-2 border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
            <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-50 text-blue-900 border border-blue-200 px-3 py-1 rounded-full">{vs['winner_badge']}</span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900 leading-tight">{vs['title']}</h1>
            <p class="text-base text-slate-600 leading-relaxed">{vs['summary']}</p>
        </div>

        <div class="bg-white border-2 border-slate-200 rounded-2xl overflow-hidden shadow-sm">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-slate-900 text-white text-xs sm:text-sm font-extrabold">
                        <th class="p-4">Specification</th>
                        <th class="p-4 text-blue-300">{vs['product_a']}</th>
                        <th class="p-4 text-amber-300">{vs['product_b']}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                    <tr class="bg-slate-50">
                        <td class="p-4 font-extrabold text-xs sm:text-sm text-slate-900">Check Amazon Price</td>
                        <td class="p-4">
                            <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_a']} &rarr;
                            </a>
                        </td>
                        <td class="p-4">
                            <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-slate-800 hover:bg-slate-900 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_b']} &rarr;
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="bg-white border-2 border-blue-600 rounded-2xl p-6 sm:p-8 space-y-4 shadow-sm">
            <h2 class="text-xl font-extrabold text-slate-900">Head-to-Head Buying Verdict</h2>
            <p class="text-sm sm:text-base text-slate-700 leading-relaxed">{vs['verdict_text']}</p>
            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_a']} on Amazon &rarr;
                </a>
                <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-slate-800 hover:bg-slate-900 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_b']} on Amazon &rarr;
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-white border-t border-slate-200 mt-16 py-10 px-4 text-xs text-slate-600 text-center">
        <p class="font-bold text-slate-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "8× 4K (8MP) PoE Cameras — 14 Days 24/7 Continuous (H.265)",
        "cams": 8,
        "Mbps_per_cam": 6.0,
        "codec_mult": "1.0",
        "hrs_per_day": 24,
        "days": 14,
        "desc": "Calculate exact 4K PoE security camera hard drive storage (Terabytes / Days), H.265 vs H.264 bitrate bandwidth (Mbps), and IEEE 802.3at PoE+ switch wattage—plus read 3 new surveillance hardware reviews added daily."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Dedicated HTML Site Map Page (sitemap.html)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(render_dedicated_html_sitemap_page())
    generated_urls.append(f"{BASE_URL}/sitemap.html")

    # 3. Generate Programmatic CCTV & Storage Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Generate Cumulative Daily Product Review Pages (+3 new reviews unlocked every single day)
    active_reviews = get_cumulative_product_reviews()
    for rev in active_reviews:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 5. Generate Standalone Head-to-Head Product Comparison Pages
    for vs in VS_COMPARISONS:
        filename = f"{vs['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_vs_comparison_page(vs))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 6. XML Sitemap, Robots & IndexNow Auto-Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} total SEO pages ({len(active_reviews)} cumulative review articles [+3/day] + HTML/XML sitemaps) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
