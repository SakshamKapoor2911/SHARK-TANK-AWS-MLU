// ==============================================================================
// PRISMATIC WEB ENGINE - HARDENED AGENTIC MULTI-MODAL LOGIC
// ==============================================================================

// XSS Sanitizer Helper (Crucial for safe DOM manipulation)
function escapeHtml(str) {
  if (typeof str !== "string") return "";
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

// Format markdown bold (**text**) safely into <strong> tags without innerHTML XSS vulnerabilities
function formatSafeMarkdown(str) {
  const escaped = escapeHtml(str);
  return escaped.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
}

const PRESETS = {
  dijkstra: {
    title: "Dijkstra's Shortest Path Algorithm",
    input: "Dijkstra's algorithm finds the shortest path between nodes in a weighted graph with non-negative edge weights. It maintains a priority queue of unvisited nodes, greedily picking the vertex with minimal tentative distance, updating neighbor distances (relaxation), and marking visited until the destination is settled. Time complexity is O((V + E) log V) with min-heap.",
    analogy: "Imagine navigating **peak lunch rush at Blackburn Center Dining Hall**. You start at the entrance (**Source Node**) wanting the shortest line to the wrap station (**Target Node**). Instead of wandering randomly, you look around at the closest stations right in front of you (**Immediate Neighbors**) and estimate wait times (**Edge Weights**). You greedily step toward the station with the shortest current line (**Min-Heap Priority Queue**). Once you stand in a line, you check if walking past it opens an even faster shortcut to the drinks station (**Edge Relaxation**). Once you grab your tray, that station is locked (**Visited / Settled**)—you never backtrack.",
    mappings: [
      { key: "Graph Nodes", val: "Dining Hall Food Stations" },
      { key: "Edge Weights", val: "Station Wait Times (Minutes)" },
      { key: "Min-Heap", val: "Glancing at Shortest Line First" },
      { key: "Relaxation", val: "Updating Better Shortcut Route" },
      { key: "Visited Set", val: "Stations Already Visited" }
    ],
    svgNodes: [
      { id: "S", label: "Entrance (Source)", x: 100, y: 160, r: 35, color: "#00c49f" },
      { id: "A", label: "Salad Station", x: 300, y: 80, r: 30, color: "#a855f7" },
      { id: "B", label: "Grill Station", x: 300, y: 240, r: 30, color: "#a855f7" },
      { id: "C", label: "Drink Oasis", x: 550, y: 80, r: 30, color: "#10b981" },
      { id: "D", label: "Dessert Bar", x: 550, y: 240, r: 30, color: "#10b981" },
      { id: "T", label: "Cashier (Target)", x: 780, y: 160, r: 35, color: "#f59e0b" }
    ],
    svgEdges: [
      { from: "S", to: "A", weight: "2 min" },
      { from: "S", to: "B", weight: "5 min" },
      { from: "A", to: "C", weight: "3 min" },
      { from: "A", to: "B", weight: "1 min" },
      { from: "B", to: "D", weight: "4 min" },
      { from: "C", to: "T", weight: "2 min" },
      { from: "D", to: "T", weight: "1 min" }
    ],
    slides: [
      {
        title: "Slide 1: The Big Picture",
        bullets: [
          "Dijkstra solves Single-Source Shortest Path on non-negative weighted graphs.",
          "Core Strategy: Greedy exploration via a priority queue (min-heap).",
          "Golden Rule: Never explore blindly; settle the closest verified node first."
        ]
      },
      {
        title: "Slide 2: Mechanics & Relaxation",
        bullets: [
          "Maintain distance array: dist[source] = 0, all other nodes = ∞.",
          "Pop vertex u with minimum dist[u] from min-heap.",
          "For each neighbor v: if dist[u] + weight(u,v) < dist[v], update dist[v]."
        ]
      },
      {
        title: "Slide 3: Professor Exam Traps",
        bullets: [
          "TRAP 1: Negative Edge Weights! Dijkstra FAILS with negative edges (use Bellman-Ford).",
          "TRAP 2: Time Complexity. Mentioning O(V^2) vs O((V+E) log V) with binary heap.",
          "TRAP 3: Forgetting to skip already-visited nodes when popped from heap."
        ]
      },
      {
        title: "Slide 4: Cheat-Sheet Invariant",
        bullets: [
          "Invariant: Once a node is popped from min-heap, its shortest path is FINAL.",
          "Space Complexity: O(V) for heap and distance tracking.",
          "Exam Recall: 'Dijkstra = BFS on Steroids with a Min-Heap'."
        ]
      }
    ],
    traps: [
      {
        name: "Negative Edge Weights",
        think: "Students assume Dijkstra works on any directed graph.",
        fix: "Dijkstra greedily assumes once visited, a distance cannot decrease. A negative edge breaks this invariant! You must use Bellman-Ford."
      },
      {
        name: "Complexity with Adjacency Matrix vs. Heap",
        think: "Students memorize one O((V+E)logV) formula blindly.",
        fix: "Without a min-heap (linear array scan), complexity is O(V^2). With Fibonacci heap, it's O(E + V log V). Professors test this exact distinction."
      },
      {
        name: "A* Search Relationship",
        think: "Treating A* and Dijkstra as completely separate algorithms.",
        fix: "A* is literally Dijkstra with a heuristic h(n) added to guide search. When h(n) = 0, A* reverts identically to Dijkstra."
      }
    ],
    socraticFirst: "Why does Dijkstra's algorithm fundamentally break when a graph contains even a single negative edge weight?"
  },

  respiration: {
    title: "Cellular Respiration & Krebs Cycle",
    input: "Cellular respiration converts biochemical energy from glucose into ATP through glycolysis, pyruvate oxidation, the citric acid cycle (Krebs cycle), and oxidative phosphorylation (electron transport chain). Oxygen acts as the terminal electron acceptor.",
    analogy: "Think of Cellular Respiration like a **campus fundraising concert**. **Glycolysis** is selling early tickets outside the dorm (yields quick pocket cash: 2 ATP). **Pyruvate Oxidation** is security checking tickets at the gate. The **Krebs Cycle** is the VIP revolving lounge inside: every spin shreds vouchers to harvest high-energy VIP passes (**NADH and FADH2**). Finally, the **Electron Transport Chain** is the main merch booth: those VIP passes are cashed in through a high-voltage turnstile (**ATP Synthase**) to mint 30+ gold tokens (**ATP**).",
    mappings: [
      { key: "Glucose", val: "Raw Concert Budget" },
      { key: "Glycolysis", val: "Dorm Ticket Sales (Net 2 ATP)" },
      { key: "NADH / FADH2", val: "High-Energy VIP Battery Packs" },
      { key: "ATP Synthase", val: "Hydraulic Cash Turnstile" },
      { key: "Oxygen", val: "Cleanup Crew (Electron Catchers)" }
    ],
    svgNodes: [
      { id: "S", label: "Glucose", x: 100, y: 160, r: 35, color: "#00c49f" },
      { id: "A", label: "Glycolysis (Cytoplasm)", x: 300, y: 160, r: 30, color: "#a855f7" },
      { id: "B", label: "Pyruvate Prep", x: 480, y: 160, r: 30, color: "#a855f7" },
      { id: "C", label: "Krebs Cycle", x: 650, y: 160, r: 30, color: "#10b981" },
      { id: "T", label: "ETC & ATP Synthase", x: 800, y: 160, r: 35, color: "#f59e0b" }
    ],
    svgEdges: [
      { from: "S", to: "A", weight: "+2 ATP" },
      { from: "A", to: "B", weight: "2 Pyruvate" },
      { from: "B", to: "C", weight: "Acetyl-CoA" },
      { from: "C", to: "T", weight: "NADH/FADH2" }
    ],
    slides: [
      {
        title: "Slide 1: Energy Transformation",
        bullets: [
          "Overall equation: C6H12O6 + 6O2 → 6CO2 + 6H2O + ~32 ATP.",
          "3 distinct phases: Cytoplasm (Glycolysis) & Mitochondria (Krebs + ETC).",
          "Oxygen is required only for the final oxidative phase."
        ]
      },
      {
        title: "Slide 2: The Electron Shuttles",
        bullets: [
          "NADH and FADH2 act as rechargeable chemical batteries.",
          "Each NADH yields ~2.5 ATP; each FADH2 yields ~1.5 ATP in ETC.",
          "Oxidation = Loss of electrons; Reduction = Gain of electrons."
        ]
      },
      {
        title: "Slide 3: Professor Exam Traps",
        bullets: [
          "TRAP 1: Net vs Gross ATP in Glycolysis (Gross = 4, Net = 2 ATP).",
          "TRAP 2: What happens if cyanide blocks Complex IV? (Zero proton gradient, no ATP).",
          "TRAP 3: Where does the CO2 you breathe out come from? (Krebs Cycle carbons!)."
        ]
      },
      {
        title: "Slide 4: Master Recall Invariant",
        bullets: [
          "ATP Synthase is powered by a PROTON GRADIENT (chemiosmosis), not direct enzymes.",
          "Fermentation occurs when O2 is absent to regenerate NAD+ so glycolysis continues.",
          "Memory Anchor: 'Oxygen catches the falling electrons at the bottom of the slide'."
        ]
      }
    ],
    traps: [
      {
        name: "Origin of Exhaled CO2",
        think: "Students think inhaled O2 is directly converted into exhaled CO2.",
        fix: "Inhaled O2 becomes H2O! Exhaled CO2 comes entirely from decarboxylation of glucose carbons in pyruvate prep and the Krebs cycle."
      },
      {
        name: "Net vs. Gross ATP in Glycolysis",
        think: "Writing down 4 ATP as the net yield.",
        fix: "Glycolysis consumes 2 ATP during investment and produces 4 ATP in payoff. Net gain is strictly 2 ATP."
      }
    ],
    socraticFirst: "If a poison punctures the inner mitochondrial membrane so protons leak through freely, does glycolysis stop? Why or why not?"
  },

  macro: {
    title: "Macroeconomic Supply & Demand Shifts",
    input: "Macroeconomic equilibrium occurs at the intersection of Aggregate Demand (AD) and Short-Run Aggregate Supply (SRAS). Shifts in consumer confidence, interest rates, or supply shocks cause inflationary or recessionary output gaps.",
    analogy: "Think of Aggregate Demand and Supply like the **campus Uber surge pricing after Homecoming**. **Aggregate Demand** is the crowd of 5,000 students wanting rides. **Aggregate Supply** is how many drivers are willing to pick up students in D.C. traffic. If sudden rain hits (**Negative Supply Shock**), drivers go offline: the price skyrockets (**Stagflation**) while available rides drop (**Recessionary Gap**).",
    mappings: [
      { key: "Aggregate Demand", val: "Total Student Spending Appetite" },
      { key: "Aggregate Supply", val: "Available Campus Drivers & Resources" },
      { key: "Supply Shock", val: "Sudden Torrential Rainstorm" },
      { key: "Price Level", val: "Surge Multiplier (1.0x to 3.5x)" }
    ],
    svgNodes: [
      { id: "S", label: "Initial Equilibrium", x: 150, y: 160, r: 35, color: "#00c49f" },
      { id: "A", label: "Demand Shift", x: 380, y: 90, r: 30, color: "#a855f7" },
      { id: "B", label: "Supply Shock", x: 380, y: 230, r: 30, color: "#ef4444" },
      { id: "T", label: "New Price & GDP", x: 680, y: 160, r: 35, color: "#f59e0b" }
    ],
    svgEdges: [
      { from: "S", to: "A", weight: "+Consumer Spend" },
      { from: "S", to: "B", weight: "-Raw Energy" },
      { from: "A", to: "T", weight: "Inflation Gap" },
      { from: "B", to: "T", weight: "Stagflation" }
    ],
    slides: [
      {
        title: "Slide 1: Equilibrium Basics",
        bullets: [
          "AD curve slopes downward due to Wealth, Interest Rate, and Exchange Rate effects.",
          "SRAS slopes upward due to sticky wages and sticky prices.",
          "Long-Run AS (LRAS) is strictly vertical at potential GDP."
        ]
      },
      {
        title: "Slide 2: Shifters vs. Movements",
        bullets: [
          "Change in Price Level causes MOVEMENT along the curve.",
          "Fiscal or Monetary Policy SHIFTS the Aggregate Demand curve.",
          "Resource costs (oil/energy/wages) shift Aggregate Supply."
        ]
      },
      {
        title: "Slide 3: Professor Exam Traps",
        bullets: [
          "TRAP 1: Stagflation! When SRAS shifts left, price rises while output falls.",
          "TRAP 2: Confusing Classical self-correction with Keynesian intervention.",
          "TRAP 3: Movement along AD vs shift in AD."
        ]
      },
      {
        title: "Slide 4: Summary Invariant",
        bullets: [
          "Monetary tightening (Fed raising rates) shifts AD left to cool inflation.",
          "Supply shocks cannot be fixed by demand policies without trade-offs.",
          "Memory Anchor: 'Surge pricing rises when drivers vanish'."
        ]
      }
    ],
    traps: [
      {
        name: "Movement vs Shift",
        think: "Thinking an increase in price level shifts the AD curve.",
        fix: "A change in price level is a MOVEMENT ALONG the AD curve. Only external variables (consumer confidence, government spending) SHIFT the curve."
      }
    ],
    socraticFirst: "Why does the Federal Reserve face an impossible dilemma when a recession is caused by an oil supply shock rather than a drop in consumer demand?"
  },

  quantum: {
    title: "Quantum Superposition & Entanglement",
    input: "In quantum mechanics, a qubit exists in a linear combination of basis states |0⟩ and |1⟩ (superposition) until observed. Measuring the state causes wavefunction collapse into an eigenstate with probability equal to the amplitude squared (|α|² + |β|² = 1). Quantum entanglement links two particles such that the quantum state of each cannot be described independently.",
    analogy: "Imagine spinning a coin on a desk in the **Undergrad Library**. While spinning, it isn't Heads or Tails—it's simultaneously both at once (**Superposition**). The moment you slap your hand down on the coin, you force it to become either Heads or Tails (**Wavefunction Collapse**). Now imagine two enchanted smartwatches given to roommates across campus: no matter where they stand, if one watch beeps at 2:00 PM, the other instantly buzzes (**Entanglement**)—not because they sent a radio text, but because their states are fundamentally intertwined.",
    mappings: [
      { key: "Superposition", val: "Spinning Coin (Heads & Tails at Once)" },
      { key: "Measurement", val: "Slapping Hand on Desk (Collapse)" },
      { key: "Entanglement", val: "Synchronized Campus Roommate Watches" },
      { key: "Probability", val: "Weighted Balance of the Coin" }
    ],
    svgNodes: [
      { id: "S", label: "Qubit In Superposition", x: 140, y: 160, r: 35, color: "#00c49f" },
      { id: "A", label: "State |0⟩ (Heads)", x: 380, y: 90, r: 30, color: "#a855f7" },
      { id: "B", label: "State |1⟩ (Tails)", x: 380, y: 230, r: 30, color: "#4a8fc2" },
      { id: "T", label: "Entangled Pair Collapse", x: 680, y: 160, r: 35, color: "#f59e0b" }
    ],
    svgEdges: [
      { from: "S", to: "A", weight: "|α|² Prob" },
      { from: "S", to: "B", weight: "|β|² Prob" },
      { from: "A", to: "T", weight: "Correlated" },
      { from: "B", to: "T", weight: "Instantaneous" }
    ],
    slides: [
      {
        title: "Slide 1: Foundations of Superposition",
        bullets: [
          "State vector: |ψ⟩ = α|0⟩ + β|1⟩, where α and β are complex amplitudes.",
          "Normalization constraint: |α|² + |β|² = 1 (probabilities must sum to 100%).",
          "Bloch Sphere: Geometric representation of a 2-level quantum state."
        ]
      },
      {
        title: "Slide 2: Measurement & Collapse",
        bullets: [
          "Measuring a qubit projects the state into |0⟩ or |1⟩ irreversibly.",
          "Born Rule: Probability of outcome i equals |⟨i|ψ⟩|².",
          "Measurement fundamentally disturbs the quantum system."
        ]
      },
      {
        title: "Slide 3: Professor Exam Traps",
        bullets: [
          "TRAP 1: Faster-than-light communication! Entanglement CANNOT transmit data (No-Communication Theorem).",
          "TRAP 2: Superposition is NOT 'we just don't know yet' (Bell's Theorem rules out local hidden variables).",
          "TRAP 3: Quantum Cloning is IMPOSSIBLE (No-Cloning Theorem)."
        ]
      },
      {
        title: "Slide 4: Summary Invariant",
        bullets: [
          "Superposition enables quantum parallelism in Shor's & Grover's algorithms.",
          "Entanglement is a foundational resource for quantum teleportation and cryptography.",
          "Memory Anchor: 'Spinning coin until the hand slaps down'."
        ]
      }
    ],
    traps: [
      {
        name: "Faster-Than-Light Signaling",
        think: "Believing Alice can send instantaneous morse code to Bob via entangled spins.",
        fix: "Bob's local measurement always looks 50/50 random noise until Alice shares her measurement basis over classical radio channels. No data travels FTL."
      }
    ],
    socraticFirst: "If measuring Alice's entangled particle instantly dictates the state of Bob's particle across the galaxy, why can't Alice use this to send a faster-than-light signal?"
  },

  tcp: {
    title: "TCP 3-Way Handshake & Flow Control",
    input: "Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of a stream of octets between applications. The connection is established via a 3-way handshake (SYN, SYN-ACK, ACK) using sequence numbers, and manages network congestion using sliding windows and AIMD (Additive Increase Multiplicative Decrease).",
    analogy: "Think of setting up a **study session at the library over noisy campus walkie-talkies**. You press talk and say: 'Hey, I'm ready to study, sync with me!' (**SYN, Seq=x**). Your friend replies: 'Got you! I'm ready too, acknowledging your call!' (**SYN-ACK, Seq=y, Ack=x+1**). You confirm: 'Awesome, heard you, let's begin!' (**ACK, Ack=y+1**). If either person drops the call, nobody starts speaking until the handshake is verified.",
    mappings: [
      { key: "SYN Packet", val: "'Can you hear me at table 4?'" },
      { key: "SYN-ACK", val: "'Yes I hear you, can you hear me?'" },
      { key: "ACK", val: "'Connection confirmed, opening book!'" },
      { key: "Sliding Window", val: "How many pages we can study before checking in" }
    ],
    svgNodes: [
      { id: "S", label: "Client Host", x: 140, y: 160, r: 35, color: "#00c49f" },
      { id: "A", label: "SYN Request (Seq=x)", x: 380, y: 90, r: 30, color: "#a855f7" },
      { id: "B", label: "SYN-ACK (Ack=x+1)", x: 380, y: 230, r: 30, color: "#4a8fc2" },
      { id: "T", label: "Server Connected (ACK)", x: 680, y: 160, r: 35, color: "#f59e0b" }
    ],
    svgEdges: [
      { from: "S", to: "A", weight: "Step 1: SYN" },
      { from: "A", to: "B", weight: "Step 2: SYN-ACK" },
      { from: "B", to: "T", weight: "Step 3: ACK" },
      { from: "S", to: "T", weight: "Established" }
    ],
    slides: [
      {
        title: "Slide 1: The 3-Way Handshake",
        bullets: [
          "Step 1: Client sends SYN with initial sequence number (ISN_c).",
          "Step 2: Server responds with SYN-ACK, ISN_s, and ACK = ISN_c + 1.",
          "Step 3: Client replies with ACK = ISN_s + 1. Connection ESTABLISHED."
        ]
      },
      {
        title: "Slide 2: Reliability & Flow Control",
        bullets: [
          "Cumulative ACKs acknowledge all bytes received up to that point.",
          "Sliding Window prevents sender from overflowing receiver's buffer.",
          "AIMD algorithm avoids network congestion collapse."
        ]
      },
      {
        title: "Slide 3: Professor Exam Traps",
        bullets: [
          "TRAP 1: Why 3 steps instead of 2? (To prevent duplicate delayed old packets from creating phantom connections).",
          "TRAP 2: Sequence number increment (SYN and FIN flags consume 1 sequence number!).",
          "TRAP 3: TCP vs UDP (UDP has zero handshake latency, best for real-time gaming/video)."
        ]
      },
      {
        title: "Slide 4: Summary Invariant",
        bullets: [
          "SYN floods exhaust server backlog queues (mitigated by SYN cookies).",
          "Connection teardown requires a 4-way handshake (FIN, ACK, FIN, ACK).",
          "Memory Anchor: 'SYN, SYN-ACK, ACK—verify both sides can speak and listen'."
        ]
      }
    ],
    traps: [
      {
        name: "Two-Way vs. Three-Way Handshake",
        think: "Assuming a 2-way handshake is sufficient to establish a connection.",
        fix: "In an unreliable network, a delayed obsolete SYN packet from an old aborted session could arrive at the server and trigger an unwanted connection if only 2 steps were used. The 3rd ACK proves the client is currently active."
      }
    ],
    socraticFirst: "Why is a 2-way handshake insufficient to open a reliable connection over an unreliable IP network where packets can be delayed?"
  }
};

let currentPresetKey = "dijkstra";
let currentSlideIndex = 0;
let chatMessages = [];
let deepseekApiKey = "";

// DOM Elements
const topicInput = document.getElementById("topicInput");
const refractBtn = document.getElementById("refractBtn");
const audioSummaryBtn = document.getElementById("audioSummaryBtn");
const profileSummary = document.getElementById("profileSummary");
const engineStatusBadge = document.getElementById("engineStatusBadge");

// Modal Elements
const apiModal = document.getElementById("apiModal");
const apiKeyToggleBtn = document.getElementById("apiKeyToggleBtn");
const closeModalBtn = document.getElementById("closeModalBtn");
const apiKeyInput = document.getElementById("apiKeyInput");
const saveApiKeyBtn = document.getElementById("saveApiKeyBtn");
const clearApiKeyBtn = document.getElementById("clearApiKeyBtn");
const apiStatusMessage = document.getElementById("apiStatusMessage");

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  initApiConfig();
  loadPreset("dijkstra");
  setupEventListeners();
  renderConceptMap();
  updateProfile();
  applyDeepLinks();
  registerServiceWorker();
});

// Light theme is the default (projector/daylight readable); dark is one tap away.
function initTheme() {
  let theme = null;
  try { theme = localStorage.getItem("PRISMATIC_THEME"); } catch (err) {}
  if (theme !== "light" && theme !== "dark") theme = "light";
  setTheme(theme);
}

function setTheme(theme) {
  const light = theme === "light";
  document.body.classList.toggle("light-theme", light);
  const btn = document.getElementById("themeToggleBtn");
  if (btn) btn.textContent = light ? "🌙 Dark" : "☀ Light";
  const meta = document.getElementById("themeColorMeta");
  if (meta) meta.setAttribute("content", light ? "#f4f6fa" : "#0b0e14");
  try { localStorage.setItem("PRISMATIC_THEME", theme); } catch (err) {}
}

// Deep links for staged demos: ?preset=quantum&stage=1&timer=1
function applyDeepLinks() {
  const params = new URLSearchParams(window.location.search);
  const preset = params.get("preset");
  if (preset && PRESETS[preset]) {
    loadPreset(preset);
    activatePresetButton(preset);
  }
  if (params.get("stage") === "1" && !document.body.classList.contains("stage-mode")) {
    toggleStageMode();
  }
  if (params.get("timer") === "1") startPitchTimer();
}

function activatePresetButton(key) {
  document.querySelectorAll(".pill-btn[data-preset]").forEach((b) => {
    const on = b.dataset.preset === key;
    b.classList.toggle("active", on);
    b.setAttribute("aria-pressed", String(on));
  });
}

// Offline-first: cache the demo shell so venue Wi-Fi outages can't stall the pitch.
function registerServiceWorker() {
  if ("serviceWorker" in navigator && /^https?:$/.test(window.location.protocol)) {
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("sw.js").catch(() => {});
    });
  }
}

function initApiConfig() {
  // Check localStorage or window.DEEPSEEK_CONFIG
  const stored = localStorage.getItem("PRISMATIC_DEEPSEEK_KEY");
  if (stored) {
    deepseekApiKey = stored;
  } else if (window.DEEPSEEK_CONFIG && window.DEEPSEEK_CONFIG.apiKey) {
    deepseekApiKey = window.DEEPSEEK_CONFIG.apiKey;
  }

  updateEngineStatus();
}

function updateEngineStatus() {
  if (deepseekApiKey && deepseekApiKey.startsWith("sk-")) {
    engineStatusBadge.textContent = "⚡ Live DeepSeek V4 Engine Active";
    engineStatusBadge.className = "badge badge-cyan";
  } else {
    engineStatusBadge.textContent = "● Deterministic Offline Mode";
    engineStatusBadge.className = "badge badge-status";
  }
}

function loadPreset(key) {
  currentPresetKey = key;
  currentSlideIndex = 0;
  const p = PRESETS[key];
  topicInput.value = p.input;

  // Render Analogy (Safely formatted)
  document.getElementById("analogyText").innerHTML = formatSafeMarkdown(p.analogy);

  // Render Mappings (Safely escaped)
  const mappingBox = document.getElementById("mappingTags");
  mappingBox.innerHTML = p.mappings.map(m => `
    <div class="map-tag">
      <span>${escapeHtml(m.key)}</span> → ${escapeHtml(m.val)}
    </div>
  `).join("");

  // Render Slides
  renderSlide();

  // Render Traps (Safely escaped + accessible click/key handling)
  const trapBox = document.getElementById("trapList");
  trapBox.innerHTML = p.traps.map((t) => `
    <div class="trap-card" tabindex="0" role="button" aria-expanded="false" onclick="toggleTrap(this)" onkeydown="if(event.key==='Enter'||event.key===' ')toggleTrap(this)">
      <div class="trap-header">
        <span>⚠️ ${escapeHtml(t.name)}</span>
        <span style="font-size: 0.75rem; color: var(--cyan-neon);">Click to Reveal</span>
      </div>
      <div class="trap-think"><strong>Common Mistake:</strong> ${escapeHtml(t.think)}</div>
      <div class="trap-fix"><strong>The Professor's Fix:</strong> ${escapeHtml(t.fix)}</div>
    </div>
  `).join("");

  // Init Socratic Chat
  chatMessages = [
    { sender: "ai", text: `Welcome to Socratic Sparring on ${escapeHtml(p.title)}. Let's test your active retention.` },
    { sender: "ai", text: escapeHtml(p.socraticFirst) }
  ];
  renderChat();

  // Redraw SVG
  renderConceptMap();
}

function renderSlide() {
  const p = PRESETS[currentPresetKey];
  const slide = p.slides[currentSlideIndex];
  const frame = document.getElementById("slideFrame");
  document.getElementById("slideIndicator").innerText = `Slide ${currentSlideIndex + 1} / ${p.slides.length}`;

  frame.innerHTML = `
    <div class="slide-title">${escapeHtml(slide.title)}</div>
    <ul class="slide-bullets">
      ${slide.bullets.map(b => `<li><span aria-hidden="true">▸</span> <div>${escapeHtml(b)}</div></li>`).join("")}
    </ul>
  `;
}

function toggleTrap(elem) {
  const isExpanded = elem.classList.toggle("revealed");
  elem.setAttribute("aria-expanded", isExpanded ? "true" : "false");
}

function renderConceptMap() {
  const p = PRESETS[currentPresetKey];
  const svg = document.getElementById("conceptMapSvg");
  svg.innerHTML = "";

  // Draw Edges
  p.svgEdges.forEach(e => {
    const fromNode = p.svgNodes.find(n => n.id === e.from);
    const toNode = p.svgNodes.find(n => n.id === e.to);
    if (!fromNode || !toNode) return;

    // Line
    const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
    line.setAttribute("x1", fromNode.x);
    line.setAttribute("y1", fromNode.y);
    line.setAttribute("x2", toNode.x);
    line.setAttribute("y2", toNode.y);
    line.setAttribute("stroke", "#2b3c55");
    line.setAttribute("stroke-width", "2");
    svg.appendChild(line);

    // Label
    const midX = (fromNode.x + toNode.x) / 2;
    const midY = (fromNode.y + toNode.y) / 2 - 8;
    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", midX);
    text.setAttribute("y", midY);
    text.setAttribute("fill", "#00c49f");
    text.setAttribute("font-size", "11");
    text.setAttribute("font-family", "ui-monospace, monospace");
    text.setAttribute("text-anchor", "middle");
    text.setAttribute("class", "edge-label");
    text.textContent = e.weight;
    svg.appendChild(text);
  });

  // Draw Nodes
  p.svgNodes.forEach(n => {
    // Circle
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", n.x);
    circle.setAttribute("cy", n.y);
    circle.setAttribute("r", n.r);
    circle.setAttribute("fill", "#131822");
    circle.setAttribute("stroke", n.color);
    circle.setAttribute("stroke-width", "2");
    svg.appendChild(circle);

    // Text Label
    const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
    text.setAttribute("x", n.x);
    text.setAttribute("y", n.y + 4);
    text.setAttribute("fill", "#ffffff");
    text.setAttribute("font-size", "10");
    text.setAttribute("font-weight", "bold");
    text.setAttribute("text-anchor", "middle");
    text.setAttribute("class", "node-label");
    text.textContent = n.label.length > 15 ? n.label.slice(0, 14) + "…" : n.label;
    svg.appendChild(text);
  });

  // Legend
  const legend = document.getElementById("visualLegend");
  legend.innerHTML = `
    <div class="legend-item"><span class="legend-dot" style="background:#00c49f"></span> Input / Source</div>
    <div class="legend-item"><span class="legend-dot" style="background:#a855f7"></span> Intermediate State</div>
    <div class="legend-item"><span class="legend-dot" style="background:#10b981"></span> Verified Route</div>
    <div class="legend-item"><span class="legend-dot" style="background:#f59e0b"></span> Final Target / Settle</div>
  `;
}

function renderChat() {
  const win = document.getElementById("chatWindow");
  win.innerHTML = chatMessages.map(m => `
    <div class="chat-bubble ${m.sender === 'ai' ? 'bubble-ai' : 'bubble-user'}">
      ${m.sender === 'ai' ? '<span class="bubble-speaker">Prismatic Socratic Coach</span>' : ''}
      ${escapeHtml(m.text)}
    </div>
  `).join("");
  win.scrollTop = win.scrollHeight;
}

function setupEventListeners() {
  // Preset buttons
  document.querySelectorAll(".pill-btn").forEach(btn => {
    const handlePreset = () => {
      document.querySelectorAll(".pill-btn").forEach(b => {
        b.classList.remove("active");
        b.setAttribute("aria-pressed", "false");
      });
      btn.classList.add("active");
      btn.setAttribute("aria-pressed", "true");
      loadPreset(btn.dataset.preset);
    };
    btn.addEventListener("click", handlePreset);
    btn.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        handlePreset();
      }
    });
  });

  // Modality Tabs
  document.querySelectorAll(".tab-btn").forEach(btn => {
    const handleTab = () => {
      document.querySelectorAll(".tab-btn").forEach(b => {
        b.classList.remove("active");
        b.setAttribute("aria-selected", "false");
      });
      document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));
      btn.classList.add("active");
      btn.setAttribute("aria-selected", "true");
      document.getElementById(`tab-${btn.dataset.tab}`).classList.add("active");
    };
    btn.addEventListener("click", handleTab);
    btn.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        handleTab();
      }
    });
  });

  // Diagnostic Choice Buttons (Q1 routes to the matching spectrum tab)
  document.querySelectorAll(".choice-btn").forEach(btn => {
    const handleChoice = () => {
      const parent = btn.closest(".choice-grid");
      parent.querySelectorAll(".choice-btn").forEach(b => {
        b.classList.remove("active");
        b.setAttribute("aria-pressed", "false");
      });
      btn.classList.add("active");
      btn.setAttribute("aria-pressed", "true");
      updateProfile();
      const group = btn.closest(".diag-group");
      if (group && group.dataset.q === "1") {
        const tab = document.querySelector(`.tab-btn[data-tab="${btn.dataset.val}"]`);
        if (tab) tab.click();
      }
    };
    btn.addEventListener("click", handleChoice);
    btn.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        handleChoice();
      }
    });
  });

  // Slide navigation
  document.getElementById("prevSlideBtn").addEventListener("click", () => {
    const p = PRESETS[currentPresetKey];
    if (currentSlideIndex > 0) {
      currentSlideIndex--;
      renderSlide();
    }
  });

  document.getElementById("nextSlideBtn").addEventListener("click", () => {
    const p = PRESETS[currentPresetKey];
    if (currentSlideIndex < p.slides.length - 1) {
      currentSlideIndex++;
      renderSlide();
    }
  });

  // Refract Button (renders a dynamic graph for custom freeform topics)
  refractBtn.addEventListener("click", runRefraction);

  // Audio Summary Button (prefers a natural voice when available)
  audioSummaryBtn.addEventListener("click", () => {
    const textToSpeak = PRESETS[currentPresetKey].analogy.replace(/[*_#]/g, "");
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(textToSpeak);
      utterance.rate = 1.05;
      utterance.pitch = 1.0;
      const voice = pickNaturalVoice();
      if (voice) utterance.voice = voice;
      window.speechSynthesis.speak(utterance);
      audioSummaryBtn.innerHTML = "<span>🔊 Speaking Analogy...</span>";
      utterance.onend = () => {
        audioSummaryBtn.innerHTML = "<span>🔊</span> Listen (Audio Modality)";
      };
    } else {
      alert("Audio synthesis is not supported on this browser.");
    }
  });

  // Socratic Chat Form
  const chatForm = document.getElementById("chatForm");
  const chatInput = document.getElementById("chatInput");
  chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const val = chatInput.value.trim();
    if (!val) return;

    chatMessages.push({ sender: "user", text: val });
    chatInput.value = "";
    renderChat();

    // Generate response (DeepSeek Live AI or Deterministic Fallback)
    await generateSocraticResponse(val);
  });

  document.getElementById("resetChatBtn").addEventListener("click", () => {
    const p = PRESETS[currentPresetKey];
    chatMessages = [
      { sender: "ai", text: `Dialogue reset for ${escapeHtml(p.title)}.` },
      { sender: "ai", text: escapeHtml(p.socraticFirst) }
    ];
    renderChat();
  });

  // Modal Listeners
  apiKeyToggleBtn.addEventListener("click", () => {
    apiKeyInput.value = deepseekApiKey || "";
    apiStatusMessage.textContent = "";
    apiModal.style.display = "flex";
  });

  closeModalBtn.addEventListener("click", () => {
    apiModal.style.display = "none";
  });

  saveApiKeyBtn.addEventListener("click", () => {
    const key = apiKeyInput.value.trim();
    if (key) {
      deepseekApiKey = key;
      localStorage.setItem("PRISMATIC_DEEPSEEK_KEY", key);
      apiStatusMessage.textContent = "✔ Key saved to localStorage.";
    } else {
      deepseekApiKey = "";
      localStorage.removeItem("PRISMATIC_DEEPSEEK_KEY");
      apiStatusMessage.textContent = "Key cleared. Using offline engine.";
    }
    updateEngineStatus();
    setTimeout(() => { apiModal.style.display = "none"; }, 800);
  });

  clearApiKeyBtn.addEventListener("click", () => {
    deepseekApiKey = "";
    apiKeyInput.value = "";
    localStorage.removeItem("PRISMATIC_DEEPSEEK_KEY");
    apiStatusMessage.textContent = "Key cleared. Switched to offline mode.";
    updateEngineStatus();
    setTimeout(() => { apiModal.style.display = "none"; }, 800);
  });

  // Pitch Timer (120s countdown lighting each cue segment in real time)
  document.getElementById("pitchStartBtn").addEventListener("click", startPitchTimer);
  document.getElementById("pitchResetBtn").addEventListener("click", resetPitchTimer);

  // Random / Surprise Preset Button
  const randomPresetBtn = document.getElementById("randomPresetBtn");
  if (randomPresetBtn) {
    randomPresetBtn.addEventListener("click", () => {
      const keys = Object.keys(PRESETS).filter(k => k !== currentPresetKey);
      const randomKey = keys[Math.floor(Math.random() * keys.length)];
      loadPreset(randomKey);
      activatePresetButton(randomKey);
      runRefraction();
    });
  }

  // Stage Mode (Presenter View)
  const stageModeBtn = document.getElementById("stageModeToggleBtn");
  if (stageModeBtn) {
    stageModeBtn.addEventListener("click", toggleStageMode);
  }

  // Keyboard shortcut 'P' for Stage Mode
  window.addEventListener("keydown", (e) => {
    if ((e.key === "p" || e.key === "P") && e.target.tagName !== "TEXTAREA" && e.target.tagName !== "INPUT") {
      toggleStageMode();
    }
    if (e.key === "Escape") {
      apiModal.style.display = "none";
      const phoneModal = document.getElementById("phoneModal");
      if (phoneModal) phoneModal.style.display = "none";
    }
  });

  // Theme toggle (light default, dark one tap away)
  const themeToggleBtn = document.getElementById("themeToggleBtn");
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener("click", () => {
      setTheme(document.body.classList.contains("light-theme") ? "dark" : "light");
    });
  }

  // Phone QR modal for judges
  const phoneModalBtn = document.getElementById("phoneModalBtn");
  const phoneModal = document.getElementById("phoneModal");
  const phoneModalClose = document.getElementById("phoneModalClose");
  if (phoneModalBtn && phoneModal) {
    phoneModalBtn.addEventListener("click", () => { phoneModal.style.display = "flex"; });
  }
  if (phoneModalClose && phoneModal) {
    phoneModalClose.addEventListener("click", () => { phoneModal.style.display = "none"; });
  }
  if (phoneModal) {
    phoneModal.addEventListener("click", (e) => {
      if (e.target === phoneModal) phoneModal.style.display = "none";
    });
  }

  // PartyRock one-click fallback (only shown when a URL is configured)
  initPartyRockFallback();

  // Shark Q&A theater
  renderSharkQAButtons();
  document.getElementById("qaPlayAllBtn").addEventListener("click", playFullGauntlet);
  document.getElementById("qaClearBtn").addEventListener("click", clearSharkStage);
}

function toggleStageMode() {
  const isStage = document.body.classList.toggle("stage-mode");
  const stageModeBtn = document.getElementById("stageModeToggleBtn");
  if (stageModeBtn) {
    stageModeBtn.textContent = isStage ? "🎬 Exit Stage Mode [P]" : "🎬 Stage Mode [P]";
    stageModeBtn.classList.toggle("active", isStage);
  }
}

// Shared refraction flow: custom freeform notes get an auto-mapped graph,
// active presets re-render their curated blueprint.
function runRefraction() {
  refractBtn.innerHTML = "<span>⚡ Refracting Spectrums...</span>";
  refractBtn.style.opacity = "0.7";
  setTimeout(() => {
    const customText = topicInput.value.trim();
    if (customText && customText !== PRESETS[currentPresetKey].input) {
      renderCustomConceptMap(customText);
    } else {
      renderConceptMap();
    }
    refractBtn.innerHTML = "<span>⚡ Refracted Successfully!</span>";
    refractBtn.style.opacity = "1";
    setTimeout(() => {
      refractBtn.innerHTML = "<span class=\"btn-spark\">⚡</span> Refract Into 4 Spectrums";
    }, 1500);
  }, 500);
}

function updateProfile() {
  const activeChoices = Array.from(document.querySelectorAll(".choice-btn.active")).map(b => b.innerText);
  const intake = activeChoices[0] || "Visual";
  const urgency = activeChoices[2] || "Cram Mode";
  const persona = activeChoices[4] || "Collegiate Peer";
  profileSummary.innerText = `Profile: ${intake} · ${urgency} (${persona} Persona)`;
}

// Prefer a natural/online English voice; fall back to the browser default.
function pickNaturalVoice() {
  try {
    const voices = window.speechSynthesis.getVoices();
    if (!voices || !voices.length) return null;
    return voices.find(v => /natural|online/i.test(v.name) && /^en/i.test(v.lang))
      || voices.find(v => /^en[-_]US/i.test(v.lang))
      || voices.find(v => /^en/i.test(v.lang))
      || null;
  } catch (err) {
    return null;
  }
}

// Prime the async voice list on supporting browsers (Chrome loads lazily).
if ("speechSynthesis" in window && typeof window.speechSynthesis.onvoiceschanged !== "undefined") {
  window.speechSynthesis.onvoiceschanged = () => window.speechSynthesis.getVoices();
}

// ---------------------------------------------------------------- Pitch timer
let pitchTimerId = null;
let pitchStartTs = 0;

function startPitchTimer() {
  resetPitchTimer(false);
  pitchStartTs = Date.now();
  document.getElementById("pitchStartBtn").textContent = "Restart Pitch";
  pitchTimerId = setInterval(updatePitchTimer, 250);
  updatePitchTimer();
}

function resetPitchTimer(clearLabel = true) {
  if (pitchTimerId) clearInterval(pitchTimerId);
  pitchTimerId = null;
  const timer = document.getElementById("pitchTimer");
  timer.textContent = "2:00";
  timer.classList.remove("overtime");
  document.querySelectorAll("#cueChips .cue-chip").forEach(c => c.classList.remove("lit", "done"));
  if (clearLabel) document.getElementById("pitchStartBtn").textContent = "Start Pitch";
}

function updatePitchTimer() {
  const elapsed = Math.floor((Date.now() - pitchStartTs) / 1000);
  const remaining = 120 - elapsed;
  const timer = document.getElementById("pitchTimer");
  if (remaining >= 0) {
    timer.textContent = `${Math.floor(remaining / 60)}:${String(remaining % 60).padStart(2, "0")}`;
  } else {
    timer.textContent = `+${Math.floor(-remaining / 60)}:${String(-remaining % 60).padStart(2, "0")}`;
    timer.classList.add("overtime");
  }
  document.querySelectorAll("#cueChips .cue-chip").forEach(chip => {
    const start = Number(chip.dataset.start);
    const end = Number(chip.dataset.end);
    chip.classList.toggle("lit", elapsed >= start && elapsed < end);
    chip.classList.toggle("done", elapsed >= end);
  });
  if (elapsed > 180) resetPitchTimer(); // auto-stop 60s past overtime
}

// ------------------------------------------------- PartyRock fallback link
function initPartyRockFallback() {
  const url = (window.DEEPSEEK_CONFIG && window.DEEPSEEK_CONFIG.partyRockUrl)
    || (window.PRISMATIC_CONFIG && window.PRISMATIC_CONFIG.partyRockUrl)
    || "";
  if (!url) return;
  const link = document.getElementById("partyRockLink");
  link.href = url;
  link.style.display = "";
}

// --------------------------------------- Dynamic graph for custom topics
// Builds a horizontal concept chain from freeform notes so the visual
// spectrum never shows a stale preset graph for a custom topic.
function renderCustomConceptMap(text) {
  const sentences = text.split(/[\n.!?]+/).map(s => s.trim()).filter(s => s.length > 24).slice(0, 5);
  const palette = ["#00c49f", "#a855f7", "#a855f7", "#10b981", "#f59e0b"];
  const labels = sentences.length
    ? sentences.map(s => s.split(/\s+/).slice(0, 5).join(" "))
    : ["Custom Topic"];
  const nodes = labels.map((label, i) => ({
    id: `N${i}`,
    label,
    x: 100 + i * (700 / Math.max(labels.length - 1, 1)),
    y: 160,
    r: i === 0 || i === labels.length - 1 ? 35 : 30,
    color: palette[Math.min(i, palette.length - 1)]
  }));
  const svg = document.getElementById("conceptMapSvg");
  svg.setAttribute("viewBox", "0 0 900 320");
  svg.innerHTML = "";
  const NS = "http://www.w3.org/2000/svg";
  nodes.forEach((n, i) => {
    if (i > 0) {
      const prev = nodes[i - 1];
      const line = document.createElementNS(NS, "line");
      line.setAttribute("x1", prev.x + prev.r);
      line.setAttribute("y1", prev.y);
      line.setAttribute("x2", n.x - n.r);
      line.setAttribute("y2", n.y);
      line.setAttribute("stroke", "#2b3c55");
      line.setAttribute("stroke-width", "2");
      svg.appendChild(line);
      const tag = document.createElementNS(NS, "text");
      tag.setAttribute("x", (prev.x + n.x) / 2);
      tag.setAttribute("y", n.y - 44);
      tag.setAttribute("fill", "#00c49f");
      tag.setAttribute("font-size", "11");
      tag.setAttribute("font-family", "ui-monospace, monospace");
      tag.setAttribute("text-anchor", "middle");
      tag.setAttribute("class", "edge-label");
      tag.textContent = `step ${i}`;
      svg.appendChild(tag);
    }
    const circle = document.createElementNS(NS, "circle");
    circle.setAttribute("cx", n.x);
    circle.setAttribute("cy", n.y);
    circle.setAttribute("r", n.r);
    circle.setAttribute("fill", "#131822");
    circle.setAttribute("stroke", n.color);
    circle.setAttribute("stroke-width", "2");
    svg.appendChild(circle);
    const text = document.createElementNS(NS, "text");
    text.setAttribute("x", n.x);
    text.setAttribute("y", n.y + 4);
    text.setAttribute("fill", "#ffffff");
    text.setAttribute("font-size", "10");
    text.setAttribute("font-weight", "bold");
    text.setAttribute("text-anchor", "middle");
    text.setAttribute("class", "node-label");
    text.textContent = n.label.length > 18 ? n.label.slice(0, 17) + "…" : n.label;
    svg.appendChild(text);
  });
  document.getElementById("visualLegend").innerHTML = `
    <div class="legend-item"><span class="legend-dot" style="background:#00c49f"></span> Custom topic flow (auto-mapped)</div>
    <div class="legend-item"><span class="legend-dot" style="background:#f59e0b"></span> Final takeaway</div>
  `;
}

// Generate response: Live DeepSeek V4 Flash or Deterministic Engine
async function generateSocraticResponse(userText) {
  // If API key is present, attempt live DeepSeek call
  if (deepseekApiKey && deepseekApiKey.startsWith("sk-")) {
    try {
      const p = PRESETS[currentPresetKey];
      const activeChoices = Array.from(document.querySelectorAll(".choice-btn.active")).map(b => b.innerText);
      const persona = activeChoices[4] || "Collegiate Peer";

      const systemPrompt = `You are Prismatic's Socratic Sparring Coach for college students studying ${p.title}. 
Persona: ${persona}.
STRICT MANDATE:
1. Limit your response to AT MOST TWO concise sentences.
2. Never lecture, dump text, or give away answers directly.
3. Validate student insight briefly, then ask ONE progressive Socratic question testing an edge case or mechanism.`;

      const response = await fetch("https://api.deepseek.com/chat/completions", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${deepseekApiKey}`
        },
        body: JSON.stringify({
          model: "deepseek-chat",
          messages: [
            { role: "system", content: systemPrompt },
            { role: "assistant", content: p.socraticFirst },
            { role: "user", content: userText }
          ],
          max_tokens: 120,
          temperature: 0.7
        })
      });

      if (response.ok) {
        const data = await response.json();
        let aiReply = data.choices[0].message.content.trim();
        // Ensure 2-sentence hard cap even from API
        const sentences = aiReply.match(/[^.!?]+[.!?]+/g) || [aiReply];
        if (sentences.length > 2) {
          aiReply = sentences.slice(0, 2).join(" ");
        }
        chatMessages.push({ sender: "ai", text: aiReply });
        renderChat();
        return;
      }
    } catch (err) {
      console.warn("DeepSeek API call failed, falling back to local deterministic engine:", err);
    }
  }

  // Deterministic Offline Fallback (Guaranteed zero latency, 2-sentence bound)
  setTimeout(() => {
    const lower = userText.toLowerCase();
    let aiReply = "";

    if (currentPresetKey === "dijkstra") {
      if (lower.includes("negative") || lower.includes("visited") || lower.includes("decrease") || lower.includes("bellman") || lower.includes("cycle")) {
        aiReply = "Spot on. Once Dijkstra pops a node, it assumes that distance is permanently locked. What algorithm would you swap in to handle negative weights?";
      } else {
        aiReply = "You're getting warm! Think about the greedy step: once a node is popped from the min-heap, can its distance ever decrease if an edge is negative?";
      }
    } else if (currentPresetKey === "respiration") {
      if (lower.includes("continue") || lower.includes("glycolysis") || lower.includes("cytoplasm") || lower.includes("anaerobic")) {
        aiReply = "Exactly right. Glycolysis happens in the cytoplasm and doesn't directly depend on the proton gradient. What happens to the overall ATP yield?";
      } else {
        aiReply = "Careful: remember where glycolysis happens vs where the proton leak occurs. Does glycolysis require the inner mitochondrial membrane?";
      }
    } else {
      aiReply = "Good instinct. A supply shock shifts the curve left, raising prices while shrinking output. If the Fed raises interest rates, which curve moves next?";
    }

    chatMessages.push({ sender: "ai", text: aiReply });
    renderChat();
  }, 350);
}

// ------------------------------------------------- Shark Q&A theater
// Scripted judge-vs-founder exchanges (verbatim from PRESENTER_TALKING_POINTS.md).
// Fully offline: makes the demo present itself with one click.
const SHARK_QA = [
  {
    short: "Q1 · ChatGPT?",
    q: "How does this differ from typing 'explain this to me' into ChatGPT?",
    a: "ChatGPT is passive text generation: it dumps 800 words that cause cognitive glaze. Prismatic is an agentic multi-widget pipeline — a 30-second diagnostic triage plus 4 modalities, including a Socratic partner that forces active recall instead of lecturing."
  },
  {
    short: "Q2 · Why Quick?",
    q: "Why did you use Amazon Quick instead of coding a frontend from scratch?",
    a: "Velocity and multi-model orchestration. In a 75-minute sprint, hand-coding auth, state, and Bedrock calls invites bugs. Quick's Apps mode let our 10-person team chain inputs into text, image, and chatbot widgets on one screen with zero boilerplate."
  },
  {
    short: "Q3 · Cheating?",
    q: "How do you prevent students from using this to cheat?",
    a: "Prismatic is engineered for retention, not answer generation. The Socratic module is capped at 2 sentences and asks conceptual 'why' questions. It cannot write essays — it trains students to master mechanics for in-person exams."
  },
  {
    short: "Q4 · Revenue?",
    q: "What is your revenue and distribution model?",
    a: "B2B university licensing integrated into Canvas, plus a freemium student tier. Universities already spend millions on retention — Prismatic directly lifts course completion rates."
  },
  {
    short: "Q5 · Hallucinations?",
    q: "How do you guarantee your Socratic AI won't hallucinate incorrect facts before an exam?",
    a: "Dual-layer guardrails: strict zero-shot syllabus grounding that penalizes extrapolation, plus a Socratic engine hard-capped to 2 sentences in inquiry-only mode — it never asserts facts, it interrogates them."
  },
  {
    short: "Q6 · Quick vs Amplify?",
    q: "Why Amazon Quick over a custom Next.js app on AWS Amplify?",
    a: "Zero infrastructure attack surface with enterprise IAM governance. Quick gives native multi-widget chaining and serverless Bedrock scaling in 60 minutes — campus IT can approve it for 50,000 students without auditing custom backends."
  }
];

let sharkQaRunId = 0;

function renderSharkQAButtons() {
  const grid = document.getElementById("qaQuestionGrid");
  if (!grid) return;
  grid.innerHTML = SHARK_QA.map((item, i) =>
    `<button class="qa-btn" data-qa="${i}">🦈 ${escapeHtml(item.short)}</button>`
  ).join("");
  grid.querySelectorAll(".qa-btn").forEach(btn => {
    btn.addEventListener("click", () => playSharkQA(Number(btn.dataset.qa)));
  });
}

function sharkStage() {
  return document.getElementById("qaStage");
}

function clearSharkStage() {
  sharkQaRunId++;
  const stage = sharkStage();
  if (stage) stage.innerHTML = '<div class="qa-empty">Select a question above — the sharks are waiting.</div>';
  document.querySelectorAll(".qa-btn.playing").forEach(b => b.classList.remove("playing"));
}

function appendSharkBubble(sender, speaker, text) {
  const stage = sharkStage();
  const empty = stage.querySelector(".qa-empty");
  if (empty) empty.remove();
  const div = document.createElement("div");
  div.className = `chat-bubble ${sender === "judge" ? "bubble-judge" : "bubble-founder"}`;
  const label = document.createElement("span");
  label.className = "bubble-speaker";
  label.textContent = speaker;
  const body = document.createElement("div");
  body.textContent = text;
  div.appendChild(label);
  div.appendChild(body);
  stage.appendChild(div);
  stage.scrollTop = stage.scrollHeight;
}

function playSharkQA(i) {
  const run = ++sharkQaRunId;
  const item = SHARK_QA[i];
  if (!item) return;
  document.querySelectorAll(".qa-btn.playing").forEach(b => b.classList.remove("playing"));
  const btn = document.querySelector(`.qa-btn[data-qa="${i}"]`);
  if (btn) btn.classList.add("playing");
  appendSharkBubble("judge", "🦈 Shark Judge", item.q);
  setTimeout(() => {
    if (run !== sharkQaRunId) return;
    appendSharkBubble("founder", "🎓 Prismatic Founder", item.a);
    if (btn) btn.classList.remove("playing");
  }, 1400);
}

function playFullGauntlet() {
  const run = ++sharkQaRunId;
  clearSharkStageSilent();
  let delay = 300;
  SHARK_QA.forEach((item, i) => {
    setTimeout(() => {
      if (run !== sharkQaRunId) return;
      document.querySelectorAll(".qa-btn.playing").forEach(b => b.classList.remove("playing"));
      const btn = document.querySelector(`.qa-btn[data-qa="${i}"]`);
      if (btn) btn.classList.add("playing");
      appendSharkBubble("judge", "🦈 Shark Judge", item.q);
    }, delay);
    delay += 1600;
    setTimeout(() => {
      if (run !== sharkQaRunId) return;
      appendSharkBubble("founder", "🎓 Prismatic Founder", item.a);
      const btn = document.querySelector(`.qa-btn[data-qa="${i}"]`);
      if (btn) btn.classList.remove("playing");
    }, delay);
    delay += 2200;
  });
}

function clearSharkStageSilent() {
  const stage = sharkStage();
  if (stage) stage.innerHTML = "";
}
