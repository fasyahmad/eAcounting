--
-- PostgreSQL database dump
--

-- Dumped from database version 10.7
-- Dumped by pg_dump version 10.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: members; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.members (
    id_member integer NOT NULL,
    username character varying,
    password character varying,
    ownerorbuyer integer,
    balance integer
);


ALTER TABLE public.members OWNER TO postgres;

--
-- Name: members_id_member_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.members_id_member_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.members_id_member_seq OWNER TO postgres;

--
-- Name: members_id_member_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.members_id_member_seq OWNED BY public.members.id_member;


--
-- Name: modal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.modal (
    id_barang integer NOT NULL,
    lapak_id integer,
    nama_barang character varying,
    jumlah_barang integer,
    satuan character varying,
    harga_beli integer,
    harga_jual integer
);


ALTER TABLE public.modal OWNER TO postgres;

--
-- Name: modal_id_barang_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.modal_id_barang_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.modal_id_barang_seq OWNER TO postgres;

--
-- Name: modal_id_barang_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.modal_id_barang_seq OWNED BY public.modal.id_barang;


--
-- Name: penjualan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.penjualan (
    id_penjualan integer NOT NULL,
    nama_barang character varying,
    jumlah_barang integer,
    tangal_pembelian timestamp without time zone
);


ALTER TABLE public.penjualan OWNER TO postgres;

--
-- Name: penjualan_id_penjualan_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.penjualan_id_penjualan_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.penjualan_id_penjualan_seq OWNER TO postgres;

--
-- Name: penjualan_id_penjualan_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.penjualan_id_penjualan_seq OWNED BY public.penjualan.id_penjualan;


--
-- Name: members id_member; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.members ALTER COLUMN id_member SET DEFAULT nextval('public.members_id_member_seq'::regclass);


--
-- Name: modal id_barang; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modal ALTER COLUMN id_barang SET DEFAULT nextval('public.modal_id_barang_seq'::regclass);


--
-- Name: penjualan id_penjualan; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.penjualan ALTER COLUMN id_penjualan SET DEFAULT nextval('public.penjualan_id_penjualan_seq'::regclass);


--
-- Data for Name: members; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.members (id_member, username, password, ownerorbuyer, balance) FROM stdin;
1	fasyahmad	123	1	0
2	emad	123	2	1200000
3	siOcong	123	1	0
\.


--
-- Data for Name: modal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.modal (id_barang, lapak_id, nama_barang, jumlah_barang, satuan, harga_beli, harga_jual) FROM stdin;
2	1	panci	3	Unit	30000	50000
5	1	dispenser	4	unit	200000	300000
1	1	hihid	2	Unit	20000	50000
8	3	kulkas	5	Unit	3000	10000
9	1	meja	5	unit	250000	400000
4	3	gelas	4	Unit	3000	10000
10	1	kursi	15	unit	100000	200000
11	1	lemari	3	unit	110000	120000
\.


--
-- Data for Name: penjualan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.penjualan (id_penjualan, nama_barang, jumlah_barang, tangal_pembelian) FROM stdin;
2	hihid	1	2019-04-20 00:00:00
3	hihid	1	2019-04-20 00:00:00
4	hihid	1	2019-04-20 00:00:00
5	hihid	2	2019-04-20 00:00:00
6	gelas	1	2019-04-20 00:00:00
7	gelas	2	2019-04-02 00:00:00
8	lemari	1	2019-04-03 00:00:00
9	lemari	1	2019-04-03 00:00:00
10	lemari	2	2019-04-02 00:00:00
11	lemari	2	2019-04-03 00:00:00
12	lemari	2	2019-04-03 00:00:00
13	lemari	1	2019-04-20 00:00:00
14	kursi	5	2019-04-20 00:00:00
15	lemari	2	2019-04-04 00:00:00
16	lemari	2	2019-04-03 00:00:00
17	lemari	2	2019-04-04 00:00:00
\.


--
-- Name: members_id_member_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.members_id_member_seq', 3, true);


--
-- Name: modal_id_barang_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.modal_id_barang_seq', 11, true);


--
-- Name: penjualan_id_penjualan_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.penjualan_id_penjualan_seq', 17, true);


--
-- Name: members members_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.members
    ADD CONSTRAINT members_pkey PRIMARY KEY (id_member);


--
-- Name: modal modal_nama_barang_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modal
    ADD CONSTRAINT modal_nama_barang_key UNIQUE (nama_barang);


--
-- Name: modal modal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modal
    ADD CONSTRAINT modal_pkey PRIMARY KEY (id_barang);


--
-- Name: penjualan penjualan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.penjualan
    ADD CONSTRAINT penjualan_pkey PRIMARY KEY (id_penjualan);


--
-- Name: modal modal_lapak_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.modal
    ADD CONSTRAINT modal_lapak_id_fkey FOREIGN KEY (lapak_id) REFERENCES public.members(id_member);


--
-- Name: penjualan penjualan_nama_barang_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.penjualan
    ADD CONSTRAINT penjualan_nama_barang_fkey FOREIGN KEY (nama_barang) REFERENCES public.modal(nama_barang);


--
-- PostgreSQL database dump complete
--

