import torch


class MultiLabelEmbedding(torch.nn.Module):
    """ Multi-label embedding for a fixed number of labels per data point

    Examples:
    ---------
    examples = [[1, 2, 4], [0, 1, 2], [2, 1, 4], [3, 2, 1]]
    examples = torch.tensor(examples)
    layer1 = MultiLabelEmbedding(
        vocab_size=500000, embed_size=300, random_state=42)
    y = layer1(examples)
    """
    def __init__(self,
                 vocab_size: int = None,
                 embed_size: int = None,
                 random_state: int = None,
                 device: str = None,
                 dtype: str = None):
        super(MultiLabelEmbedding, self).__init__()
        # store hyper params
        self.vocab_size = vocab_size   # v
        self.embed_size = embed_size   # e
        # layers
        self.weight = torch.nn.parameter.Parameter(
            torch.empty((self.vocab_size, self.embed_size),
                        **{'device': device, 'dtype': dtype}))
        # initialize layer weights
        if random_state:
            torch.manual_seed(random_state)
        # initialize layer weights
        self._reset_parameters()

    def _reset_parameters(self) -> None:
        torch.nn.init.normal_(self.weight, mean=0.0, std=0.2745960056781769)

    def forward(self, inputs: torch.int64):
        h = self.weight[inputs]
        h = h.sum(axis=-2)  # vorletzte Dim muss es sein.
        return h
