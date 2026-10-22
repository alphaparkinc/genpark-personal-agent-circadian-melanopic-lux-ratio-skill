# Circadian Ocular Melanopic Ratio & CIE S 026 Lux Sensor Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Cyanopic, melanopic, and photopic illuminance ratios (CIE S 026/E:2018), Equivalent Melanopic Lux (EML), and daylight pupil miosis controller. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_equivalent_melanopic_lux`: Calculate Equivalent Melanopic Lux (EML) from photopic lux and light source Melanopic Daylight Ratio (M/P).
- `audit_well_building_circadian_lighting_compliance`: Audit daytime work area melanopic lux against WELL Building Standard v2 feature L03.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_circadian_melanopic_lux_ratio_skill.server --test
```
