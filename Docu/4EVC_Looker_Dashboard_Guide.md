# Guía de Configuración y Navegación del Panel de Looker Studio (4EVC)

Esta guía paso a paso describe cómo configurar el **Panel de Control de Investigación y Ejecución de Trades de 4EVC (Earnings Volatility Crunch)** en Looker Studio (anteriormente Google Data Studio) completamente en español.

---

## 1. Prerrequisitos y Fuentes de Datos de BigQuery

Asegúrate de que las 4 vistas de BigQuery se hayan desplegado ejecutando:
```bash
poetry run python Scripts/BigQuery/views/deploy_all_views.py
```

### Vistas Conectadas en Looker Studio

| Nombre de la Fuente | ID Completo de la Vista en BigQuery | Propósito |
| :--- | :--- | :--- |
| **`ds_trade_sequence`** | `bav-personal-cloud.develop.v_4EVC_trade_execution_sequence` | Secuencia de operaciones ($1..N$), PnL acumulado, drawdowns y duración. |
| **`ds_trade_flow`** | `bav-personal-cloud.develop.v_4EVC_trade_flow` | Flujo del ciclo de vida de las órdenes (Sankey: Entrada $\rightarrow$ Resultado $\rightarrow$ Motivo de Salida). |
| **`ds_decile_signals`** | `bav-personal-cloud.develop.v_4EVC_decile_signals` | Gráficos de investigación de retorno por deciles para parámetros (`slope`, `vol_ratio`, `ivrv_ratio`). |
| **`ds_backtest_comparison`** | `bav-personal-cloud.develop.v_4EVC_backtest_execution_comparison` | Matriz de métricas comparativas para $1:N$ backtests. |

---

## 2. Barra Superior de Filtros Globales

Coloca estos controles en la parte superior de **todas las páginas** para filtrar dinámicamente todo el panel.

### Filtro 1: Selector de Ejecución de Backtest
* **Navegación**: Menú Superior $\rightarrow$ **Insertar $\rightarrow$ Control $\rightarrow$ Lista desplegable**
* **Fuente de Datos**: `ds_trade_sequence`
* **Campo de Control**: `backtest_run_id`
* **Etiqueta Visible**: `"Seleccionar Ejecución de Backtest (1:N)"`

### Filtro 2: Selector de Activo Subyacente
* **Navegación**: Menú Superior $\rightarrow$ **Insertar $\rightarrow$ Control $\rightarrow$ Lista desplegable**
* **Fuente de Datos**: `ds_trade_sequence`
* **Campo de Control**: `underlying`
* **Etiqueta Visible**: `"Filtrar por Activo Subyacente"`

### Filtro 3: Selector de Motivo de Cierre
* **Navegación**: Menú Superior $\rightarrow$ **Insertar $\rightarrow$ Control $\rightarrow$ Lista desplegable**
* **Fuente de Datos**: `ds_trade_sequence`
* **Campo de Control**: `exit_reason`
* **Etiqueta Visible**: `"Filtrar por Motivo de Cierre"`

---

## 3. Página 1: Ejecución de Órdenes y Ciclo de Vida de Trades

### Gráfico 1.1: Curva de PnL Acumulado por Secuencia de Ejecución (Gráfico de Líneas)
* **Navegación**: **Insertar $\rightarrow$ Gráfico de Líneas**
* **Fuente de Datos**: `ds_trade_sequence`
* **Pestaña Datos**:
  * **Dimensión**: `trade_seq` (Tipo = **Número**)
  * **Dimensión de Desglose**: `backtest_run_id` (Dibuja $N$ líneas para comparar backtests)
  * **Métrica**: `running_pnl` (Nombre visible: **`PnL Acumulado`**, Agregación = **SUM** o **AVG**)
  * **Ordenar**: `trade_seq` Ascendente
* **Pestaña Estilo**:
  * **Título del Gráfico**: `"PnL Acumulado por Secuencia de Operaciones (1..N)"`
  * **Título Eje X**: `"Número de Secuencia de Operación (1..N)"`
  * **Título Eje Y**: `"Retorno Realizado Acumulado (PnL %)"`

### Gráfico 1.2: Perfil de Drawdown Secuencial (Gráfico de Área)
* **Navegación**: **Insertar $\rightarrow$ Gráfico de Área**
* **Fuente de Datos**: `ds_trade_sequence`
* **Pestaña Datos**:
  * **Dimensión**: `trade_seq`
  * **Dimensión de Desglose**: `backtest_run_id`
  * **Métrica**: `drawdown` (Nombre visible: **`Drawdown (%)`**)
  * **Ordenar**: `trade_seq` Ascendente
* **Pestaña Estilo**:
  * **Color de la Serie**: Rojo / Carmesí (`#D32F2F`)
  * **Título Eje Y**: `"Drawdown de Pico a Valle (%)"`

### Gráfico 1.3: Flujo del Ciclo de Vida de las Órdenes (Diagrama Sankey)
* **Navegación**: **Visualizaciones de la Comunidad $\rightarrow$ Diagrama Sankey**
* **Fuente de Datos**: `ds_trade_flow`
* **Pestaña Datos**:
  * **Dimensión de Origen**: `source_node`
  * **Dimensión de Destino**: `target_node`
  * **Métrica de Peso**: `trade_count` (Nombre visible: **`Número de Operaciones`**)
* **Trayectoria**: `Todas las Órdenes 4EVC` $\rightarrow$ `Ganadoras` / `Perdedoras` $\rightarrow$ `Toma de Ganancias` / `Stop Loss` / `Seguridad DTE` / `Salida por Tiempo`

---

## 4. Página 2: Gráficos de Investigación por Deciles (Optimizador de Parámetros)

Esta página correlaciona los parámetros de entrada del algoritmo (`slope`, `vol_ratio`, `ivrv_ratio`) con el retorno medio realizado a lo largo de 10 deciles.

### Gráfico 2.1: Deciles de Slope vs Retorno Medio ("Salto de Retorno Medio por Decil de Slope")
* **Navegación**: **Insertar $\rightarrow$ Gráfico de Líneas**
* **Fuente de Datos**: `ds_decile_signals`
* **Pestaña Datos**:
  * **Dimensión**: `decile_range_label` (Rangos intervalares como `(-0.0147, -0.0108]`)
  * **Métrica 1**: `mean_pnl` (Cambiar nombre visible a: **`Retorno Medio (slope)`**)
  * **Métrica 2**: `zero_pnl_benchmark` (Cambiar nombre visible a: **`Línea Base PnL Cero`**)
  * **Ordenar**: `decile_bucket` Ascendente
* **Filtro del Gráfico (Nivel Gráfico)**:
  * Hacer clic en **Añadir Filtro** en Propiedades del Gráfico $\rightarrow$ **Crear Filtro**:
  * **Regla**: Incluir `metric_name` **Igual a (=)** `slope`
* **Pestaña Estilo**:
  * **Título del Gráfico**: `"Salto de Retorno Medio por Decil de Slope"`
  * **Serie 1 (`mean_pnl`)**: Color de línea = Azul (`#1976D2`), Mostrar Puntos/Marcadores = **Activado**, Tamaño de Punto = 6px.
  * **Serie 2 (`zero_pnl_benchmark`)**: Color de línea = Rojo (`#E53935`), Estilo de línea = **Discontinua (Dashed)**.
  * **Título Eje X**: `"Rango Decil de Slope"`
  * **Etiquetas Eje X**: Rotación a **45°**
  * **Título Eje Y**: `"Retorno Realizado Medio (PnL)"`

### Gráfico 2.2: Deciles de Ratio de Volatilidad (`vol_ratio`)
* **Navegación**: Duplicar Gráfico 2.1 (Copiar/Pegar)
* **Actualizar Filtro**: Cambiar regla de filtro a `metric_name` **Igual a (=)** `vol_ratio`
* **Título del Gráfico**: `"Salto de Retorno Medio por Decil de Vol Ratio"`
* **Etiqueta Serie 1**: **`Retorno Medio (vol_ratio)`**
* **Título Eje X**: `"Rango Decil de Vol Ratio"`

### Gráfico 2.3: Deciles de Ratio IV/RV (`ivrv_ratio`)
* **Navegación**: Duplicar Gráfico 2.1 (Copiar/Pegar)
* **Actualizar Filtro**: Cambiar regla de filtro a `metric_name` **Igual a (=)** `ivrv_ratio`
* **Título del Gráfico**: `"Salto de Retorno Medio por Decil de IV/RV Ratio"`
* **Etiqueta Serie 1**: **`Retorno Medio (ivrv_ratio)`**
* **Título Eje X**: `"Rango Decil de IV/RV Ratio"`

---

## 5. Página 3: Matriz Comparativa de Backtests 1:N

### Sección de Tarjetas KPI
* **Navegación**: **Insertar $\rightarrow$ Tarjeta de Resultados (Scorecard)**
* **Fuente de Datos**: `ds_backtest_comparison`
* **Métricas**:
  1. `total_trades` (Nombre visible: **`Total de Operaciones`**)
  2. `win_rate` (Nombre visible: **`Tasa de Acierto (%)`**, Formato = Porcentaje)
  3. `total_realized_pnl` (Nombre visible: **`PnL Total Realizado (%)`**, Formato = Porcentaje)
  4. `max_trade_drawdown` (Nombre visible: **`Drawdown Máximo (%)`**, Formato = Porcentaje)

### Tabla Matriz Comparativa (Tabla con Mapa de Calor)
* **Navegación**: **Insertar $\rightarrow$ Tabla con Mapa de Calor**
* **Fuente de Datos**: `ds_backtest_comparison`
* **Pestaña Datos**:
  * **Dimensión**: `backtest_run_id` (Nombre visible: **`ID de Ejecución de Backtest`**)
  * **Métricas**:
    1. `total_trades` (Nombre: **`Total Operaciones`**)
    2. `win_rate` (Nombre: **`Tasa Acierto`**)
    3. `total_realized_pnl` (Nombre: **`PnL Realizado`**)
    4. `avg_trade_pnl` (Nombre: **`PnL Promedio/Trade`**)
    5. `max_trade_drawdown` (Nombre: **`Max Drawdown`**)
    6. `avg_holding_hours` (Nombre: **`Duración Media (Horas)`**)
    7. `avg_slope_at_entry` (Nombre: **`Slope Medio Entrada`**)
    8. `avg_vol_ratio_at_entry` (Nombre: **`Vol Ratio Medio Entrada`**)
  * **Ordenar**: `total_realized_pnl` Descendente
* **Pestaña Estilo**:
  * Activar **Mapa de Calor** para `win_rate` y `total_realized_pnl` (Verde para valores altos, Rojo para valores bajos).

---

## 6. Esquema de Navegación del Panel

```
Panel de Control Looker: Estrategia 4EVC
│
├── Barra de Encabezado (Filtros Globales)
│   ├── [Desplegable] Seleccionar Ejecución de Backtest (1:N)
│   ├── [Desplegable] Filtrar por Activo Subyacente
│   └── [Desplegable] Filtrar por Motivo de Cierre
│
├── Página 1: Ejecución de Órdenes y Ciclo de Vida
│   ├── Gráfico 1.1: PnL Acumulado por Secuencia (Líneas)     -> ds_trade_sequence
│   ├── Gráfico 1.2: Perfil de Drawdown Secuencial (Área)      -> ds_trade_sequence
│   └── Gráfico 1.3: Ciclo de Vida de las Órdenes (Sankey)     -> ds_trade_flow
│
├── Página 2: Gráficos de Investigación por Deciles
│   ├── Gráfico 2.1: Salto de Retorno Medio por Decil de Slope -> ds_decile_signals (metric=slope)
│   ├── Gráfico 2.2: Salto de Retorno Medio por Decil Vol Ratio-> ds_decile_signals (metric=vol_ratio)
│   └── Gráfico 2.3: Salto de Retorno Medio por Decil IV/RV    -> ds_decile_signals (metric=ivrv_ratio)
│
└── Página 3: Matriz Comparativa de Backtests 1:N
    ├── Tarjetas KPI: Total Operaciones | Tasa Acierto % | PnL Total % | Max Drawdown %
    └── Tabla Matriz: Comparación de Backtests con Mapa de Calor -> ds_backtest_comparison
```
