CREATE TABLE [Carros] (
	id_carro integer NOT NULL,
	modelo_carro string(15) NOT NULL,
	status_carro boolean NOT NULL,
  CONSTRAINT [PK_CARROS] PRIMARY KEY CLUSTERED
  (
  [id_carro] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [Cliente] (
	id_cliente integer NOT NULL,
	nome_cliente string(30) NOT NULL,
	status_cliente boolean NOT NULL,
  CONSTRAINT [PK_CLIENTE] PRIMARY KEY CLUSTERED
  (
  [id_cliente] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [Aluguel_veiculo] (
	id_aluguel integer NOT NULL,
	id_carro binary NOT NULL,
	id_cliente integer NOT NULL,
	modelo_carro string(15) NOT NULL,
	nome_cliente string(30) NOT NULL,
	data_retirada datetime(15) NOT NULL,
	data_devolucao datetime(15) NOT NULL,
  CONSTRAINT [PK_ALUGUEL_VEICULO] PRIMARY KEY CLUSTERED
  (
  [id_aluguel] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO


ALTER TABLE [Aluguel_veiculo] WITH CHECK ADD CONSTRAINT [Aluguel_veiculo_fk0] FOREIGN KEY ([id_carro]) REFERENCES [Carros]([id_carro])
ON UPDATE CASCADE
GO
ALTER TABLE [Aluguel_veiculo] CHECK CONSTRAINT [Aluguel_veiculo_fk0]
GO
ALTER TABLE [Aluguel_veiculo] WITH CHECK ADD CONSTRAINT [Aluguel_veiculo_fk1] FOREIGN KEY ([id_cliente]) REFERENCES [Cliente]([id_cliente])
ON UPDATE CASCADE
GO
ALTER TABLE [Aluguel_veiculo] CHECK CONSTRAINT [Aluguel_veiculo_fk1]
GO
ALTER TABLE [Aluguel_veiculo] WITH CHECK ADD CONSTRAINT [Aluguel_veiculo_fk2] FOREIGN KEY ([modelo_carro]) REFERENCES [Carros]([modelo_carro])
ON UPDATE CASCADE
GO
ALTER TABLE [Aluguel_veiculo] CHECK CONSTRAINT [Aluguel_veiculo_fk2]
GO
ALTER TABLE [Aluguel_veiculo] WITH CHECK ADD CONSTRAINT [Aluguel_veiculo_fk3] FOREIGN KEY ([nome_cliente]) REFERENCES [Cliente]([nome_cliente])
ON UPDATE CASCADE
GO
ALTER TABLE [Aluguel_veiculo] CHECK CONSTRAINT [Aluguel_veiculo_fk3]
GO

